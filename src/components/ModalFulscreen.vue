<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <!-- <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Open Dialog
        </v-btn>
      </template> -->


     
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
      >
        <v-toolbar
          dark
          color="primary"
        >
          <v-btn
            icon
            dark
            @click="dialog = false"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{headModalProp}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              dark
              text
              @click="dialog = false"
            >
              Save
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>


        
      <v-container>


        <template v-for="(value) in recursos">
          <!-- <v-img
            height="250"
            src="https://www.quo.es/wp-content/uploads/2019/10/los-cinco-trabajos-que-por-ahora-no-podra-quitarte-un-robot.jpg"
          ></v-img> -->
          <Carousel> </Carousel>

          <v-card-title>Nombre del recurso: {{value.nombreRecurso}}</v-card-title>

          <v-card-text>
            <v-row
              align="center"
              class="mx-0"
            >
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              ></v-rating>

              <div class="grey--text ml-4">
                4.5 (413)
              </div>
            </v-row>

            <div class="my-4 subtitle-1">
              $ • Italian, Cafe
            </div>

            <div>ID: {{value.id}}</div>
            <div>Usuario: {{value.Usuario}}</div>
            <div>Descripcion: {{value.descripcion}}</div>
            <div>Fecha de creacion: {{value.fechaCreacion}}</div>
            <div>Fecha de modificación: {{value.fechaModificacion}}</div>
            <div>Estado de procedencia: {{value.estado}}</div>
            <div>Municipio de procedencia: {{value.municipio}}</div>

          </v-card-text>

          <v-divider class="mx-4"></v-divider>

          <v-card-title>Tonight's availability</v-card-title>

          <v-card-text>
            <v-chip-group
              v-model="selection"
              active-class="deep-purple accent-4 white--text"
              column
            >
              <v-chip>5:30PM</v-chip>

              <v-chip>7:30PM</v-chip>

              <v-chip>8:00PM</v-chip>

              <v-chip>9:00PM</v-chip>
            </v-chip-group>
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="deep-purple lighten-2"
              text
              @click="reserve"
            >
              Reserve
            </v-btn>
          </v-card-actions>
        </template>

      </v-container>
      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>

import {getAPI} from '../Api/axios-base'
import Carousel from '../components/Carousel'

getAPI()
  export default {
    data () {
      return {
        dialog: false,
        loading: false,
        selection: 1,
        headModalProp: String,
        contentModalProp: String,
        recursos: []
      }
    },
    props: {
      
    },
    components: {
      Carousel
    },
    methods: {
      showModal: function() {
      this.dialog = true;
      },

      setTextModal: function (headModal, contentModal) {
        // let myHeadModal = this.headModalProp
        // let myContentModal = this.contentModalProp

        // let myHeadModal = headModal
        // let myContentModal = contentModal

        this.headModalProp =  headModal;
        this.contentModalProp = contentModal;
        

        getAPI.get("Recursos/api/Articulos/Estado/", {
          params:{
            "Estado": headModal
          }
          }
        ).then(response => {
            // console.log('AAA prro')
            console.log(response.data)
            this.recursos = response.data
        })
      },
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      // obtieneEstado: function() {
      //   // const self = this
      //   getAPI.get("api/Estados/").then(response => {
      //     console.log('AAA prro')
      //     console.log(response.data)
      //     this.estados = response.data
      //   })
      // }

      
      

      

      
    },
  }
</script>