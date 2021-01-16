<template>
<v-container fluid>
    
    <v-card >
        
        <v-row>
            <v-col cols="8" style="background-color: #F3F3F3" >

                <v-container style="background-color: #FFFFFF" >
                    
                    <h1 class="text-center display-2 black--text text--accent-2">{{this.Post.temaDiscusion}}</h1>

                    <h4>Creado el {{this.Post.created}} por {{this.Post.administrador.username}}</h4>

                    <v-img
                    
                    max-height="400"
                    max-width="800"
                    :src="this.Post.Imagen"
                    class="ml-auto mr-auto mt-10 mb-10"
                    ></v-img>

                    <div>{{this.Post.descripcion}}</div>

                    <div v-html="this.Post.html"></div>

                    
                </v-container>
            </v-col >

            <v-col style="background-color: #FFF3E6" >
                
                    <CommentsAppBlog :perfil = perfil :id = id :Post = Post> </CommentsAppBlog>
                    
                
                <br>
                
                    <CardRecomendaciones v-for="post in Posts" :key="post.id" :post = post></CardRecomendaciones>
                    
                
            </v-col>
        </v-row>
        
    </v-card>
</v-container>
</template>

<script>
import { getAPI } from '../../Api/axios-base';
import CardRecomendaciones from '../CardRecomendaciones'
import CommentsAppBlog from '../comments/CommentsAppBlog'



export default {
    name: "BlogDetail",
    data() {
        return {
            id:this.$route.params.id,
            Post:{},
            Posts:{},

            perfil: {
                email: null,
                nombre: null,
                apellidos: null,
                usuario: null,
                foto: null,
                municipio: null,
                intereses: [],
            },
        }
    },

    
    components: {

        CardRecomendaciones,
        CommentsAppBlog
       
    },
    methods: {
        
        GetArticulo: async function () {

            try {
                self= this
                const res = await getAPI.get("/Foro/api/Post/"+this.id)
                self.Post = res.data
                // const res = await getAPI.get("/Foro/api/Post/"+this.id).then((res)=> {
                //     self.Post = res.data
                // });
                console.log('Articulo: ',res.data)
            } catch (error) {
                console.log(error)
            }
        },

        GetArticulos: async function () {

            try {
                self= this
                const res = await getAPI.get("/Foro/api/Post")
                self.Posts = res.data
                // const res = await getAPI.get("/Foro/api/Post/"+this.id).then((res)=> {
                //     self.Post = res.data
                // });
                console.log('Articulos', res.data)
            } catch (error) {
                console.log(error)
            }
        },

        obtiene_datos_usuario: function () {
            const self = this;
            getAPI.get("Usuarios/View/profile/").then((response) => {

            self.perfil.email = response.data.email;
            self.perfil.nombre = response.data.first_name;
            self.perfil.apellidos = response.data.last_name;
            self.perfil.usuario = response.data.username;
            self.perfil.foto = response.data.profile.foto;
            self.perfil.semblanza = response.data.profile.semblanza;
            self.perfil.intereses = response.data.profile.intereses;

            // console.log(response.data)
            });

            

        },
 
    }, 

    mounted(){ 
        this.GetArticulo()
        this.GetArticulos()
        this.obtiene_datos_usuario()
      
    }
};
</script>

<style scoped>

</style>