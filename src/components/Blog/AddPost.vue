<template>
  <v-container>
    <v-toolbar
      dark
      color="primary"
    >

      <v-toolbar-title>Crea una publicación</v-toolbar-title>
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


            <v-card-title>Describe Mejor Tu articulo</v-card-title>


          </v-col>


        </v-row>


        <v-row>

          <v-col cols="12" md="12">

            <v-subheader>Detalle De la publicación</v-subheader>

          </v-col>

        </v-row>


        <v-row>
          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Nombre del artículo</v-list-item-title>


                <v-text-field

                  v-model="formdata.Nombre"


                  color="purple darken-2"
                  label="Es como va aparecer al momento de publicarlo"
                  required
                  :rules="nameRules"
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>


          </v-col>


          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Imagen preview del Post</v-list-item-title>


                <v-file-input @change="onFileChange"
                              label="Esta imagen aparecerá como una descripción gráfica"
                              v-model="formdata.Img"

                              filled
                              prepend-icon="mdi-camera"
                ></v-file-input>

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
                <v-list-item-title>¿Tienes Algún PDF o Word  que lo respalde?</v-list-item-title>


                <v-file-input
                              v-model="formdata.Archivo"
                              filled
                ></v-file-input>


              </v-list-item-content>
            </v-list-item>

          </v-col>


        </v-row>
        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Descripción del artículo</v-list-item-title>


                <v-textarea :rules="nameRules" v-model="formdata.Description"></v-textarea>
              </v-list-item-content>
            </v-list-item>


          </v-col>
        </v-row>

        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Institución de Procedencia</v-list-item-title>


                <v-autocomplete
                  v-model="formdata.instituto"
                  :items="institutos"
                  item-text="NombreInstitucion"
                  return-object
                  label="Institución o Empresa"
                  :rules="selectRules"
                ></v-autocomplete>

              </v-list-item-content>
            </v-list-item>


          </v-col>
        </v-row>

        <v-row>


          <v-col cols="12">
            <quill-editor
              ref="myQuillEditor"
              v-model="formdata.content"
              :options="editorOption"
              @blur="onEditorBlur($event)"
              @focus="onEditorFocus($event)"
              @ready="onEditorReady($event)"
            />


          </v-col>
        </v-row>
        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Tags</v-list-item-title>

                <v-autocomplete
                  v-model="formdata.tags"
                  :items="tags"
                  item-text="slug"
                  item-value="slug"
                  outlined
                  dense
                  chips
                  small-chips
                  label="Tags"
                  :search-input.sync="search"
                  multiple

                  v-on:keyup.enter="addNewTag"
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
            Solicitar publicación
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
        id:"",
        search: "",

        institutos:[],

        tags: [],

        url: "",
        formdata: {
          Nombre: "",
          Description: "",
          Img: null,
          File: null,
          Archivo:null,
          tags: [],
          instituto:[],
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
          v => !!v || 'Es Requerido',

        ],



      };
    }, methods: {
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
        this.url = URL.createObjectURL(this.formdata.Img)

      },
      get_tags: function () {
        self = this
        getAPI.get("/Foro/api/Post/Tags/").then((response) => {
          console.log(response.data)

          self.tags = response.data;

        });
      },

            get_institucion: function () {
        self = this
        getAPI.get("/api/Instituciones/").then((response) => {

          self.institutos = response.data;

        });
      },

      addNewTag() {
        if (this.search != null || (this.search.trim()) != '') {
          this.tags.push({slug: this.search});
          this.formdata.tags.push(this.search);
        }
      },


      submit() {

        var self = this
        let a = this.$refs.form.validate();
        if (!a)
          return

        var self = this

        let formData = new FormData()
        /*for( let file in this.formdata.Img){
                formData.append("cave", file)
            }*/
        formData.append("Imagen", this.formdata.Img);
        formData.append("Archivo", this.formdata.Archivo);
        formData.append("html", this.formdata.content);
        formData.append("temaDiscusion", this.formdata.Nombre);
        formData.append("descripcion", this.formdata.Description);
        formData.append("institucion", this.formdata.instituto.id);
        formData.append("tags", JSON.stringify(this.formdata.tags));

        let data = {temaDiscusion: self.formdata.Nombre}
        console.log(data)
        getAPI.post("/Foro/api/Post/", formData, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then((data) => {
          self.id=data.data.id
           Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Tu Articulo se ha publicado con éxito',
            showConfirmButton: false,
            timer: 1500
          }).then((e)=>{
             this.$router.push({name: 'post', params:{id: self.id} })
          })
        })

      }
    },
    computed: {
      editor() {
        return this.$refs.myQuillEditor.quill
      }
    },
    mounted() {
      this.get_tags()
      this.get_institucion()
      console.log('this is current quill instance object', this.editor)
    },
    watch: {
      "formdata.tags"() {
        this.search = ""
      }


    },

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
