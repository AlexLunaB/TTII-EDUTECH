<template>
  <v-container fluid>
    <v-card width="100%">
      <v-toolbar flat color="#30475e" dark>
        <v-toolbar-title> {{ nombre }} </v-toolbar-title>
      </v-toolbar>
      <v-tabs vertical>
        <v-tab>
          <v-icon left> fas fa-id-badge </v-icon>
          Información de cuenta
        </v-tab>
        <v-tab>
          <v-icon left> fas fa-sliders-h </v-icon>
          Preferencias
        </v-tab>
        <v-tab>
          <v-icon left> mdi-access-point </v-icon>
          Option
        </v-tab>

        <v-tab-item>
          <v-card class="mx-auto" tile>
            <v-img
              max-height="300"
              src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
            >
              <v-row align="end" class="fill-height">
                <v-col align-self="start" class="pa-0" cols="12">
                  <v-avatar class="profile" color="grey" size="164" tile>
                    <v-img
                      src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"
                    ></v-img>
                  </v-avatar>
                </v-col>
                <v-col class="py-0">
                  <v-list-item color="rgba(0, 0, 0, .4)" dark>
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        {{ nombre }}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        {{ tipoUsuario }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
          <v-card flat>
            <v-card-text>
              <!-- Perfil -->
              <v-layout justify-center>
                <v-avatar size="150">
                  <v-img
                    src="https://randomuser.me/api/portraits/women/85.jpg"
                  ></v-img>
                </v-avatar>
              </v-layout>

              Nombre Apellidos Correo electronico
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <!-- Preferencias -->
            <v-container fluid>
              <v-subheader size="20">
                Preferencias
              </v-subheader>
              <h1>Preferencias</h1>
              <v-card-text>
                Preferencias
              </v-card-text>
              <v-row align="center">
                <v-col cols="12">
                  <v-autocomplete
                    v-model="values"
                    :items="categorias"
                    outlined
                    dense
                    chips
                    small-chips
                    item-text="descripcion"
                    label="Outlined"
                    multiple
                  ></v-autocomplete>
                </v-col>
              </v-row>
            </v-container>
            <!-- Fin Preferencias -->
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <!-- Opcion3 -->
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </v-container>
</template>

<script> 

import {getAPI} from  '../../Api/axios-base';
export default {
  data() {
    return {
      nombre: "Luis Pavel",
      apellidoP: "Varela",
      apellidoM: "Aguilar",
      tipoUsuario: "Tipo de usuario",

      values: [],
      value: null,
      categorias:[

      ],
    };
  },

  methods:{




    obtiene_clasificacion: function(){

      const self= this
          //categorias de los tipos de recursos 
     getAPI.get("Recursos/api/categorias/").then(response => { // if API sends back new access and refresh token update the store
            console.log('New access successfully generated')
            console.log(response.data)

            self.categorias=response.data
          })
       
    }


     },


  mounted(){
    this.obtiene_clasificacion()

  }

};
</script>

<style scoped>
</style>