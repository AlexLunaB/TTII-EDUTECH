<template>
  <v-app>
    <navbar/>
    <v-main class="Dash">
      <router-view></router-view>
    </v-main>
    <FooterComponent/>
  </v-app>
</template>

<script>
  import Vue from "vue"
  import Navbar from "../components/Navbar";

  import VueNativeSock from "vue-native-websocket";
  import store from "../store";
  import FooterComponent from "../components/FooterComponent";

  export default {



    mounted() {

      //inicializa Socket
      const vm = new Vue()
      vm.$connect()



    },

    name: "DashBoard",
    components: {Navbar, FooterComponent}
  }
</script>

<style scoped>
.Dash{
  background-color: #eeeeee;
}

</style>
