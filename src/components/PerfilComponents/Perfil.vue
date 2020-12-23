<template>
  <v-container fluid>
    <v-card width="100%">
      <v-toolbar flat color="#30475e" dark>
        <v-toolbar-title> Usuario: {{ perfil.usuario }} </v-toolbar-title>
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
                      :src=perfil.foto
                    ></v-img>
                  </v-avatar>
                </v-col>
                <v-col class="py-0">
                  <v-list-item color="rgba(0, 0, 0, .4)" dark>
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        {{ perfil.nombre }} {{perfil.apellidos}}
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
              <!-- <v-layout justify-center>
                <v-avatar size="150">
                  <v-img
                     :src=perfil.foto
                  ></v-img>
                </v-avatar>
              </v-layout> -->
              <v-layout justify-center>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title class="title"> 
                      Nombre: {{perfil.nombre}}
                    </v-list-item-title>
                    <v-list-item-title class="title">
                      Correo electrónico: {{ perfil.email }}
                    </v-list-item-title>
                    <v-list-item-title class="title">
                      Usuario: {{ perfil.usuario }}
                    </v-list-item-title>
                    <v-list-item-title class="title">
                      Municipio: {{ perfil.municipio }}
                    </v-list-item-title>
                    <v-list-item-title class="title">
                      Intereses: {{ perfil.intereses }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-layout>
              
              {{ perfil.nombre}} {{ perfil.apellidos }}
              <!-- <v-btn> </v-btn> -->
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <!-- Preferencias -->
            <v-container fluid>
              <!-- <v-subheader size="20"> Preferencias </v-subheader> -->
              <h1>Preferencias</h1>
              <v-card-text> Tags </v-card-text>
              <v-row align="center">
                <!-- <v-col cols="12">
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
                  <v-list shaped>
                    <v-list-item-group v-model="model" multiple>
                      <template v-for="(item, i) in items_list">
                        <v-divider
                          v-if="!item"
                          :key="`divider-${i}`"
                        ></v-divider>

                        <v-list-item
                          v-else
                          :key="`item-${i}`"
                          :value="item"
                          active-class="deep-purple--text text--accent-4"
                        >
                          <template v-slot:default="{ active }">
                            <v-list-item-content>
                              <v-list-item-title
                                v-text="item"
                              ></v-list-item-title>
                            </v-list-item-content>

                            <v-list-item-action>
                              <v-checkbox
                                :input-value="active"
                                color="deep-purple accent-4"
                              ></v-checkbox>
                            </v-list-item-action>
                          </template>
                        </v-list-item>
                      </template>
                    </v-list-item-group>
                  </v-list>
                </v-col>
                <v-col cols="12">
                  <v-rating
                    empty-icon="far fa-star"
                    full-icon="fas fa-star"
                    half-icon="$mdiStarHalfFull"
                    hover
                    length="5"
                    size="25"
                    value="0"
                  ></v-rating>
                  <v-btn elevation="10">Calificar</v-btn>
                </v-col> -->

                <v-col cols="12">
                  <v-toolbar flat color="transparent">
                    <v-spacer></v-spacer>
                    <v-btn icon @click="$refs.search.focus()">
                      <v-icon>mdi-magnify</v-icon>
                    </v-btn>
                  </v-toolbar>

                  <v-container class="py-0">
                    <v-row align="center" justify="start">
                      <v-col
                        v-for="(selection, i) in selections"
                        :key="selection.text"
                        class="shrink"
                      >
                        <v-chip
                          :disabled="loading"
                          close
                          @click:close="selected.splice(i, 1)"
                        >
                          <v-icon left v-text="selection.icon"></v-icon>
                          {{ selection.text }}
                        </v-chip>
                      </v-col>

                      <v-col v-if="!allSelected" cols="12">
                        <v-text-field
                          ref="search"
                          v-model="search"
                          full-width
                          hide-details
                          label="Buscar Tag"
                          single-line
                          v-on:keyup.enter="addNewTag"
                        >
                          ></v-text-field
                        >
                      </v-col>
                    </v-row>
                  </v-container>

                  <v-divider v-if="!allSelected"></v-divider>

                  <v-list>
                    <template v-for="item in categories">
                      <v-list-item
                        v-if="!selected.includes(item)"
                        :key="item.text"
                        :disabled="loading"
                        @click="selected.push(item)"
                      >
                        <v-list-item-avatar>
                          <v-icon
                            :disabled="loading"
                            v-text="item.icon"
                          ></v-icon>
                        </v-list-item-avatar>
                        <v-list-item-title
                          v-text="item.text"
                        ></v-list-item-title>
                      </v-list-item>
                    </template>
                  </v-list>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      :disabled="!selected.length"
                      :loading="loading"
                      color="purple"
                      text
                      @click="next"
                    >
                      Next
                    </v-btn>
                  </v-card-actions>
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
import { getAPI } from "../../Api/axios-base";
export default {
  data() {
    return {
      perfil: {
        email: null,
        nombre: null,
        apellidos: null,
        usuario: null,
        foto: null,
        municipio: null,
        intereses: [],
      },
      nombre: "Luis Pavel",
      apellidoP: "Varela",
      apellidoM: "Aguilar",
      tipoUsuario: "Tipo de usuario",
      emailUsuario: "luispavelvarela@gmail.com",
      values: [],
      value: null,
      categorias: [],
      items_list: ["Dog Photos", "Cat Photos", "", "Potatoes", "Carrots"],
      model: ["Carrots"],
      items: [
        {
          text: "Nature",
          icon: "mdi-nature",
        },
        {
          text: "Nightlife",
          icon: "mdi-glass-wine",
        },
        {
          text: "November",
          icon: "mdi-calendar-range",
        },
        {
          text: "Portland",
          icon: "mdi-map-marker",
        },
        {
          text: "Biking",
          icon: "mdi-bike",
        },
      ],
      loading: false,
      search: "",
      selected: [],
    };
  },

  computed: {
    allSelected() {
      return this.selected.length === this.items.length;
    },
    categories() {
      const search = this.search.toLowerCase();

      if (!search) return this.items;

      return this.items.filter((item) => {
        const text = item.text.toLowerCase();

        return text.indexOf(search) > -1;
      });
    },
    selections() {
      const selections = [];

      for (const selection of this.selected) {
        selections.push(selection);
      }

      return selections;
    },
  },

  watch: {
    selected() {
      this.search = "";
    },
  },

  methods: {
    obtiene_clasificacion: function () {
      const self = this;
      //categorias de los tipos de recursos
      getAPI.get("Recursos/api/categorias/").then((response) => {
        // if API sends back new access and refresh token update the store
        console.log("New access successfully generated");
        console.log(response.data);

        self.categorias = response.data;
      });
    },
    obtiene_datos_usuario: function () {
      const self = this;
      getAPI.get("Usuarios/api/Profile/").then((response) =>{
        console.log(response.data);
        console.log(response.data.usuario);
        self.perfil.email = response.data.usuario.email;
        self.perfil.nombre = response.data.usuario.first_name;
        self.perfil.apellidos = response.data.usuario.last_name;
        self.perfil.usuario = response.data.usuario.username;
        self.perfil.foto = response.data.foto;
        self.perfil.intereses = response.data.intereses;
      });
    },
    next() {
      this.loading = true;

      setTimeout(() => {
        this.search = "";
        this.selected = [];
        this.loading = false;
      }, 2000);
    },
    addNewTag() {
      this.items.push({ text: this.search });
    },
  },

  mounted() {
    // this.obtiene_clasificacion();
    this.obtiene_datos_usuario();
  },
};
</script>

<style scoped>
</style>