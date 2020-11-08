<template>
  <v-app>
    <navbar/>
    <v-main class="Dash">
      <transition name="slide" mode="out-in">
        <router-view></router-view>
      </transition>
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

.slide-enter-active,
.slide-leave-active{
  transition: opacity .5s, transform .5s;
}

.slide-enter,
.slide-leave-to{
  opacity: 0;
  transform: translateX(-30%);
}

</style>
