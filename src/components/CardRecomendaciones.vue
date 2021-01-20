<template>
  <v-card
    class="mx-auto"
    max-width="400"
    :loading="loading"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      :src="post.Imagen"
    >
      <v-card-title>{{post.temaDiscusion}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">
      {{post.descripcion}}
    </v-card-subtitle>

    <v-chip
        v-for="tag in post.tags"
        class="ma-2"
        color="green"
        text-color="white"
    >
        {{tag}}
    </v-chip>

    <v-card-text class="text--primary">
      <div>Escrito por: {{post.administrador.username}}</div>
      <div>Creado: {{post.created}}</div>
    </v-card-text>

    <v-card-actions>

      <v-btn
        color="orange"
        text
        @click="showBlogDetail"
      >
        Explorar
      </v-btn>

    </v-card-actions>
  </v-card>
</template>


<script>
  export default {
    data() {
      return {
        loading: false
      }
    },
    props: {
      post: {}
    },
    methods: {
      // showPost() {
      //   console.log(this.post)
      // }
      showBlogDetail() {
        this.loading = true
          setTimeout( () => {

              this.loading = false
              this.$router.push({name: 'post', params: { id: this.post.id}})
              location.reload()
          }, 2000)
          
      }
    },
    mounted() {
      // this.showPost()
    }
  }
</script>