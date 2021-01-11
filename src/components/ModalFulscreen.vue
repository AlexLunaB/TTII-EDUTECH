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
              X
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

        <v-row>
          <v-col>
            Lo mas visitado de este estado......
          </v-col>
          <v-col v-if="dialog && recursos.length > 0">

            <v-list style="max-height: 700px" class="overflow-y-auto">
              <TarjetaRecurso v-for="recurso in recursos" :key="recurso.id" :recurso = recurso> </TarjetaRecurso>
            </v-list>

          </v-col>
          <v-col v-if="dialog && recursos.length === 0">
            No hay recursos en este estado :c
          </v-col>
          <v-col>
            Tal vez te interese......

            <!-- <CardRecomendaciones> </CardRecomendaciones> -->

          </v-col>
        </v-row>

      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>

import {getAPI} from '../Api/axios-base'
import Carousel from '../components/Carousel'
import TarjetaRecurso from './TarjetaRecurso'
import CardRecomendaciones from './CardRecomendaciones'
import CommentsApp from './comments/CommentsApp'


export default {


  mounted(){

  },


  watch:{
    headModalProp: function(){
      this.getRecursos()
    }
  },
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
    Carousel,
    TarjetaRecurso,
    CardRecomendaciones,
    CommentsApp
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

      // return headModal;



    },
    reserve () {
      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
    },


     getRecursos: function() {
            getAPI.get("Recursos/api/Articulos/Estado/", {
                params:{
                "Estado": this.headModalProp
                }
            }
            ).then(response => {
                // console.log('AAA prro')
                console.log(response.data)
                this.recursos = response.data
            })
        },





  },
}
</script>



<style>
  /* Dashed border */
  hr.dashed {
    border-top: 3px dashed #bbb;
  }
</style>
