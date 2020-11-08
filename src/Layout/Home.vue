import Swal from "sweetalert2";
<template>
<v-container :style="{ background: $vuetify.theme.themes.light.background }">
frfrr
</v-container>
  <!-- <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-layout row>

    </v-layout>
  </v-app> -->
</template>

<script>
import { getAPI } from "../Api/axios-base";
import Vue from "vue";

export default {
  name: "Home",

  data() {
    return {
      color: "#00AFC5",
      with: 2,
      radius: 10,
      padding: 8,
      lineCap: "round",
      date2: new Date().toISOString().substr(0, 19),
      servicios: [],

      user: {},
    };
  },
  
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
  mounted() {
    this.obtieneServicio();
    this.ObtienePerfil();
  },
};
</script>

<style scoped>

</style>
