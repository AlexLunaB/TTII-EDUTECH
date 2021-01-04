<!--
<template v-for="(value) in recursos">
-->
<template>
    <!-- <v-card-title>Nombre del recurso: {{value.nombreRecurso}}</v-card-title>4 -->
    <div>
        <v-card max-width=45% >


            <!-- <div>{{recurso.id}}</div>
            <div>{{recurso.nombreRecurso}}</div> -->

            <!-- <v-img
            height="250"
            src="https://www.quo.es/wp-content/uploads/2019/10/los-cinco-trabajos-que-por-ahora-no-podra-quitarte-un-robot.jpg"
            ></v-img> -->
            <Carousel> </Carousel>

            <v-card-title>Nombre del recurso: {{recurso.nombreRecurso}}</v-card-title>

            <v-card-text>
                <v-row
                    align="center"
                    class="mx-0"
                >
                    <v-rating
                    v-model="recurso.calificacion"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    @input="postCalificacion"
                    
                    hover
                    large

                    ></v-rating>

                    <div class="grey--text ml-4" >
                    {{recurso.calificacion}} (413)
                    </div>
                </v-row>

                <div class="my-4 subtitle-1">
                    $ • Italian, Cafe
                </div>

                <v-list-item-title class="headline mb-1">
                    ID: {{recurso.id}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Usuario: {{recurso.Usuario}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Descripcion: {{recurso.descripcion}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Fecha de creacion: {{recurso.fechaCreacion}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Fecha de modificación: {{recurso.fechaModificacion}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Estado de procedencia: {{recurso.estado}}
                </v-list-item-title>
                <v-list-item-title class="headline mb-1">
                    Municipio de procedencia: {{recurso.municipio}}
                </v-list-item-title>

                <!-- <div>ID: {{value.id}}</div>
                <div>Usuario: {{value.Usuario}}</div>
                <div>Descripcion: {{value.descripcion}}</div>
                <div>Fecha de creacion: {{value.fechaCreacion}}</div>
                <div>Fecha de modificación: {{value.fechaModificacion}}</div>
                <div>Estado de procedencia: {{value.estado}}</div>
                <div>Municipio de procedencia: {{value.municipio}}</div> -->

            </v-card-text>

            <!-- <div> 
            <v-divider class="mx-4"></v-divider>

            </div> -->

            <hr class="dashed">
            
            <br><br>
            
            

            <!-- <v-card-title>Tonight's availability</v-card-title>

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
            </v-card-actions> -->
        </v-card>
            
    </div>
</template>

<script>
import { getAPI } from "../Api/axios-base";
import Carousel from './Carousel'
export default {
    data() {
        return {
            recursos: [],
            rating: 2.5
        }
    },
    components: {
        Carousel
    },
    props: {
        idEstado: String,
        recurso:{},
    },
    methods: {
        postCalificacion: async function() {
            // try {
            //     await getAPI.post("Recursos/api/Articulos/",
            //     {"calificacionRecurso":this.rating}).then((res)=> {
            //         alert(JSON.stringify(res))
            //     });
            // } catch (error) {
            //     alert(error);
            // }
            // console.log(this.recurso.id)
            getAPI.post("Recursos/api/Articulos/"+this.recurso.id+"/CalificaRecurso/",{
                "calificacion": this.recurso.calificacion
            }).then((d)=>{
          console.log(d)
        })

            console.log(`ID: ${this.recurso.id} - Nombre: ${this.recurso.nombreRecurso} - Rating: ${this.rating}`)
        },
    }
   

}
</script>