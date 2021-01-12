<template>
<v-container fluid>
    
    <v-btn
        block
        elevation="2"
        color = "primary"
        @click="handleStateClick"
    >
        ¿Agregar recurso? Click aqui
    </v-btn>

    <v-row>
        <v-col cols="12">
                    <v-card
      class="mt-2"

    >
      <v-img
        class="white--text align-end"
        height="200px"
        src="https://images.freeimages.com/images/large-previews/595/law-education-series-3-1467430.jpg"
      >
        <v-card-title>Quieres Publicar un articulo</v-card-title>
      </v-img>
  

  

  
      <v-card-actions>
        <v-btn
          color="orange"
          dark
          router :to="{ name: 'AddPub'}"
        >
          Compartir
        </v-btn>
  

      </v-card-actions>
    </v-card>
        </v-col>


    </v-row>


    <v-row>
        
                <SingleComponent v-for="arti in Post" :articulo="arti"></SingleComponent>
                
      
    </v-row>

    <!-- <div v-if="visible">

        <RecursoArticulo></RecursoArticulo>
        
    </div> -->

    <RecursoArticulo ref="addResource"></RecursoArticulo>
    
</v-container>
</template>

<script>
import NavBar from './NavBar';
import HeaderBlog from './BlogComponents/HeaderBlog';
import SingleComponent from './BlogComponents/SingleComponent';
import RecursoArticulo from './Recursos/RecursoArticulo';
import { getAPI } from '../Api/axios-base';

export default {
    name: "Blog",
    data() {
        return {
            visible: false,
            Post: [],
        }
    },
    components: {
        NavBar,
        HeaderBlog,
        SingleComponent,
        RecursoArticulo
    },
    methods: {
        handleStateClick: function () {

            this.$refs.addResource.showAddResource();
        }, 
        

        GetArticulos: function () {
          self= this
                getAPI.get("/Foro/api/Post").then((res)=> {
                  self.Post = res.data
                  console.log(res.data)
      });

            
        }, 
    },
    mounted(){
      this.GetArticulos()
    }
};
</script>

<style scoped>

</style>