<template>
    <header class="header">
        <v-container>
            <v-row>
                <v-col class="head" cols="2">
                    Vi-GamesHub
                </v-col>
                <v-col class="category" cols="1">
                    <div class="category__text">
                        <router-link :to="{ name: 'home' }" class="caterogy__link">Home</router-link>
                    </div>
                </v-col>
                <v-col class="category" cols="2">
                    <div class="category__text">
                        <router-link :to="{ name: 'recognition' }" class="caterogy__link">Recognition</router-link>
                    </div>
                </v-col>
            </v-row>
        </v-container>
    </header>
</template>

<script>
export default {
    data() {
        return {
            idxUrl: 0,
            currentURL: ''
        }
    },
    mounted() {
        this.updateColor();
    },
    watch: {
        '$route.path': function () {
            this.updateColor();
        }
    },
    methods: {
        updateColor() {
            this.currentURL = this.$route.path;
            if (this.currentURL === '/') {
                this.idxUrl = 0;
            } else if (this.currentURL === '/recognition') {
                this.idxUrl = 1;
            } else {
                this.idxUrl = 2;
            }

            const categoryText = document.getElementsByClassName('category__text');
            for (let i = 0; i < categoryText.length; i++) {
                categoryText[i].style.color = "#fff";
            }
            if (this.idxUrl < 2) {
                categoryText[this.idxUrl].style.color = "blue";
            }
        }
    }
}
</script>

<style>
.header {
    height: 64px;
    background-color: rgb(20, 20, 20);
}

.category {
    cursor: pointer;
}

.category:hover {
    background-color: rgb(42, 42, 42);
    font-weight: bold;
}

.category__text,
.head {
    color: #fff;
    text-align: center;
    font-size: 1.3em;
}

.caterogy__link {
    color: inherit;
    text-decoration: none;
}
</style>
