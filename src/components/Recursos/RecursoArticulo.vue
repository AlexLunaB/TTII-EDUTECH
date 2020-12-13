<template>
  <v-container>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Nuevo Artículo</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>


              <v-flex xs12>
                <v-text-field
                  v-model="titulo"
                  label="Título del artículo*"
                ></v-text-field>
                <p> {{titulo}} </p>
              </v-flex>

              <v-flex xs12>
                <v-text-field
                  v-model="descripcionA"
                  label="Descripción del artículo*"
                ></v-text-field>
                <p>{{ descripcionA }}</p>
              </v-flex>
              

              <v-flex xs12 sm6>
                <v-autocomplete
                  v-model="estado"
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
                  v-model="municipio"
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
                  v-model="categoria"
                  :items="categorias"
                  item-text="descripcion"
                  label="Categorias"
                  return-object
                ></v-autocomplete>
                {{categoria.id}}
              </v-flex>

            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false"
            >Close</v-btn
          >
          <v-btn color="blue darken-1" flat @click="dialog = false">Save</v-btn>
        </v-card-actions>
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
      dialog: true,
      articulo: {
        nombre:null,
        descripcion:null,
        estado:null,
        municipio:null,
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
      getAPI.get("api/Estados/"+ self.estado.id +"/GetMunicipio").then((res)=> {
        self.municipios = res.data
      });
    },
    obtiene_categorias: function() {
      const self=this
      getAPI.get("Recursos/api/Categorias").then((res)=> {
        self.categorias = res.data
      });
    }
  },
};
</script>

<style scoped>
</style>