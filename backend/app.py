from ultralytics import RTDETR
import cv2
import math
import base64
import pandas as pd

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
from unidecode import unidecode

app = Flask(__name__)

# Set up module
classes_path = './assets/classes.txt'
excel_file_path = './assets/rules.xlsx'
games_path = './assets/games.txt'

# models object detector
model = RTDETR('./assets/rtdetr_epoch30.pt')

df = pd.read_excel(excel_file_path)
features_col = df.iloc[:, -1].tolist()
features_list = [set(item.split(", ")) for item in features_col]

classes_txt = []
games = []
with open(classes_path, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    classes_txt = lines

with open(games_path, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    games = lines

def convertIdx2Class(set_index, classes):
    result_set = {classes[item] for item in set_index}
    return result_set

def detect_features(model, img):
    results = model(img, conf=0.3, save=False)
    names = results[0].names
    detected_cls = results[0].boxes.cls.tolist()
    boxes = results[0].boxes.xyxy.tolist()
    return detected_cls, boxes

def crop_image(image, coordinates):
    # coordinates of bounding box yolo x1, y1, x2, y2
    x1, y1, x2, y2 = map(int, coordinates)

    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

def jaccard_distance(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return 1 - intersection / union if union != 0 else 1   

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def crop_obj_detected(img, boxes):
    detected_images = []
    for index, box in enumerate(boxes):
        cropped_image = crop_image(img, box)

        _, encoded_image = cv2.imencode('.jpg', cropped_image)
        encoded_image = base64.b64encode(encoded_image).decode('utf-8')
        detected_images.append(encoded_image)
    return detected_images

@app.route('/api/predict', methods=['POST'])
@cross_origin(origins='*')
def predict_label():
    global classes_txt
    global features_list
    global model

    file = request.files['file']
    img = cv2.imread(file)
    temp, boxes = detect_features(model, img)
    detected_cls = [int(x) for x in temp]
    detected_cls = convertIdx2Class(detected_cls, classes_txt)

    distances_jaccard = [jaccard_distance(detected_cls, rule) for rule in features_list]
    min_index_jaccard = distances_jaccard.index(min(distances_jaccard))
    predicted_game = games[min_index_jaccard]
    detected_imgs = crop_obj_detected(img, boxes)

    return jsonify({
        'detected_cls': list(detected_cls),
        'min_index_jaccard': min_index_jaccard,
        'predicted_label': predicted_game,
        'detected_images': detected_imgs
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')