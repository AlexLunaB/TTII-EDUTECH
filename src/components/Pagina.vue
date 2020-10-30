<template>
  <section id="content">
    <h2 class="subheader">Página de pruebas</h2>
    <h3>{{ id_desde_url }}</h3>
    <button @click="actualizarNombre()">Actualizar Nombre</button>
    <button @click="redirigirAlBlog()">Redirigir</button>
    <h4>{{nombre}}</h4>
  </section>
</template>

<script>
export default {
  name: "Pagina",
  //cuando el componente se crea y no se ha terminado de cargar totalmente
  created() {
    console.log("Componente creado ¡");
  },
  //se ejecuta al cargar el componente cuando el componente se monta
  mounted() {
    this.id_desde_url = this.$route.params.id;
    console.log("Componente montado¡");
  },
  //cada que el componente se actualiza
  updated() {
    console.log("Componente actualizado");
  },
  //cuando el componente se elimina
  destroyed() {
    console.log("Componente eliminado");
  },
  data() {
    return {
      id_desde_url: null,
      nombre: "Luis Pavel"
    };
  },
  methods: {
    actualizarNombre() {
      this.nombre = "LUIS PAVEL VARELA";
      console.log(this.nombre);
    },
    redirigirAlBlog(){
      this.$router.push('/blog');
    }
  }
};
</script>