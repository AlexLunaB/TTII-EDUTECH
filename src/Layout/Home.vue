import Swal from "sweetalert2";
<template>

  <v-app :style="{background: $vuetify.theme.themes.light.background}">

    <v-layout row>


      <v-flex md3>
        <v-app :style="{background: $vuetify.theme.themes.light.background}">

          <v-container>
            <v-flex>
              <v-card class="ma-5 text-center mt-8 " shaped elevation="10">
                <v-avatar class="mt-n7" size="60" elevation="10"></v-avatar>
                <v-card-title class="layout justify-center">
                  Perfil
                </v-card-title>

                <v-card-subtitle class="layout justify-center">{{user.username}}</v-card-subtitle>
                <v-avatar class="mt-5" size="100"><img :src=user.Imagen></v-avatar>

              </v-card>

              <v-card-text>

              </v-card-text>
            </v-flex>
          </v-container>

        </v-app>
      </v-flex>
      <v-flex md9>
        <v-app :style="{background: $vuetify.theme.themes.dark.background}" class="rounded">
          <v-container>
            <v-flex>

              <v-card-text>

                <v-row>
                  <v-col cols="12">
                    <v-card
                      v-for="servicio in servicios"
                      color="#385F73"
                      dark
                      class="ma-5 text-center mt-8 "
                    >
                      <v-card-title class="headline">
                        {{servicio.servicio.servicio}}
                      </v-card-title>

                      <v-card-text>

                        <v-row align="center">
                          <v-col
                            class="display-2"
                            cols="6"
                          >
                            <h6></h6>
                          </v-col>
                          <v-col class="display-1" cols="6">
                            Tarea por hacer: {{servicio.nodo.descrip_accion}}


                          </v-col>
                        </v-row>


                      </v-card-text>

                      <v-card-actions>
                        <v-btn @click="AfectaServicio(servicio)" text>
                          Acepta Tarea
                        </v-btn>
                        <v-btn text>
                          Detalle Tarea
                        </v-btn>
                      </v-card-actions>
                    </v-card>

                  </v-col>
                </v-row>

              </v-card-text>
            </v-flex>
          </v-container>
        </v-app>
      </v-flex>

    </v-layout>
  </v-app>

</template>

<script>
  import {getAPI} from "../Api/axios-base";
  import Vue from "vue";

  export default {
    name: "Home",


    data() {
      return {
        with: 2,
        radius: 10,
        padding: 8,
        lineCap: 'round',
        date2: new Date().toISOString().substr(0, 19),
        servicios: [],

        user: {}
      }
    },
    methods: {


      AfectaServicio: function (servicio) {
        const self = this


        getAPI.post("acciones/api/Servicio_Cliente/CambiaEstadoServicio/",{servicio}).then(
          (response) => {

            console.log(response)
          }
        )


      },

      obtieneServicio: function () {

        const self = this
        getAPI.get("acciones/api/Servicio_Cliente/").then(
          (response) => {
            self.servicios = response.data

            console.log(response)
          }
        )

      },


      ObtienePerfil: function () {


        const self = this
        var u = localStorage.getItem("Usuario")
        u = JSON.parse(u)


        getAPI.get("Usuarios/users/" + u[0].username + "/").then(
          (response) => {
            self.user = response.data.user


          }
        )

      },


    },
    computed: {
      theme() {
        return this.$vuetify.theme.dark ? "dark" : "light"
      }

    },
    mounted() {
      this.obtieneServicio()
      this.ObtienePerfil()
    },


  }
</script>

<style scoped>

  .rounded {
    border-top-left-radius: 50px;
    border-bottom-left-radius: 50px;
  }

</style>
