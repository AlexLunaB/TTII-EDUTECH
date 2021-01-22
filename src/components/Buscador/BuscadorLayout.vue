<template>
  <v-container fluid>
    <v-card class="mx-auto">
      <v-card-text>

        <v-row v-if="busqueda.institucion">
          <v-col cols="12">
            <v-card >
              <v-img
                :src="busqueda.institucion.Imagen"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="500px"
              >
                <v-card-title v-text="busqueda.institucion.NombreInstitucion"></v-card-title>
              </v-img>

              <v-card-actions>
                <v-spacer></v-spacer>

              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="3">
            <v-card


            >

              <v-card-title dark class="headline text-white primary ">
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

                  item-value="id"
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
                <v-autocomplete
                  v-model="busqueda.institucion"
                  return-object
                  :items="institutos"
                  item-text="NombreInstitucion"
                  label="Instituciones o Empresas"
                  chips
                  @change="Filtrado();"
                ></v-autocomplete>
              </v-card-text>
            </v-card>
          </v-col>


          <v-col cols="12" md="9">
            <v-tabs
              v-model="tab"
              background-color="transparent"
              color="basil"
              grow
            >
              <v-tab>
                Recursos {{recursos.length}}
              </v-tab>
              <v-tab>
                Blogs {{blogs.length}}
              </v-tab>
              <v-tab>
                Usuarios
              </v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab">
              <v-tab-item>
                <v-card
                  color="basil"
                  flat
                >
                  <v-card>
                    <v-card-title>Recursos</v-card-title>
                    <v-card-text>
                      <v-row>
                        <v-col cols="12" sm="12" md="4" v-for="articulo in visiblePages">
                          <TarjetaRecurso :recurso="articulo"></TarjetaRecurso>

                        </v-col>
                      </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-pagination
                        v-model="page"
                        :length="Math.ceil( recursos.length/perPage)"
                      ></v-pagination>
                    </v-card-actions>
                  </v-card>


                </v-card>
              </v-tab-item>
              <v-tab-item>


                <v-card
                  color="basil"
                  flat
                >
                  <v-card>
                    <v-card-title>Blogs</v-card-title>
                    <v-card-text>
                      <v-row>
                        <v-col cols="12" md="6" v-for="arti in  visiblePagesblogs">
                          <SingleComponent :articulo="arti"></SingleComponent>

                        </v-col>
                      </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-pagination
                        v-model="pageblogs"
                        :length="Math.ceil( blogs.length/perPage)"
                      ></v-pagination>
                    </v-card-actions>
                  </v-card>
                </v-card>


              </v-tab-item>
            </v-tabs-items>


          </v-col>


          <v-col cols="12" md="9">

          </v-col>

        </v-row>
      </v-card-text>


    </v-card>


  </v-container>
</template>

<script>

  import {mapMutations, mapState} from 'vuex';

  import TarjetaRecurso from "../TarjetaRecurso"
  import SingleComponent from "../BlogComponents/SingleComponent"

  import {getAPI} from "../../Api/axios-base";

  export default {
    name: "BuscadorLayout",
    data() {
      return {
        tab: null,
        page: 1,
        institutos: [],
        pageblogs: 1,
        perPage: 6,
        recursos: [],
        visible: false,
        Post: [],
        blogs: [],
        categorias: [],
        estados: [],
        municipios: [],
        busqueda: {
          estado: null,
          municipio: null,
          tags: [],
          institucion: null,
        }
      }
    },
    components: {TarjetaRecurso, SingleComponent},
    computed: {
      ...mapState(['buscador']),
      visiblePages() {
        return this.recursos.slice((this.page - 1) * this.perPage, this.page * this.perPage)
      },
      visiblePagesblogs() {
        return this.blogs.slice((this.pageblogs - 1) * this.perPage, this.pageblogs * this.perPage)
      }


    },
    methods: {
      ...mapMutations(['SetLoading']),
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
        self.SetLoading(true)
        getAPI.get("/Recursos/api/Articulos/?", {
          params: {
            "search": this.$route.query.search,

          },
        }).then((response) => {
          self.recursos = response.data.recursos
          self.SetLoading(false)
        });
        getAPI.get("/Foro/api/Post/?", {

          params: {
            "search": this.$route.query.search,

          },
        }).then((response) => {
          self.SetLoading(false)
          self.blogs = response.data
        });
      },
      Filtrado: function () {

        var self = this
        self.SetLoading(true)
        var idinstituto= null
        if (self.busqueda.institucion){
          idinstituto=self.busqueda.institucion.id


        }

        var s = "";
        for (var i = 0; i < self.busqueda.tags.length; i++) {
          s += "&tags=" + self.busqueda.tags[i];
        }
        getAPI.get("/Recursos/api/Articulos/?" + s, {
          params: {
            "search": this.$route.query.search,
            "institucion": idinstituto,
            "estado": self.busqueda.estado,
            "municipio": self.busqueda.municipio
          }
        }).then((response) => {
          self.recursos = response.data.recursos
          self.SetLoading(false)

        });
      },

      get_institucion: function () {
        self = this
        getAPI.get("/api/Instituciones/").then((response) => {

          self.institutos = response.data;

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
      this.get_institucion()
    }

  };
</script>

<style scoped>

</style>
