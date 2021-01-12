<!--
<template v-for="(value) in recursos">
-->
<template>
    <!-- <v-card-title>Nombre del recurso: {{value.nombreRecurso}}</v-card-title>4 -->
    <div>
        <v-card max-width=550 :loading="loading" class="mx-100% mt-0 mb-0 ml-auto mr-auto"  >
            <template slot="progress">
                <v-progress-linear
                color="deep-purple"
                height="10"
                indeterminate
                ></v-progress-linear>
            </template>


            <!-- <div>{{recurso.id}}</div>
            <div>{{recurso.nombreRecurso}}</div> -->

            <!-- <v-img
            height="250"
            src="https://www.quo.es/wp-content/uploads/2019/10/los-cinco-trabajos-que-por-ahora-no-podra-quitarte-un-robot.jpg"
            ></v-img> -->
            <Carousel :imagenes="recurso.recurso_img" > </Carousel>

            <v-card-title class="justify-center">Nombre del recurso: {{recurso.nombreRecurso}}</v-card-title>

            <v-card-text>
                <v-row
                    align="center"
                    class="mx-0"
                >
                    <v-col>
                        <v-rating
                        v-model="recurso.calificacion"
                        color="yellow darken-3"
                        background-color="grey darken-1"
                        @input="postCalificacion"
                        hover
                        small
                        large

                        ></v-rating>

                        <div class="grey--text ml-4" >
                            {{recurso.calificacion}} (413)

                        </div>
                    </v-col>

                    <v-col>
                        <template>
                            <div class="text-center">
                                <v-btn
                                    rounded
                                    color="primary"
                                    dark
                                    router @click="reserve"
                                >
                                Ver mas
                                </v-btn>
                            </div>
                        </template>
                    </v-col>

                </v-row>

                <div class="my-4 subtitle-1">
                    Tags: {{recurso.tags.join(', ')}}
                </div>

                <v-simple-table>
                    <template v-slot:default>
                    <thead>
                        <tr>
                        <th class="text-left">
                            Datos del recurso
                        </th>
                        <th class="text-left">

                        </th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- <tr>
                            <td>ID:</td>
                            <td>{{recurso.id}}</td>
                        </tr> -->
                        <tr>
                            <td>Subido por:</td>
                            <td>{{recurso.Usuario.username}}</td>
                        </tr>
                        <tr>
                            <td>Descripcion:</td>
                            <td>{{recurso.descripcion}}</td>
                        </tr>
                        <tr>
                            <td>Fecha de creacion:</td>
                            <td>{{recurso.fechaCreacion}}</td>
                        </tr>
                        <!-- <tr>
                            <td>Fecha de modificación:</td>
                            <td>{{recurso.fechaModificacion}}</td>
                        </tr> -->
                        <tr>
                            <td>Estado de procedencia:</td>
                            <td>{{recurso.estado}}</td>
                        </tr>
                        <tr>
                            <td>Municipio de procedencia:</td>
                            <td>{{recurso.municipio}}</td>
                        </tr>
                    </tbody>
                    </template>
                </v-simple-table>



                <!-- <v-list-item-title >

                </v-list-item-title> -->
                <v-list-item-title >

                </v-list-item-title>
                <v-list-item-title >

                </v-list-item-title>
                <v-list-item-title >

                </v-list-item-title>
                <v-list-item-title >

                </v-list-item-title>
                <v-list-item-title >

                </v-list-item-title>
                <v-list-item-title >

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

        <br>

    </div>
</template>

<script>
import { getAPI } from "../Api/axios-base";
import Carousel from './Carousel'
import CommentsApp from './comments/CommentsApp'
export default {
    data() {
        return {
            recursos: [],
            rating: 2.5,
            loading: false
        }
    },
    components: {
        Carousel,
        CommentsApp
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

        reserve () {
            this.loading = true

            setTimeout( () => {

                this.loading = false
                this.$router.push({name: 'RecursoDetail', params: { id: this.recurso.id}})
            }, 2000)
        },
    }


}
</script>
