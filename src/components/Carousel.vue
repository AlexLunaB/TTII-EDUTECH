<template>
  <v-carousel 
    show-arrows-on-hover
    height="150px">
    
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>
</template>


<script>
  export default {
    data () {
      return {
        items: [
          {
            src: 'https://ep01.epimg.net/elpais/imagenes/2019/10/30/album/1572424649_614672_1572453030_noticia_normal.jpg',
          },
          {
            src: 'https://www.quo.es/wp-content/uploads/2019/10/los-cinco-trabajos-que-por-ahora-no-podra-quitarte-un-robot.jpg',
          },
          {
            src: 'https://i.blogs.es/594843/chrome/1366_2000.jpg',
          },
          {
            src: 'https://cde.laprensa.e3.pe/ima/0/0/2/3/8/238082.jpg',
          },
        ],
      }
    },
  }
</script>