<template>
  <v-container >
  <footer id="footer" class="foot">
    <div class="center">
      <p>&copy; Prototipo de observatorio Tecnológico</p>
    </div>
  </footer>
  </v-container>
</template>

<script>
export default {
  name: "FooterComponent"
};
</script>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  height: 100px;
  line-height: 60px;
  background-color: #f5f5f5;
}
</style>