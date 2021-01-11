<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="6" sm="12">

        <v-card>

          <v-row class="pa-3">
            <v-col offset="1" cols="10" align="center">
              <v-avatar size="200">
                <v-img class="card-img" :src="perfil.foto"></v-img>
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

      <v-col cols="12" md="6" sm="12">
        <v-row>

          <v-col cols="12" md="12" sm="12">
            <v-card>

              <v-card-title>Mis Recursos</v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                sort-by="calories"
                class="elevation-1"
              >
                <template v-slot:top>
                  <v-toolbar
                    flat
                  >
                    <v-toolbar-title>Mis Recursos</v-toolbar-title>
                    <v-divider
                      class="mx-4"
                      inset
                      vertical
                    ></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog
                      v-model="dialog"
                      max-width="500px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          color="primary"
                          dark
                          class="mb-2"
                          v-bind="attrs"
                          v-on="on"
                        >
                          Nuevo Reurso
                        </v-btn>
                      </template>
                      <v-card>
                        <v-card-title>
                          <span class="headline">{{ formTitle }}</span>
                        </v-card-title>
            
                        <v-card-text>
                          <v-container>
                            <v-row>
                              <v-col
                                cols="12"
                                sm="6"
                                md="4"
                              >
                                <v-text-field
                                  v-model="editedItem.name"
                                  label="Dessert name"
                                ></v-text-field>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="6"
                                md="4"
                              >
                                <v-text-field
                                  v-model="editedItem.calories"
                                  label="Calories"
                                ></v-text-field>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="6"
                                md="4"
                              >
                                <v-text-field
                                  v-model="editedItem.fat"
                                  label="Fat (g)"
                                ></v-text-field>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="6"
                                md="4"
                              >
                                <v-text-field
                                  v-model="editedItem.carbs"
                                  label="Carbs (g)"
                                ></v-text-field>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="6"
                                md="4"
                              >
                                <v-text-field
                                  v-model="editedItem.protein"
                                  label="Protein (g)"
                                ></v-text-field>
                              </v-col>
                            </v-row>
                          </v-container>
                        </v-card-text>
            
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="close"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="save"
                          >
                            Save
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                      <v-card>
                        <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                          <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                          <v-spacer></v-spacer>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                  <v-icon
                    small
                    class="mr-2"
                    @click="editItem(item)"
                  >
                    mdi-pencil
                  </v-icon>
                  <v-icon
                    small
                    @click="deleteItem(item)"
                  >
                    mdi-delete
                  </v-icon>
                </template>
                <template v-slot:no-data>
                  <v-btn
                    color="primary"
                    @click="initialize"
                  >
                    Reset
                  </v-btn>
                </template>
              </v-data-table>

              <v-card-actions>
                <v-btn color="primary" router :to="{ name: 'AddRecurso'}">Agregar un recurso</v-btn>
              </v-card-actions>
            </v-card>


          </v-col>


          <v-col cols="12" md="12" sm="12">
            <v-card>

              <v-toolbar flat color="primary" dark>
                <v-toolbar-title>Mis Artículos</v-toolbar-title>
              </v-toolbar>
            </v-card>

          </v-col>


        </v-row>
      </v-col>


    </v-row>


  </v-container>
</template>

<script>
  import {getAPI} from "../../Api/axios-base";

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
        },
        nombre: "Luis Pavel",
        apellidoP: "Varela",
        apellidoM: "Aguilar",
        tipoUsuario: "Tipo de usuario",
        emailUsuario: "luispavelvarela@gmail.com",
        values: [],
        value: null,
        categorias: [],
        items_list: ["Dog Photos", "Cat Photos", "", "Potatoes", "Carrots"],
        model: ["Carrots"],
        items: [
          {
            text: "Nature",
            icon: "mdi-nature",
          },
          {
            text: "Nightlife",
            icon: "mdi-glass-wine",
          },
          {
            text: "November",
            icon: "mdi-calendar-range",
          },
          {
            text: "Portland",
            icon: "mdi-map-marker",
          },
          {
            text: "Biking",
            icon: "mdi-bike",
          },
        ],
        loading: false,
        search: "",
        selected: [],

        // para el data table
        dialog: false,
        dialogDelete: false,
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Actions', value: 'actions', sortable: false },
        ],
        // PARA RECURSOS
        headers2: [
          {
            text: 'Nombre recurso',
            align: 'start',
            sortable: false,
            value: 'nombre',
          },
          { text: 'Fecha', value: 'fecha'},
          { text: 'Calificación promedio', value: 'calificacion'},
          { text: 'Acciones', value: 'actions', sortable: false},

        ],
        // PARA RECURSOS
        losRecursos: [],
        desserts: [],
        editedIndex: -1,
        editedRecurso: {
          nombre: '',
          fecha: '',
          calificacion: 0, 
        },
        editedItem: {
          name: '',
          calories: 0,
          fat: 0,
          carbs: 0,
          protein: 0,
        },
        defaultItem: {
          name: '',
          calories: 0,
          fat: 0,
          carbs: 0,
          protein: 0,
        },

      };
    },

    computed: {
      allSelected() {
        return this.selected.length === this.items.length;
      },
      categories() {
        const search = this.search.toLowerCase();

        if (!search) return this.items;

        return this.items.filter((item) => {
          const text = item.text.toLowerCase();

          return text.indexOf(search) > -1;
        });
      },
      selections() {
        const selections = [];

        for (const selection of this.selected) {
          selections.push(selection);
        }

        return selections;
      },
      formTitle() {
         return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      values() {
        this.search = "";
      },
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    methods: {
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
        getAPI.get("Usuarios/View/profile/").then((response) => {

          self.perfil.email = response.data.email;
          self.perfil.nombre = response.data.first_name;
          self.perfil.apellidos = response.data.last_name;
          self.perfil.usuario = response.data.username;
          self.perfil.foto = response.data.profile.foto;
          self.perfil.semblanza = response.data.profile.semblanza;
          self.perfil.intereses = response.data.profile.intereses;
        });

      },

      get_tags: function () {
        self = this
        getAPI.get("Usuarios/View/Tags/").then((response) => {

          self.tags = response.data;

        });


      },
      next() {
        this.loading = true;

        setTimeout(() => {
          this.search = "";
          this.selected = [];
          this.loading = false;
        }, 2000);
      },
      addNewTag() {
        if (this.search != null || (this.search.trim()) != '') {
          alert(this.search.trim())
          this.tags.push({slug: this.search});
          this.values.push({slug: this.search});
        }

      },
      initialize () {
        this.desserts = [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
          },
        ]
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.desserts.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      },
    },

    mounted() {
      // this.obtiene_clasificacion();
      this.obtiene_datos_usuario();
      this.get_tags()
    },
  };
</script>

<style scoped>
  .background {
    background-color: #367cff;
  }
</style>
