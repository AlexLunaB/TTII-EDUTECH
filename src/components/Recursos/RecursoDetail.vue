<template>
<v-container fluid>
    <v-row>
      <v-col cols="12" md="3" sm="12">

        <v-card>

          <v-row class="pa-3">
            <v-col offset="1" cols="10" align="center">
              <v-avatar size="200">
                <v-img class="card-img" :src="Post.Usuario.profile.foto"></v-img>
              </v-avatar>

              <!------------------ EDIT IMAGE BUTTON ------------------>

              <input type="file" id="imageInput" hidden>
              

            </v-col>
            <v-col offset="1" cols="10">
              <v-row>
                <v-col>

                  <v-card
                    color="#385F73"
                    dark
                  >
                    <!------------------ PROFILE DATA ------------------>
                    <div class="text-center mb-3 title text-secundario font-weight-bold">
                      <span>Datos de contacto</span>
                    </div>

                    <div class="text-center mb-2 title ">
                      <span>Usuario: @{{Post.Usuario.username}}</span>
                    </div>
                    <div class="text-center mb-3 pr-5 pl-5 font-weight-regular">

                    </div>
                    <div class="text-center mb-3">
                      <v-icon>fas fa-signature</v-icon>
                      <span>
                      {{Post.Usuario.first_name}}
                      {{Post.Usuario.last_name}}

                                </span>
                    </div>
                    <div class="text-center mb-3">
                      <v-icon>fas fa-envelope</v-icon>
                      <span>
                      {{Post.Usuario.email}}
                                </span>
                    </div>
                    <div class="text-center mb-3">
                      <v-icon>phone-alt</v-icon>
                      <span>
                      {{Post.Usuario.profile.telefono}}
                                </span>
                    </div>
                    <div class="text-center">
                      <v-chip
                        class="ma-2"
                        color="pink"
                        label
                        text-color="white"
                        v-for="tag in Post.intereses "
                      >
                        <v-icon left>
                          fas fa-tag

                        </v-icon>
                        {{tag}}
                      </v-chip>
                    </div>
                    <!------------------ END PROFILE DATA ------------------>
                    <div class="mt-5">

                    </div>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

        </v-card>

      </v-col >
      
      <v-col cols="12" md="6" sm="12" >
          <h1 class="text-center display-2 black--text text--accent-2">{{this.Post.nombreRecurso}}</h1>
          <h4>Creado el {{this.Post.fechaCreacion}} por {{this.Post.Usuario.username}}</h4>
          <div>{{this.Post.descripcion}}</div>
          <div v-html="this.Post.html"></div>
      </v-col>

      <v-col>
          <CommentsApp></CommentsApp>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import { getAPI } from '../../Api/axios-base';
import CommentsApp from '../comments/CommentsApp'
import Swal from 'sweetalert2'



export default {
    name: "RecursoDetail",
    data() {
        return {
            id:this.$route.params.id,
            Post:{},
           
            // perfil: {
            //     email: null,
            //     nombre: null,
            //     apellidos: null,
            //     usuario: null,
            //     foto: null,
            //     municipio: null,
            //     intereses: [],
            // },
            
        }
    },

    
    components: {

        CommentsApp
       
    },
    methods: {
        
        GetArticulo: function () {
            self= this
            getAPI.get("Recursos/api/Articulos/"+this.id).then((res)=> {
                  self.Post = res.data
                  console.log(res.data)
            });
       
        },

        // obtiene_datos_usuario: function () {
        //     const self = this;
        //     getAPI.get("Usuarios/View/profile/").then((response) => {

        //     self.perfil.email = response.data.email;
        //     self.perfil.nombre = response.data.first_name;
        //     self.perfil.apellidos = response.data.last_name;
        //     self.perfil.usuario = response.data.username;
        //     self.perfil.foto = response.data.profile.foto;
        //     self.perfil.semblanza = response.data.profile.semblanza;
        //     self.perfil.intereses = response.data.profile.intereses;
        //     });

        // },

        
    }, 

    mounted(){ 
        this.GetArticulo()
        // this.obtiene_datos_usuario()
    }
};
</script>

<style scoped>

</style>