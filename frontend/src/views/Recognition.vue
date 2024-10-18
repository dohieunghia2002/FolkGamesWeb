<template>
    <div class="recognition">
        <v-container>
            <v-row>
                <v-col cols="12">
                    <h1 class="heading">Vietnamese Folk Game Recognition System</h1>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="6">
                    <v-btn variant="flat" color="blue-darken-4" @click="clickInput()">
                        Upload an image
                    </v-btn>

                    <input type="file" id="upload" accept="image/png, image/jpeg, image/jpg" hidden
                        @change="displayUploadImg()">

                    <v-btn class="btn--recognize" variant="flat" color="green-accent-4" @click="recognizeImg()">
                        <span>Predict</span>
                    </v-btn>

                    <div class="img__wrapper">
                        <img class="img" src="../assets/logo_ctu.png" alt="ảnh upload">
                    </div>
                </v-col>
                <v-col cols="6" class="result-detect__wrapper">
                    <h3>Detected features include:</h3>
                    <p>{{ detectResults }}</p>
                    <br />
                    <h3>Folk game is <strong>{{ predictedLabel }}</strong></h3>

                    <br>
                    <router-link v-if="predictedLabel.length > 0" :to="{ name: 'detail', params: { id: idPredicted } }">
                        <v-btn variant="flat" color="light-green-lighten-1">
                            View details
                        </v-btn>
                    </router-link>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="3" v-for="(img, i) in detectedImages" :key="i">
                    <div class="img__container">
                        <img class="img--cropped" :src="'data:image/jpeg;base64,' + img" alt="ảnh được phát hiện">
                    </div>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            idPredicted: 1,
            detectedCls: [],
            detectResults: '',
            predictedLabel: '',
            detectedImages: []
        }
    },

    methods: {
        async displayUploadImg() {
            const inputElement = document.getElementById("upload");
            const file = inputElement.files[0];
            const imgElement = document.getElementsByClassName("img")[0];
            imgElement.src = URL.createObjectURL(file)
        },

        async clickInput() {
            const inputElement = document.getElementById("upload");
            inputElement.click();
        },

        async recognizeImg() {
            const inputElement = document.getElementById("upload");
            const file = inputElement.files[0];

            const form = new FormData()
            form.append('file', file)
            const res = await axios.post('http://127.0.0.1:9999/api/predict', form, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            const temp = await res.data.detected_cls;
            this.predictedLabel = await res.data.predicted_label;
            this.detectedImages = await res.data.detected_images;
            this.idPredicted = res.data.min_index_jaccard + 1;
            this.detectedCls = await temp.map(item => item.replace('-', ' '));
            this.detectResults = this.detectedCls.join(', ');
        }
    }
}
</script>

<style scoped>
.recognition {
    min-height: 100vh;
}

.heading {
    text-align: center;
}

.btn--recognize {
    margin-left: 20px;
}

.btn--recognize span {
    color: aliceblue;
}

.img__wrapper {
    margin-top: 2rem;
    width: 65%;
}

.img,
.img--cropped {
    width: 100%;
}

.result-detect__wrapper {
    background-color: rgb(209, 236, 249);
}
</style>