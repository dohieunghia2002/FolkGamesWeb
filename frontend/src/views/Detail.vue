<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-img :src="product.imgPath" class="img" height="400px"></v-img>
                <h3 class="headline">{{ product.name }}</h3>
            </v-col>
        </v-row>

        <v-row v-if="product && product.gameplay">
            <v-col cols="12">
                <!-- Preparation Section -->
                <h3 class="sub-heading">Preparation</h3>
                <ul v-if="product.gameplay.Preparation">
                    <li v-for="(prep, index) in product.gameplay.Preparation" :key="index">{{ prep }}</li>
                </ul>

                <!-- How to Play Section -->
                <h3 class="sub-heading">How to Play</h3>
                <ul v-if="product.gameplay['How to Play']">
                    <li v-for="(playStep, index) in product.gameplay['How to Play']" :key="index">{{ playStep }}</li>
                </ul>

                <!-- Rules Section -->
                <h3 class="sub-heading">Rules</h3>
                <ul v-if="product.gameplay.Rules">
                    <li v-for="(rule, index) in product.gameplay.Rules" :key="index">{{ rule }}</li>
                </ul>

                <!-- Significance Section -->
                <h3 class="sub-heading">Significance</h3>
                <ul v-if="product.gameplay.Significance">
                    <li v-for="(significance, index) in product.gameplay.Significance" :key="index">{{ significance }}
                    </li>
                </ul>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            product: {}
        };
    },

    async created() {
        const productId = this.$route.params.id;
        try {
            const response = await axios.get('/data.json');
            const products = response.data;
            this.product = await products.find(p => p.id === parseInt(productId));
            this.product.imgPath = "../" + this.product.imgPath
            console.log(this.product);
        } catch (error) {
            console.error("Lỗi khi tải dữ liệu:", error);
        }
    }
};
</script>

<style scoped>
.headline {
    text-align: center;
}

p {
    text-align: justify;
    margin-top: 1rem;
}

.sub-heading {
    margin-top: 1rem;
}
</style>
