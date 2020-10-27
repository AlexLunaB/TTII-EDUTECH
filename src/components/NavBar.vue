<template>
<nav>

  <v-navigation-drawer permanent v-model="drawer" dark app mini-variant mini-variant-width="100" class="cyan darken-1 barra">

    <v-list flat>
      <v-list-item  router to="/Inicio/dashboard">
        <v-list-item-content>
          <v-icon class="mb-2">dashboard</v-icon>
          <v-list-item-subtitle class="text-center">Inicio</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item  router to="/Inicio/Servicios">
        <v-list-item-content>
          <v-icon class="mb-2">fas fa-briefcase</v-icon>
          <v-list-item-subtitle class="text-center">Servicios</v-list-item-subtitle>
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
            drawer: true,
          }
        }
    }
</script>

<style scoped>
.barra  {
  padding: 0;
}

</style>
