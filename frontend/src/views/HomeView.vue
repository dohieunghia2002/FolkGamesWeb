<template>
  <div class="home">
    <v-container>
      <v-row>
        <v-col cols="12">
          <h2 class="heading">Vietnamese Folk Games</h2>
        </v-col>
      </v-row>

      <v-row v-if="jsonData">
        <v-col cols="3" v-for="item in jsonData" :key="item.id">
          <router-link class="card__router" :to="{ name: 'detail', params: { id: item.id } }">
            <v-card class="card">
              <v-img :src="item.imgPath" alt="img folk game" height="200px"></v-img>
              <v-card-title class="text-h6" style="text-align: center;">{{ item.name }}</v-card-title>
            </v-card>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      jsonData: null,
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('/data.json');
        if (response.ok) {
          const data = await response.json();
          this.jsonData = data;
          console.log(this.jsonData);
        } else {
          console.error('Error fetching data:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },
}
</script>
<style scoped>
.heading {
  text-align: center;
}

.card__router {
  text-decoration: none;
}

.card:hover {
  background-color: rgb(72, 72, 249);
  cursor: pointer;

  .text-h6 {
    color: #fff;
  }
}
</style>