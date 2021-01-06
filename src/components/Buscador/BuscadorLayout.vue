<template>
<v-container fluid>
    <v-card class="mx-auto" >
        <v-card-text>
        
        <v-row>
            <v-col cols="12" md="3">
                    <v-card
      color="red lighten-2"
      dark
    >
      <v-card-title class="headline red lighten-3">
        Filtros
      </v-card-title>
      <v-card-text>

                                                    <v-select
                                                            
                                                            item-text="nombre" item-value="pk"
                                                            label="Estado"
                                                            v-model="busqueda.estado"
                                                            multiple
                                                            @change="filtrado"


                                                    ></v-select>
      </v-card-text>
                    </v-card>
            </v-col>
            <v-col cols="12" md="9"></v-col>
        </v-row>
        </v-card-text>

       
    </v-card>
    
 
</v-container>
</template>

<script>


export default {
    name: "BuscadorLayout",
    data() {
        return {
            visible: false,
            Post: [],
            busqueda:{
                estado:null
            }
        }
    },
    components: {
   
    },
    methods: {
       
    },
    mounted(){
     
    }
};
</script>

<style scoped>

</style>