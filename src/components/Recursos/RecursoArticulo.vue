<template>
  <v-container>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Agregar Nuevo Artículo</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>


              <v-flex xs12>
                <v-text-field
                  v-model="articulo.nombre"
                  label="Título del artículo*"
                ></v-text-field>
                
              </v-flex>

              <v-flex xs12>
                <v-text-field
                  v-model="articulo.descripcion"
                  label="Descripción del artículo*"
                ></v-text-field>
   
              </v-flex>
              

              <v-flex xs12 sm6>
                <v-autocomplete
                  v-model="articulo.estado"
                  :items="estados"
                  item-text="nombre"
                  return-object
                  label="Estados"
                  @change="obtiene_municipios()"
                ></v-autocomplete>
                {{estado.id}}
              </v-flex>

              <v-flex xs12>
                <v-autocomplete
                  v-model="articulo.municipio"
                  :items="municipios"
                  item-text="nombre"
                  return-object
                  label="Municipios"
                  @change="obtiene_categorias()"
                ></v-autocomplete>
                {{municipio.id}}
              </v-flex>

              <v-flex xs12>
                <v-autocomplete
                  v-model="articulo.categoria"
                  :items="categorias"
                  item-text="descripcion"
                  label="Categorias"
                  item-value = 'id'
                  multiple
                ></v-autocomplete>
                {{categoria.id}}
              </v-flex>

            </v-layout>
          </v-container>
          <small>*Campos necesarios</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red " text @click="dialog = false"
            >Cancelar</v-btn
          >
          <v-btn color="green darken-1" text @click="dialog = false; postArticulos()">Save</v-btn>
        </v-card-actions>

        <!-- <v-fab-transition>
        <v-btn
          :key="activeFab.icon"
          :color="activeFab.color"
          fab
          large
          dark
          bottom
          left
          class="v-btn--example"
        >
          <v-icon>{{ activeFab.icon }}</v-icon>
        </v-btn>
      </v-fab-transition> -->
      
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { getAPI } from "../../Api/axios-base";
export default {
  data: function () {
    return {
      estados: [],
      municipios:[],
      dialog: false,
      articulo: {
        nombre:null,
        descripcion:null,
        estado:null,
        municipio:null,
        categoria:null,
        usuario:1
      },
      estado:{
        id:null
      },
      categorias:[],
      categoria:{
        id:null
      },
      municipio:{
        id:null
      }
      
    };
  },
  mounted: function () {
    this.obtiene_estado();
  },

  methods: {
    obtiene_estado: function () {
      const self = this
      getAPI.get("api/Estados").then((response) => {
        self.estados = response.data
      });
    },
    obtiene_municipios: function () {
      const self = this
      getAPI.get("api/Estados/"+ self.articulo.estado.id +"/GetMunicipio").then((res)=> {
        self.municipios = res.data
      });
    },
    obtiene_categorias: function() {
      const self=this
      getAPI.get("Recursos/api/Categorias").then((res)=> {
        self.categorias = res.data
      });
    },
    postArticulos: async function() {
      const self = this
      await getAPI.post("Recursos/api/Articulos/",
      {"nombreRecurso":self.articulo.nombre, "descripcion":self.articulo.descripcion, 
      "Usuario":1,"estado":self.articulo.estado.id,"municipio":self.articulo.municipio.id, 
      "categoria":self.articulo.categoria}).then((res)=> {
        alert(JSON.stringify(res))

      });
    },

    showAddResource: function() {
      this.dialog = true;
    }
  },
};
</script>

<style scoped>
</style>