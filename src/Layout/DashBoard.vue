<template>
  <v-app>
    <navbar/>
    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>


  import Vue from "vue"


  import Navbar from "../components/Navbar";
  import Home from "./Home";
  import VueNativeSock from "vue-native-websocket";
  import store from "../store";

  export default {



    mounted() {

      //inicializa Socket
      const vm = new Vue()
      vm.$connect()



    },

    name: "DashBoard",
    components: {Home, Navbar}
  }
</script>

<style scoped>

</style>
