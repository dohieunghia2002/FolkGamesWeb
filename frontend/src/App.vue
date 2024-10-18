<template>
  <Header />
  <router-view></router-view>
  <footer class="footer">
    <p>Copyright 2024: Hieu-Nghia Do, Nhu-Phuc Nguyen, Truong-Thanh Ma, Bich-Chung Phan</p>
    <a href="https://www.ctu.edu.vn/en/" style="color: blue;">Can Tho University, Vietnam</a>
  </footer>
</template>
<script>
import Header from './components/Header.vue'

export default {
  components: {
    Header
  }
}
</script>
<style>
.footer {
  text-align: center;
  padding: 20px;
  background-color: #333;
  color: #fff;
  margin-top: 2rem;
}
</style>