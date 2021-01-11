<template>
<v-container fluid>
    
    <v-card>
        <v-container>

        <v-row>
            <v-col cols="12">

                <div v-html="this.Post.html"></div>
                
            </v-col>
        </v-row>
        </v-container>
    </v-card>
</v-container>
</template>

<script>
import { getAPI } from '../../Api/axios-base';



export default {
    name: "RecursoDetail",
    data() {
        return {
            id:this.$route.params.id,
            Post:{},
           
        }
    },

    
    components: {


       
    },
    methods: {
        
            GetArticulo: function () {
          self= this
                getAPI.get("Recursos/api/Articulos/"+this.id).then((res)=> {
                  self.Post = res.data
                  console.log(res.data)
      });
       
    },
    }, 

    mounted(){ 
        this.GetArticulo()
      
    }
};
</script>

<style scoped>

</style>