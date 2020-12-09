<template>
<nav>
  <v-navigation-drawer 
    permanent v-model="drawer" 
    app mini-variant mini-variant-width="100" 
    class="barra"
    expand-on-hover
    dark
  >

    <v-list>
      <v-list-item>
        <v-layout justify-center>
          <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/women/85.jpg" class="text-center"></v-img>
          </v-list-item-avatar>
        </v-layout>
        
      </v-list-item>

      <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="title">
                {{nombre}}
              </v-list-item-title>
              <v-list-item-subtitle>{{correo}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
    </v-list>

    <v-list>
      <v-list-item  router to="/Inicio">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-globe-americas</v-icon>
          <v-list-item-subtitle class="text-center">Inicio</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item  router to="/Servicios">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-briefcase</v-icon>
          <v-list-item-subtitle class="text-center">Servicios</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item router to="/Blog">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-book-reader</v-icon>
          <v-list-item-subtitle class="text-center">Blog</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item router to="/InfoMaterialEstado">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-book-reader</v-icon>
          <v-list-item-subtitle class="text-center">MaterialEstado</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-list style="position: absolute; bottom: 0" class="ml-3">
      <v-list-item>
        <v-list-item-action>
          <v-icon right>fas fa-sign-out-alt</v-icon>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</nav>
</template>

<script>
  export default {
      name: "Navbar",
      data(){
        return {
          nombre: 'Nombre Apellido',
          correo: 'correo@dominio.com',
          drawer: true,
        }
      }
  }
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
