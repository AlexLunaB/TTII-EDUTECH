<template>
  <v-container fluid class="mb-0">


        <v-card :loading="loading" class="mx-100% mt-0 mb-0" >
          <template slot="progress">
            <v-progress-linear
              color="deep-purple"
              height="10"
              indeterminate
            ></v-progress-linear>
          </template>

          <v-img
            height="250"
            src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
          ></v-img>

          <v-card-title>{{tituloArticulo}} </v-card-title>

          <v-card-text>
            <v-row align="center" class="mx-0">
              <v-rating
                :value="4.0"
                color="amber"
                dense
                half-increments
                readonly
                size="15"
              ></v-rating>

              <div class="grey--text ml-4">{{valorCalificacion}} ({{totalCalificaciones}})</div>
            </v-row>

            <div class="my-4 subtitle-1"> {{subtituloArticulo}} </div>

            <div class="my-2">
              {{resumenArticulo}}
            </div>

            <span class="date"> Hace 5 minutos </span>
            <a href="#">Leer más</a>
          </v-card-text>

          <v-divider class="mx-4"></v-divider>

          <v-card-title>Comentar</v-card-title>



          <v-card-text>
            <v-text-field ></v-text-field>
          </v-card-text>

          <v-card-actions>
            <v-btn color="deep-purple lighten-2" text @click="reserve">
              Comentar
            </v-btn>
          </v-card-actions>
        </v-card>

  </v-container>
</template>

<script>
export default {
  data () {
    return {
      tituloArticulo: 'Titulo del artículo',
      // Valor ( en texto de la califcacion)
      valorCalificacion: '4.5',
      // Numero de calificaciones
      totalCalificaciones: '333',
      resumenArticulo: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s',
      subtituloArticulo: 'Subtitulo del articulo',
      loading: false,
      selection: 1,
    }
  },
  methods : {
    reserve () {
      this.loading = true

      setTimeout( () => (this.loading = false), 2000)
    },
  }
};
</script>

<style scoped>
</style>