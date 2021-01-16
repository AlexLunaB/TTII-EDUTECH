<template>
    <div class="comments-outside">
      <div class="comments-header">
        <div class="comments-stats">
            <!-- <span><i class="fa fa-thumbs-up"></i> {{ likes }}</span> -->
            <span><i class="fa fa-comment"></i> {{ comments.length }}</span>
          </div>
          <div class="post-owner">
            <div class="avatar">
              <img :src="perfil.foto" alt="">
            </div>
            <div class="username">
              <a href="#">@{{ perfil.usuario }}</a>
            </div>
          </div>
        </div>
        <CommentsBlog
          :comments_wrapper_classes="['custom-scrollbar', 'comments-wrapper']"
          :comments="comments"
          :current_user="current_user"
          :perfil = perfil
          @submit-comment="submitComment"
        ></CommentsBlog>
    </div>
</template>

<script>
import CommentsBlog from './CommentsBlog'
import Swal from 'sweetalert2'
import { getAPI } from '../../Api/axios-base'

export default {
  name: 'app',
  props: {
    perfil: {},
    id: '',
    Post: {}
  },
  components: {
    CommentsBlog
  },
  data() {
    return {
      likes: 15,
      creator: {
        avatar: 'http://via.placeholder.com/100x100/a74848',
        user: 'exampleCreator'
      },
      current_user: {
        avatar: 'http://via.placeholder.com/100x100/a74848',
        user: 'exampler'
      },
      comments: this.Post.comentarioblog_set
        // {
        //   id: 1,
        //   user: 'example',
        //   avatar: 'http://via.placeholder.com/100x100/a74848',
        //   text: 'lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor ',
        // },
        // {
        //   id: 2,
        //   user: 'example1',
        //   avatar: 'http://via.placeholder.com/100x100/2d58a7',
        //   text: 'lorem ipsum dolor',
        // },
        // {
        //   id: 3,
        //   user: 'example2',
        //   avatar: 'http://via.placeholder.com/100x100/36846e',
        //   text: 'lorem ipsum dolor again',
        // },
      
    }
  },
  methods: {
    submitComment: async function(reply) {
      // this.comments.push({
      //   id: this.comments.length + 1,
      //   usuario: this.perfil.usuario,
      //   avatar: this.perfil.foto,
      //   text: reply
      // });

      const self = this
      try {
          const res = await getAPI.post("Foro/api/Post/"+this.id+"/Comentar/",
          {"comentario": reply})
          // this.comments = this.Post.comentario_set

          console.log('comments', this.comments)
          // console.log('Post desde CommentsApp', this.Post)

          // console.log(this.id)
          // alert(JSON.stringify(res))

          Swal.fire({
              icon: 'success',
              title: '¡Registro exitoso!',
              text: 'Comentario publicado con exito',
              footer: 'Regresa al Login para iniciar sesión'
          })

          setTimeout(function()
          { 
            // alert("Hello"); 
            location.reload()
          }, 2000);
          

          
      } catch (error) {
          console.log(error)
          Swal.fire({
              icon: 'error',
              title: 'ERROR...',
              text: 'Algo no salio bien',
              footer: 'Intenta de nuevo'
          })
          // location.reload()
      }
    }
  }
}
</script>


<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
a {
  text-decoration: none;
}
hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 1px solid #ececec;
  margin: 1em 0;
  padding: 0;
}
.comments-outside {
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
  margin: auto;
}
.comments-header {
  background-color: #C8C8C8;
  padding: 10px;
  align-items: center;
  display: flex;
  justify-content: space-between;
  color: #333;
  min-height: 80px;
  font-size: 20px;
}

.comments-header .comments-stats span {
  margin-left: 10px;
}

.post-owner {
  display: flex;
  align-items: center;
}

.post-owner .avatar > img {
  width: 30px;
  height: 30px;
  border-radius: 100%;
}

.post-owner .username {
  margin-left: 5px;
}

.post-owner .username > a {
  color: #333;
}
</style>