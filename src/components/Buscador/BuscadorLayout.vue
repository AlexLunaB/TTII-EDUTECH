<template>
  <v-container fluid>
    <v-card class="mx-auto">
      <v-card-text>

        <v-row>
          <v-col cols="12" md="3">
            <v-card


            >

              <v-card-title class="headline text-white red lighten-3">
                Filtros
              </v-card-title>
              <v-card-text>


                <v-autocomplete
                  v-model="busqueda.estado"
                  :items="estados"
                  item-text="nombre"
                  label="Estados"
                  @change="obtiene_municipios(); Filtrado();"
                  chips
                  item-value="id"
                ></v-autocomplete>


                <v-autocomplete
                  v-model="busqueda.municipio"
                  :items="municipios"
                  item-text="nombre"
                  @change="Filtrado();"

                  label="Municipios"
                  chips
                ></v-autocomplete>
                <v-autocomplete
                  v-model="busqueda.tags"
                  :items="categorias"
                  item-text="name"
                  label="Categorias"
                  chips
                  multiple
                  @change="Filtrado();"
                ></v-autocomplete>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" md="9">
            <v-row>
                <v-col cols="12" sm="12" md="6" v-for="articulo in recursos">
                  <TarjetaRecurso :recurso="articulo"></TarjetaRecurso>

                </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>



    </v-card>


  </v-container>
</template>

<script>

  import {mapState} from 'vuex';

  import TarjetaRecurso from "../TarjetaRecurso"

  import {getAPI} from "../../Api/axios-base";

  export default {
    name: "BuscadorLayout",
    data() {
      return {
        recursos:[],
        visible: false,
        Post: [],
        categorias: [],
        estados: [],
        municipios: [],
        busqueda: {
          estado: null,
          municipio: null,
          tags: []
        }
      }
    },
    components: {TarjetaRecurso},
    computed: mapState(['buscador']),
    methods: {

      send: function () {
        const self = this

        console.log(this.busqueda)

      },


      obtiene_estado: function () {
        const self = this
        getAPI.get("api/Estados").then((response) => {
          self.estados = response.data
        });
      },
      Search: function () {


        const self = this
        getAPI.get("/Recursos/api/Articulos/?", {
          params: {
            "search": this.$route.query.search,
          }


        }).then((response) => {
           self.recursos=response.data
        });
      }, Filtrado: function () {

        var self= this

        var s = "";
        for (var i = 0; i < self.busqueda.tags.length; i++) {
          s += "&tags=" + self.busqueda.tags[i];
        }
        getAPI.get("/Recursos/api/Articulos/?"+s,  {
          params: {
            "search": this.$route.query.search,
          }


        }).then((response) => {
          self.recursos=response.data

        });
      },
      obtiene_municipios: function () {
        const self = this
        getAPI.get("api/Estados/" + self.busqueda.estado + "/GetMunicipio").then((res) => {
          self.municipios = res.data
        });
      },
      obtiene_categorias: function () {
        self = this
        getAPI.get("/Recursos/api/Articulos/Tags/").then((response) => {

          self.categorias = response.data;

        });
      }
    },


    watch: {
      buscador(newValue, oldValue) {

        this.Search()


      }

    },
    mounted() {
      this.obtiene_estado();
      this.obtiene_categorias()
      this.Search()
    }
  };
</script>

<style scoped>

</style>
