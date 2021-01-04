<template>
  <v-app>
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
        ></v-text-field>
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

  import VueNativeSock from "vue-native-websocket";
  import store from "../store";
  import FooterComponent from "../components/FooterComponent";

  export default {



    mounted() {

      //inicializa Socket
      const vm = new Vue()




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
