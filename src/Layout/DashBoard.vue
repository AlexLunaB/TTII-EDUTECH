<template>
  <v-app>

    <loading :active.sync="isLoading"
        :can-cancel="false"
        :is-full-page="fullPage"></loading>

    <v-app-bar
      color="primary"
      :dark="true"
      app
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>EdutechMap</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
        hide-details
        prepend-icon="fas fa-search"
        single-line
        v-model="valor"
        v-on:keyup.enter="buscador()">
        >
      </v-text-field>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
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
  // Import component
  import Loading from 'vue-loading-overlay';
  // Import stylesheet
  import 'vue-loading-overlay/dist/vue-loading.css';

  import VueNativeSock from "vue-native-websocket";
  import store from "../store";
  import FooterComponent from "../components/FooterComponent";
  import {mapMutations, mapState} from 'vuex'


  export default {

    data() {
      return {



        fullPage: true,


        valor: ""


      }
    },

    computed:{
      ...mapState(['isLoading']),


    },
    methods: {

      ...mapMutations(['ActualizaBuscador']),

      buscador: function () {
        this.$router.push({path: 'Buscador', query: {search: this.valor}})
        this.ActualizaBuscador(this.valor)


      }
    },

    mounted() {


      //inicializa Socket
      const vm = new Vue()


    },

    name: "DashBoard",
    components: {Navbar, FooterComponent,Loading}
  }
</script>

<style scoped>
  .Dash {
    background-color: #eeeeee;
  }

  .slide-enter-active,
  .slide-leave-active {
    transition: opacity .5s, transform .5s;
  }

  .slide-enter,
  .slide-leave-to {
    opacity: 0;
    transform: translateX(-30%);
  }

</style>
