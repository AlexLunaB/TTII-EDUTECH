<template>
  <v-container>
    <v-toolbar
      dark
      color="primary"
    >

      <v-toolbar-title>Edita tus datos</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn
          dark
          text
          @click="dialog = false"
        >
          Solicitar publicación
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-card>


      <v-form>

        <v-row>

          <v-col cols="12">


          </v-col>


        </v-row>


        <v-row>

          <v-col cols="12" md="12">


          </v-col>

        </v-row>


        <v-row>
          <v-col cols="12" md="6" sm="12">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Nombre</v-list-item-title>
                <v-text-field

                  v-model="user.first_name"


                  color="purple darken-2"

                  required
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>


          </v-col>


          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Apellidos</v-list-item-title>


                <v-text-field
                  v-model="user.last_name"


                ></v-text-field>

                <div id="preview">
                  <img v-if="url" :src="url"/>
                </div>
              </v-list-item-content>
            </v-list-item>

          </v-col>


        </v-row>

        <v-row>
          <v-col cols="12" md="6" sm="12">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Correo</v-list-item-title>
                <v-text-field

                  v-model="user.email"
                  prepend-icon="far fa-envelope"

                  color="purple darken-2"

                  required
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>


          </v-col>


          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Foto de Perfil</v-list-item-title>


                <v-file-input @change="onFileChange"
                              label=""
                              v-model="Img"
                              filled
                              prepend-icon="mdi-camera"
                ></v-file-input>

                <div id="preview">
                  <img v-if="user.profile.foto" :src="user.profile.foto"/>
                </div>
              </v-list-item-content>
            </v-list-item>

          </v-col>


        </v-row>
        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Semblanza</v-list-item-title>


                <v-textarea v-model="user.profile.semblanza"></v-textarea>
              </v-list-item-content>
            </v-list-item>


          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6" sm="12">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Estado</v-list-item-title>
                <v-autocomplete
                  v-model="user.profile.estado"
                  :items="estados"
                  item-text="nombre"
                  label="Estados"
                  @change="obtiene_municipios(); "
                  chips
                  item-value="id"
                ></v-autocomplete>
              </v-list-item-content>
            </v-list-item>


          </v-col>


          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Municipio</v-list-item-title>


                <v-autocomplete
                  v-model="user.profile.municipio"
                  :items="municipios"
                  item-text="nombre"
                  label="Municipios"
                  @change="obtiene_municipios(); "
                  chips
                  item-value="id"
                ></v-autocomplete>


              </v-list-item-content>
            </v-list-item>

          </v-col>


        </v-row>


        <v-card-actions>
          <v-btn

            text
            blue
            @click="submit"
          >
            Guardar Cambios
          </v-btn>
        </v-card-actions>

      </v-form>

    </v-card>
  </v-container>
</template>

<script>
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'


  import {quillEditor} from 'vue-quill-editor'
  import {getAPI} from '../../Api/axios-base'
  import Swal from "sweetalert2";


  export default {
    name: 'AddPost',
    components: {
      quillEditor,
    },
    data() {
      return {

        estados: [],
        municipios: [],

        Img: null,

        user: {},

        url: "",
        formdata: {
          Nombre: "",
          Description: "",
          Img: null,
          File: null,

          content: "<h1>Coloca el texto</h1>"


        },
        content: '<h2>I am Example</h2>',
        editorData: '<p>Rich-text editor content.</p>',
        editorConfig: {
          // The configuration of the rich-text editor.
        },
        editorOption: {
          // Some Quill options...
        }

      };
    }, methods: {

      obtiene_estado: function () {
        const self = this
        getAPI.get("api/Estados").then((response) => {
          self.estados = response.data

        });
      },
      obtiene_municipios: function () {
        const self = this
        getAPI.get("api/Estados/" + self.user.profile.estado + "/GetMunicipio").then((res) => {
          self.municipios = res.data

        });
      },

      obtiene_datos_usuario: function () {
        const self = this;
        getAPI.get("Usuarios/View/profile/").then((response) => {
          console.log(response.data)

          self.user = response.data
          this.obtiene_municipios()
        });

      },

      retorna(){
        Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Tu Información ha sido actualizada',
            showConfirmButton: false,
            timer: 2500
          }).then((e)=>{
             this.$router.push({name: 'Perfil'})
          })

      },


      onEditorBlur(quill) {
        console.log('editor blur!', quill)
      },
      onEditorFocus(quill) {
        console.log('editor focus!', quill)
      },
      onEditorReady(quill) {
        console.log('editor ready!', quill)
      },
      onEditorChange({quill, html, text}) {
        console.log('editor change!', quill, html, text)
        this.content = html
      }, onFileChange() {
        this.user.profile.foto = URL.createObjectURL(this.Img)
      },

      submit() {

        var self = this


        /*for( let file in this.formdata.Img){
                formData.append("cave", file)
            }*/
        let formData = new FormData()
        if (this.Img != null) {

          formData.append("foto", self.Img);

          getAPI.patch("/Usuarios/View/foto/", formData)
            .then((d) => {
              getAPI.patch("/Usuarios/View/profile/",
                {usuario: self.user}).then((d) => {
                self.retorna()
              })
            })
        }

        else {

          getAPI.patch("/Usuarios/View/profile/",
            {usuario: self.user,}).then((d) => {
              self.retorna()

          })
        }


      }
    },
    computed: {
      editor() {
        return this.$refs.myQuillEditor.quill
      }
    },
    mounted() {
      this.obtiene_datos_usuario()
      this.obtiene_estado()

    }

  }
</script>


<style scoped>
  #preview {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #preview img {
    max-width: 100%;
    max-height: 200px;
  }

</style>
