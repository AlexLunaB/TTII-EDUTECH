<template>
  <v-container>


    <BlockUI v-if="alerta" :message="msg">
      <i class="fa fa-cog fa-spin fa-3x fa-fw"></i>

    </BlockUI>

    <v-row>
      <v-col md="6">
        <v-card

          v-for="Servicio in Servicios"

          :key="Servicio.id"

          class="mx-auto mt-12"
        >
          <v-img
            height="250"
            :src=Servicio.Imagen
          ></v-img>

          <v-card-title>Servicio De Café</v-card-title>

          <v-card-text>
            <v-row
              align="center"
              class="mx-0"
            >
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              ></v-rating>

              <div class="grey--text ml-4">
                4.5 (413)
              </div>
            </v-row>

            <div class="my-4 subtitle-1">
              $ 0.0
            </div>

            <div>{{Servicio.descripcion_servicio}}</div>
          </v-card-text>

          <v-divider class="mx-4"></v-divider>
          <v-card-text>

          </v-card-text>

          <v-card-actions>
            <v-btn
              color="deep-purple lighten-2"
              text
              @click="reserve(Servicio)"
            >
              Solicitar Servicio
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {getAPI} from "../Api/axios-base"
  import Swal from 'sweetalert2'
  import APIUrl from "../Api/axios-base"

  export default {
    name: "CatalogoServicios",


    computed: {
      Mensaje() {
        return this.$store.state.socket.message
        // Or return basket.getters.fruitsCount
        // (depends on your design decisions).
      },
    },

    watch: {
      Mensaje(a, b) {
        self=this

        console.log(a)
        console.log(b)
        if (a.event == "Buscando") {

          self.msg = "Se esta buscando quien acepte su petición"


        } else if (a.event == "Encontrado") {

          self.alerta = false

          Swal.fire({
            icon: "success",
            text: "Servicio En Proceso",
          })

        }

      }

    },

    data() {
      return {


        alerta: false,


        Servicios: [],
        msg: ""


      }
    },


    mounted() {
      this.ObtieneCatalogo()

    },


    methods: {

      ObtieneCatalogo: function () {

        getAPI.get("acciones/api/CatalogoServicio/").then(
          (response) => {
            this.Servicios = response.data
            console.log(response)
          }
        )

      },
      reserve: function (item) {
        var self = this


        Swal.queue([{
          title: 'Confirma Servicio',
          confirmButtonText: 'Aceptar',
          text:"Estas seguro de iniciar tu Servicio",
          showLoaderOnConfirm: true,
          preConfirm: () => {
            self.msg = "Estamos inicializando Su servicio"
            self.alerta = true


            return getAPI.post("acciones/api/Servicio_Cliente/", {

              servicio: item.id_servicio

            }).then(
              (response) => {
                self.msg = "Estamos buscando quien atienda su petición"
                const token = this.$store.state.accessToken
              })
          }
        }
        ])


        console.log(item)


      }
    }
  }
</script>

<style scoped>


</style>
