<template>
  <header id="header">
    <div class="center">
      <!-- LOGO -->
      <div id="logo">
        <img src="../assets/logo.png" class="app-logo" alt="Logotipo" />
        <span id="brand"> <strong>Observatorio</strong> </span>
      </div>

      <!-- MENU -->
      <nav id="menu">
        <ul>
          <li>
            <router-link to="/home" active-class="active"> Inicio </router-link>
          </li>
          <li>
            <router-link to="/blog" active-class="active"> Blog </router-link>
          </li>
          <li>
            <router-link to="/formulario" active-class="active"> Formulario </router-link>
          </li>
          <li>
            <!-- pasando un objeto -->
            <router-link :to="{ name:'pagina', params: {id: 'Soy el valor del parametro'} }" active-class="active" > Pagina1 </router-link>
          </li>
          <li>
            <router-link to="/mi-componente" active-class="active"> Pagina2 </router-link>
          </li>
        </ul>
      </nav>

      <!--LIMPIAR FLOTADOS-->
      <div class="clearfix"></div>
    </div>
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>