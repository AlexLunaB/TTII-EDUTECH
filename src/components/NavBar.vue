<template>
<nav>
  <v-navigation-drawer 
    v-model="drawer" 
    app mini-variant mini-variant-width="100" 
    class="barra"
  
    dark
  >

    <v-list>
      <v-list-item router to="/Perfil">
        <v-layout justify-center>
          <v-list-item-avatar>
            <v-img :src=perfil.foto></v-img>
          </v-list-item-avatar>
        </v-layout>        
      </v-list-item>

      <v-list-item router to="/Perfil">
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ perfil.nombre}}
          </v-list-item-title>
          <v-list-item-subtitle>{{perfil.usuario}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-list>
      <v-list-item  router to="/Perfil">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-user</v-icon>
          <v-list-item-subtitle class="text-center">Perfil</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item  router to="/Inicio">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-globe-americas</v-icon>
          <v-list-item-subtitle class="text-center">Inicio</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item router to="/Buscador">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-search</v-icon>
          <v-list-item-subtitle>Buscador</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item router to="/Blog">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-book-reader</v-icon>
          <v-list-item-subtitle class="text-center">Blog</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="logoutUser" v-if="loggedIn">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-sign-out-alt</v-icon>
          <v-list-item-subtitle class="text-center">Salir</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <!-- <v-list style="position: absolute; bottom: 0" class="ml-3" v-if="loggedIn" @click="logoutUser">
      <v-list-item>
        <v-list-item-action>
          <v-icon right>fas fa-sign-out-alt</v-icon>
        </v-list-item-action>
      </v-list-item>
    </v-list> -->
  </v-navigation-drawer>
  
</nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { getAPI } from "../Api/axios-base";
export default {
  name: "Navbar",
  data(){
    return {
      perfil: {
        email: null,
        nombre: null,
        apellidos: null,
        usuario: null,
        foto: null,
        municipio: null,
        intereses: [],
      },
      nombre: 'Nombre Apellido',
      correo: 'correo@dominio.com',
      drawer: true,
    };
  },

  methods: {
    obtiene_datos_usuario: function () {
      const self = this;
      getAPI.get("Usuarios/View/profile/").then((response) => {
        console.log(response)
        self.perfil.email = response.data.email;
        self.perfil.nombre = response.data.first_name;
        self.perfil.apellidos = response.data.last_name;
        self.perfil.usuario = response.data.username;
        self.perfil.foto = response.data.profile.foto;
      });
    },

    ...mapActions(['logoutUser'])
  },

  mounted() {
    this.obtiene_datos_usuario();
  },

  computed: {
    ...mapGetters(['loggedIn'])
  },
};
</script>

<style scoped>
.barra  {
  padding: 0;
  background-color: #222831;
}

.slide-enter,
.slide-leave-to{
  opacity: 0;
  transform: translateX(-30%);
}

</style>
