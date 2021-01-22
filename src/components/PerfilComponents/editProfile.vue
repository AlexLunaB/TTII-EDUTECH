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


      <v-form ref="form">

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
                  :rules="nameRules"


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
                  :rules="nameRules"
                  color="purple darken-2"

                  required


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
                  :rules="emailRules"

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
                              show-size
                              counter
                              prepend-icon="fas fa-camera"
                              placeholder="Elige una imagen para tu perfil"
                              :rules="imgRules"
                              counter-size-string="$vuetify.fileInput.counterSize"
                              accept="image/png, image/jpeg, image/bmp"
                              
                ></v-file-input>

                <!-- <v-btn
                  depressed
                  color="primary"
                  @click="eliminaFoto"
                >
                  Eliminar foto
                </v-btn> -->

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


                <v-textarea 
                v-model="user.profile.semblanza"
                :rules="semblanzaRules"
                placeholder="Escribe una breve descripción sobre ti (250 caracteres máximo">
                </v-textarea>
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

        <v-row>
          <v-col cols="12" md="6" sm="12">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Telefono de contacto</v-list-item-title>
                <v-text-field

                  v-model="user.profile.telefono"


                  color="purple darken-2"
                  type="number"
                  :rules="telRules"
                  placeholder="Número telefonico de 10 dígitos"
                  

                  required
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>
          </v-col>

        </v-row>


        <v-card-actions>
          <v-btn
            text
            color="blue darken-1"
            @click="submit"
          >
            Guardar Cambios
          </v-btn>


          <v-btn
            text
            color="blue darken-1"
            @click="imagen"
          >
            Datos imagen
          </v-btn>
          

          <v-btn
            text
            color="blue darken-1"
            @click="regresarPerfil"
          >
            CANCELAR
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
  import {mapMutations} from "vuex";

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
        },

        nameRules: [
          v => !!v || 'Se requiere un nombre',
          v => (v && v.length <= 20) || 'Máximo 20 caracteres',
          v => (/^(([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\'])|([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\']+[\s]))+([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\'])+[\s]?([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\'])?$/.test(v)) || 'Debe tener solo caracteres del alfabeto'
        ],

        emailRules: [
          v => !!v || 'Correo necesario',
          v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'El correo debe ser valido',
        ],

        imgRules: [
          file => !file || file.size <= 2e6 || 'Tu imagen debe pesar a lo mas 2 MB!',
          file => !file || file.type === "image/png" || file.type === "image/jpeg" || file.type === "image/bmp" || 'Debes subir un archivo de tipo imagen'
          // files => !files || console.log(files)
        ],

        semblanzaRules: [
          v => v && v.length <= 250  || 'Maximo 250 caracteres'
        ],

        telRules: [
          tel => tel.length === 0 || tel.length === 10 || 'Recuerda que ahora todos los números telefonicos son de 10 dígitos',
          
        ]

      };
    }, methods: {

      ...mapMutations(['SetLoading']),

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

      regresarPerfil: function() {
        Swal.fire({
            position: 'top-end',
            icon: 'info',
            title: 'No se guardaron los cambios',
            showConfirmButton: false,
            timer: 2500
          }).then((e)=>{
             this.$router.push({name: 'Perfil'})
          })
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
             location.reload()
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
        if(this.$refs.form.validate()) {

          /*for( let file in this.formdata.Img){
                  formData.append("cave", file)
              }*/
          let formData = new FormData()
          if (this.Img != null) {

            formData.append("foto", self.Img);

            self.SetLoading(true)

            getAPI.patch("/Usuarios/View/foto/", formData)
              .then((d) => {
                getAPI.patch("/Usuarios/View/profile/",
                  {usuario: self.user}).then((d) => {
                    self.SetLoading(false)
                  self.retorna()
                })
              })
          }

          else {
            
            self.SetLoading(true)
            getAPI.patch("/Usuarios/View/profile/",
              {usuario: self.user}).then((d) => {
                self.SetLoading(false)
                self.retorna()
            })
              
          }
        }


        


      },

      imagen() {
        console.log(this.Img)
        console.log(this.user.profile.telefono)
        console.log(this.user.profile.foto)
      },

      // eliminaFoto() {
      //   this.user.profile.foto = null
      //   this.Img = null
      // }
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
