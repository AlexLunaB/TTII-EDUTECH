<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="6" sm="12">

        <v-card>

          <v-row class="pa-3">
            <v-col offset="1" cols="10" align="center">
              <v-avatar size="200">
                <v-img v-if="perfil.foto !== null" class="card-img" :src="perfil.foto"></v-img>
                <v-img v-else class="card-img" src="../../static/images/default_avatar.jpg"></v-img>

              </v-avatar>

              <!------------------ EDIT IMAGE BUTTON ------------------>

              <input type="file" id="imageInput" hidden>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn class="mx-2" fab small color="#32BCC3" absolute right bottom v-on="on" dark router :to="{ name: 'PerfilEdit'}">
                    <v-icon dark> fas fa-pencil-alt</v-icon>
                  </v-btn>
                </template>
                <span>Editar Perfil</span>
              </v-tooltip>

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
                      <span>@{{perfil.usuario}}</span>
                    </div>

                    <div class="text-center mb-2 title ">
                      <span>{{perfil.semblanza}}</span>
                    </div>
                    <div class="text-center mb-3 pr-5 pl-5 font-weight-regular">

                    </div>
                    <div class="text-center mb-3">
                      <v-icon>fas fa-signature</v-icon>
                      <span>
                      {{perfil.nombre}}
                      {{perfil.apellidos}}

                                </span>
                    </div>
                    <div class="text-center mb-3">
                      <v-icon>fas fa-envelope</v-icon>
                      <span>
                      {{perfil.email}}
                                </span>
                    </div>
                    <div class="text-center mb-3">
                      <v-icon>fas fa-phone-alt</v-icon>
                      <span>
                      {{perfil.telefono}}
                                </span>
                    </div>
                    <div class="text-center">
                      <v-chip
                        class="ma-2"
                        color="pink"
                        label
                        text-color="white"
                        v-for="tag in perfil.intereses "
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

      </v-col>

      <v-col cols="12" md="6" sm="12" v-if="permisoUsuario === 'ED'">
        <v-row>

          <v-col cols="12" md="12" sm="12">
            <v-card :loading="loadingRecursos">

              <v-card-title>Mis Recursos</v-card-title>
              
              <!-- Table recursos -->
              <v-data-table
                :headers="headersRecursos"
                :items="recursosUsuario"
                item-key="id"
                class="elevation-1"
                :search="searchRecursos"
                :custom-filter="filterOnlyCapsTextRecursos"
              >
                <template v-slot:top>
                  <v-text-field
                    v-model="searchRecursos"
                    label="Buscar (ingresa minusculas)"
                    class="mx-4"
                  ></v-text-field>
                </template>

                <template v-slot:item.id="{item}">
                  <v-btn color="primary" router @click="abrirRecurso(item.id)" >Abrir</v-btn>
                </template>

                <template v-slot:body.append>
                  <tr>
                    <td></td>
                    <td>
                      <!-- <v-text-field
                        v-model="calories"
                        type="number"
                        label="Less than"
                      ></v-text-field> -->
                    </td>
                    <td colspan="4"></td>
                  </tr>
                </template>
              </v-data-table>

              <v-card-actions>
                <v-btn color="primary" router :to="{ name: 'AddRecurso'}">Agregar un recurso</v-btn>
              </v-card-actions>
            </v-card>


          </v-col>


          <v-col cols="12" md="12" sm="12">
            <v-card :loading="loadingArticulos">

              <v-card-title>Mis Blogs</v-card-title>
              
              <!-- Table blogs -->
              <v-data-table
                :headers="headersBlogs"
                :items="blogsUsuario"
                item-key="id"
                class="elevation-1"
                :search="searchBlogs"
                :custom-filter="filterOnlyCapsTextBlogs"
              >
                <template v-slot:top>
                  <v-text-field
                    v-model="searchBlogs"
                    label="Buscar (ingresa minusculas)"
                    class="mx-4"
                  ></v-text-field>
                </template>

                <template v-slot:item.id="{item}">
                  <v-btn color="primary" router @click="abrirArticulo(item.id)" >Abrir</v-btn>
                </template>

                <template v-slot:body.append>
                  <tr>
                    <td></td>
                    <td>
                      <!-- <v-text-field
                        v-model="calories"
                        type="number"
                        label="Less than"
                      ></v-text-field> -->
                    </td>
                    <td colspan="4"></td>
                  </tr>
                </template>
              </v-data-table>

              <v-card-actions>
                <v-btn color="primary" router :to="{ name: 'AddPub'}">Agregar un blog</v-btn>
              </v-card-actions>
            </v-card>

          </v-col>


        </v-row>
      </v-col>

      <v-col cols="12" md="6" sm="12" v-else>
        <v-row>
          <v-card>
            <v-card-title> No se pueden mostrar tus recursos.</v-card-title>
            <h3>
              No cuentas con permisos para añadir material. 
              Para mostrar este apartado, comunicate con un administrador para solicitar permisos.
            </h3>
            <v-img
              src="../../../static/images/alto.png"
              height="250px"
              width="300px"
              style="margin-left: auto; margin-right: auto"
            ></v-img>
          </v-card>
        </v-row>
        
      </v-col>


    </v-row>


  </v-container>
</template>

<script>
  import {getAPI} from "../../Api/axios-base";
  import store from '../../store'
  import {mapMutations} from "vuex";

  export default {
    data() {
      return {
        tags: [],
        perfil: {
          email: null,
          nombre: null,
          apellidos: null,
          usuario: null,
          foto: null,
          municipio: null,
          intereses: [],
          telefono: null
        },
        nombre: "Luis Pavel",
        apellidoP: "Varela",
        apellidoM: "Aguilar",
        tipoUsuario: "Tipo de usuario",
        emailUsuario: "luispavelvarela@gmail.com",
        values: [],
        value: null,
        categorias: [],



        //Data del data table
        searchRecursos: '',
        searchBlogs: '',
        calories: '',
        recursosUsuario: [],
        blogsUsuario: [],
        
        permisoUsuario: store.getters.getterPermiso[0].permiso,

        loadingRecursos: false,
        loadingArticulos: false,
      };
    },

    computed: {
      //computed del data table

      headersRecursos () {
        return [
          
          {
            text: 'Nombre',
            value: 'nombreRecurso',
            sortable: true,
            width: "20%"
            // filter: value => {
            //   if (!this.calories) return true

            //   return value < parseInt(this.calories)
            // },
          },
          // {
          //   text: 'Tags',
          //   value: 'tags',
          //   sortable: false,
          //   width: "20px"
          // },
          {
            text: 'Descripción',
            value: 'descripcion',
            sortable: false,
            width: "40%"
          
          },
          {
            text: 'Creado',
            value: 'fechaCreacion',
            sortable: false,
            width: "20%"
          
          },
          {
            text: 'Ver',

            value: 'id',
            sortable: false,
            width: "20%"
          
          },
          // 
        ]
      },

      headersBlogs () {
        return [
          
          {
            text: 'Nombre',
            value: 'temaDiscusion',
            sortable: true,
            // filter: value => {
            //   if (!this.calories) return true

            //   return value < parseInt(this.calories)
            // },
          },
          // {
          //   text: 'Tags',
          //   value: 'tags',
          //   sortable: false,
          
          // },
          {
            text: 'Descripción',
            value: 'descripcion',
            sortable: false,
          
          },
          {
            text: 'Creado',
            value: 'created',
            sortable: false,
          
          },
          {
            text: 'Ver',

            value: 'id',
            sortable: false,
            width: "20%"
          
          },
          // 
        ]
      },
      
    },

    watch: {
      
      
    },

    methods: {
      ...mapMutations(['SetLoading']),

      obtiene_clasificacion: function () {
        const self = this;
        //categorias de los tipos de recursos
        getAPI.get("Recursos/api/categorias/").then((response) => {
          // if API sends back new access and refresh token update the store
          console.log("New access successfully generated");
          console.log(response.data);

          self.categorias = response.data;
        });
      },
      obtiene_datos_usuario: function () {
        const self = this;
        self.SetLoading(true)
        getAPI.get("Usuarios/View/profile/").then((response) => {

          self.perfil.email = response.data.email;
          self.perfil.nombre = response.data.first_name;
          self.perfil.apellidos = response.data.last_name;
          self.perfil.usuario = response.data.username;
          self.perfil.foto = response.data.profile.foto;
          self.perfil.semblanza = response.data.profile.semblanza;
          self.perfil.intereses = response.data.profile.intereses;
          self.perfil.telefono = response.data.profile.telefono;

          self.SetLoading(false)

        });

      },

      get_tags: function () {
        self = this
        getAPI.get("Usuarios/View/Tags/").then((response) => {

          console.log('Tags', response.data)
          self.tags = response.data;

        });
      },

      getRecursosUsuario: async function() {
        try {
          self = this;
          const res = await getAPI.get("/Recursos/api/Articulos/PorUsuario/")
          self.recursosUsuario = res.data
          // const res = await getAPI.get("/Foro/api/Post/"+this.id).then((res)=> {
          //     self.Post = res.data
          // });
          console.log('RecursosUsuario', res.data)
          console.log('Permiso', this.permisoUsuario)
        } catch (error) {
          console.log(error)
        }
      },

      getBlogsUsuario: async function() {
        try {
          self = this;
          const res = await getAPI.get("/Foro/api/Post/PorUsuario/")
          self.blogsUsuario = res.data
          // const res = await getAPI.get("/Foro/api/Post/"+this.id).then((res)=> {
          //     self.Post = res.data
          // });
          console.log('BlogUsuario', res.data)
        } catch (error) {
          console.log(error)
        }
      },

      filterOnlyCapsTextRecursos (value, search, item) {
        return value != null &&
          search != null &&
          typeof value === 'string' &&
          value.toString().toLocaleLowerCase().indexOf(search) !== -1
      },

      filterOnlyCapsTextBlogs (value, search, item) {
        return value != null &&
          search != null &&
          typeof value === 'string' &&
          value.toString().toLocaleLowerCase().indexOf(search) !== -1
      },

      
      abrirRecurso (recurso) {
          this.loadingRecursos = true
          setTimeout( () => {
              this.loadingRecursos = false

              // this.loading = false
              this.$router.push({name: 'RecursoDetail', params: { id: recurso}})
          }, 2000)
      },

      abrirArticulo (articulo) {
          this.loadingArticulos = true
          setTimeout( () => {

              this.loadingArticulos = false
              this.$router.push({name: 'post', params: { id: articulo}})
          }, 2000)
      },
      
    },

    mounted() {
      // this.obtiene_clasificacion();
      this.obtiene_datos_usuario();
      this.get_tags(),
      this.getRecursosUsuario(),
      this.getBlogsUsuario()
    },
  };
</script>

<style scoped>
  .background {
    background-color: #367cff;
  }
</style>
