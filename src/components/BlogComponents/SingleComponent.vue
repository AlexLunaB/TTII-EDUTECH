<template>

<v-col  cols="4" md="4" sm="12">
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
            :src="this.articulo.Imagen"
          ></v-img>

          <v-card-title>{{tituloArticulo}} </v-card-title>

          <v-card-text>


           

            <div class="my-2">
              {{resumenArticulo}}
            </div>

            <span class="date">Creado: {{this.articulo.created}} </span>
            <!-- <a href="#">Leer más</a> -->
          </v-card-text>

          <v-divider class="mx-4"></v-divider>





          <v-card-actions>
            <v-btn color="deep-purple" router @click="reserve">
              Leer más
            </v-btn>
          </v-card-actions>
        </v-card>

  </v-container>
</v-col>
</template>

<script>
export default {
  props: ['articulo'],

  data () {
    return {
      tituloArticulo: this.articulo.temaDiscusion,
      // Valor ( en texto de la califcacion)

      // Numero de calificaciones

      resumenArticulo: this.articulo.descripcion,

      loading: false,
      selection: 1,
    }
  },
  methods : {
    reserve () {
      this.loading = true

      setTimeout( () => {
        
      this.loading = false
      this.$router.push({name: 'post', params: { id: this.articulo.id}})
      }, 2000)
    },
  }
};
</script>

<style scoped>
</style>