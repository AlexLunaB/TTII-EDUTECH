<template>
<div style="background-color: #eeeeee">
    
    <div class="mainbox">
        <h1 style="text-align: center; ">Tenemos un problema</h1>
        
        <i class="far fas fa-ban"></i>
        <div class="msg">No tienes permisos para acceder a este espacio.  
            <p>Solicita permisos a un administrador.</p>
            <p>Vuelve al <router-link :to="{path: '/Inicio' }">Inicio</router-link> para seguir explorando</p>
        </div>
    </div>
</div>
    
  
</template>

<script>
export default {

}
</script>

<style scoped>
.mainbox {
  background-color: #95c2de;
  margin: auto;
  height: 600px;
  width: 600px;
  position: relative;
}

  .err {
    color: #ffffff;
    font-family: 'Nunito Sans', sans-serif;
    font-size: 11rem;
    position:absolute;
    left: 20%;
    top: 8%;
  }

.far {
  position: absolute;
  font-size: 8.5rem;
  left: 42%;
  top: 15%;
  color: #ffffff;
}

 .err2 {
    color: #ffffff;
    font-family: 'Nunito Sans', sans-serif;
    font-size: 11rem;
    position:absolute;
    left: 68%;
    top: 8%;
  }

.msg {
    text-align: center;
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.6rem;
    position:absolute;
    left: 16%;
    top: 45%;
    width: 75%;
  }

a {
  text-decoration: none;
  color: white;
}

a:hover {
  text-decoration: underline;
}
</style>

