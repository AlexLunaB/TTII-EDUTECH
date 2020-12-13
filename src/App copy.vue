<template>
  <div id="app">
    <v-app>
      <v-main style="padding: 0;">
        <router-view/>
      </v-main>
    </v-app>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>


<style scoped>
  hola{
    padding: 0;
  }
</style>
