<template>
  <v-container>
    <v-toolbar
      dark
      color="primary"
    >

      <v-toolbar-title>Agregar Nuevo Recurso</v-toolbar-title>
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


      <v-form lazy-validation ref="form">

        <v-row>

          <v-col cols="12">


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
                <v-list-item-title>Nombre del Recurso</v-list-item-title>


                <v-text-field
                  required
                  :rules="nameRules"
                  v-model="articulo.nombre"
                  label="Título del artículo*"
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>


          </v-col>


          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Descripcion del Recurso</v-list-item-title>


                <v-text-field
                  v-model="articulo.descripcion"
                  label="Descripción del artículo*"
                  :rules="descripcionRules"
                ></v-text-field>

                <!-- <div id="preview">
                  <img v-if="url" :src="url"/>
                </div> -->
              </v-list-item-content>
            </v-list-item>

          </v-col>


        </v-row>

        <v-row>
          <v-col cols="12" md="6" sm="12">


            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Archivos Imagen</v-list-item-title>


                <v-file-input
                  v-model="files"
                  small-chips
                  show-size
                  multiple
                  :rules="imgRules"
                  accept="image/png, image/jpeg, image/bmp"
                ></v-file-input>
              </v-list-item-content>
            </v-list-item>


          </v-col>

          <v-col cols="12" md="6" sm="12">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Autor(es)</v-list-item-title>


                <v-text-field
                  required
                  :rules="autorRules"
                  v-model="articulo.autores"
                  label="Ingresa los autores, separalos por coma"
                ></v-text-field>
              </v-list-item-content>
            </v-list-item>
          </v-col>


        </v-row>
        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Estado Origen</v-list-item-title>


                <v-autocomplete
                  v-model="articulo.estado"
                  :items="estados"
                  item-text="nombre"
                  return-object
                  label="Estados"
                  @change="obtiene_municipios()"
                  :rules="selectRules"
                ></v-autocomplete>
                {{estado.id}}
              </v-list-item-content>
            </v-list-item>


          </v-col>
        </v-row>

        <v-row>


          <v-col cols="12">

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Municipio Origen</v-list-item-title>


                <v-autocomplete
                  v-model="articulo.municipio"
                  :items="municipios"
                  item-text="nombre"
                  return-object
                  label="Municipios"
                  @change="obtiene_categorias()"
                  :rules="selectRules"
                ></v-autocomplete>
                {{municipio.id}}

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
                  v-model="articulo.instituto"
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
            <v-autocomplete
              v-model="articulo.categoria"
              :items="tags"
              item-text="slug"
              item-value="slug"
              outlined
              dense
              chips
              small-chips
              label="Preferencias"
              :search-input.sync="search"
              multiple
              :rules="nameRules"
              v-on:keyup.enter="addNewTag"
            ></v-autocomplete>
            {{categoria.id}}


          </v-col>
        </v-row>

        <v-row>


          <v-col cols="12">
            <quill-editor
              ref="myQuillEditor"
              v-model="articulo.html"
              :options="editorOption"

            />


          </v-col>
        </v-row>

        <v-card-actions>
          <v-btn
            text
            blue
            @click="postArticulos"
          >
            Solicitar publicación
          </v-btn>

          <v-btn
            text
            blue
            @click="imagen"
          >
            Datos imagen
          </v-btn>

        </v-card-actions>

      </v-form>

    </v-card>

  </v-container>
</template>

<script>
  import {getAPI} from "../../Api/axios-base";
  import Swal from 'sweetalert2'
  import {quillEditor} from 'vue-quill-editor'


  export default {
    components: {quillEditor},
    name: "AddRecurso",
    data: function () {
      return {
        nameRules: [
          v => !!v || 'Es Requerido',
          v => v && v.length <= 100 || 'No debe ser mayor a 100 caracteres'
        ],
        selectRules: [
          v => !!v || 'Es Requerido',

        ],

        descripcionRules: [
          v => !!v || 'Es Requerido',
          v => v && v.length <= 200 || 'No debe ser mayor a 200 caracteres'
        ],

        imgRules: [
          files => files && files.length > 0 || 'Debes adjuntar mínimo una imagen para vista previa',
          files => !files || !files.some(file => file.size > 2e6) || 'Procura que tus fotografias pesen a lo mas 2 MB!',
          files => !files || files.some(file => file.type === "image/png") || files.some(file => file.type === "image/jpeg") || files.some(file => file.type === "image/bmp") || 'Debes subir archivos de imagen',
          // file => !file || file.size <= 2e6 || 'Tu imagen debe pesar a lo mas 2 MB!',
          // file => !file || file.type === "image/png" || file.type === "image/jpeg" || file.type === "image/bmp" || 'Debes subir un archivo de tipo imagen'

        ],

        autorRules: [
          autor => !!autor || 'Es requerido',
          autor => autor && autor.length <= 100 || 'No debe ser mayor a 100 caracteres'
        ],

        editorConfig: {
          // The configuration of the rich-text editor.
        },
        editorOption: {
          // Some Quill options...
        },
        search: "",
        files: [],
        estados: [],
        municipios: [],
        dialog: false,
        institutos: [],
        articulo: {
          nombre: null,
          descripcion: null,
          estado: null,
          municipio: null,
          categoria: [],
          instituto: null,
          usuario: 1,
          html: "",
          autores: ''
        },
        estado: {
          id: null
        },
        categorias: [],
        categoria: {
          id: null
        },
        municipio: {
          id: null
        },
        tags: [],

      };
    },
    mounted: function () {
      this.obtiene_estado();
      this.get_tags();
      this.get_institucion();
    },

    methods: {
      obtiene_estado: function () {
        const self = this
        getAPI.get("api/Estados").then((response) => {
          self.estados = response.data
        });
      },
      obtiene_municipios: function () {
        const self = this
        getAPI.get("api/Estados/" + self.articulo.estado.id + "/GetMunicipio").then((res) => {
          self.municipios = res.data
        });
      },
      obtiene_categorias: function () {
        const self = this
        getAPI.get("Recursos/api/Categorias").then((res) => {
          self.categorias = res.data
        });
      },
      addNewTag() {
        if (this.search != null || (this.search.trim()) != '') {


          this.tags.push({slug: this.search});
          this.articulo.categoria.push(this.search);
        }
      },


      postArticulos: async function () {

        var self = this
        let a = this.$refs.form.validate();
        if (!a)
          return

        let formData = new FormData()
        for (let file in this.files) {
          console.log(this.files[file])
          formData.append("image", this.files[file])
        }

        formData.append("nombreRecurso", this.articulo.nombre);
        formData.append("descripcion", this.articulo.descripcion);
        formData.append("Usuario", 1);
        formData.append("estado", this.articulo.estado.id);
        formData.append("html", this.articulo.html);
        formData.append("municipio", this.articulo.municipio.id);
        formData.append("tags", JSON.stringify(this.articulo.categoria));
        formData.append("autores", this.articulo.autores);
        formData.append("institucion", this.articulo.instituto.id);

        console.log(JSON.stringify(this.articulo.categoria))

        await getAPI.post("Recursos/api/Articulos/",
          formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        ).then((res) => {

          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Tu Recurso se ha guardado con éxito',
            showConfirmButton: false,
            timer: 1500
          }).then((e) => {
            this.$router.push({name: 'Perfil'})
          })


        });
      },

      get_tags: function () {
        self = this
        getAPI.get("/Recursos/api/Articulos/Tags/").then((response) => {

          self.tags = response.data;

        });
      },
      get_institucion: function () {
        self = this
        getAPI.get("/api/Instituciones/").then((response) => {

          self.institutos = response.data;

        });
      },

      imagen() {
        console.log(this.files)
        // console.log(this.user.profile.telefono)
      },


    },
    watch: {
      "articulo.categoria"() {
        this.search = ""
      }


    },
  }
</script>

<style scoped>

</style>
