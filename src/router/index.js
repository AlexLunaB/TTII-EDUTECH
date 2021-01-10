import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
import Login from "../Layout/Login";
import DashBoard from "../Layout/DashBoard";
import CatalogoServicios from "../Layout/CatalogoServicios";
import ErrorComponent from "../components/ErrorComponent";
import MapaComponent from "../components/MapaComponent";
import Blog from "../components/Blog";
import Perfil from "../components/PerfilComponents/Perfil";
import store from '../store'
import AddPost from "../components/Blog/AddPost"
import AddRecurso from "../components/Recursos/AddRecurso"

import BlogDetail from "../components/BlogComponents/BlogDetail"
import BuscadorLayout from "../components/Buscador/BuscadorLayout"
Vue.use(VueRouter)
const router = new VueRouter({
  routes: [

    {
      path: '/Login',
      name: 'Login',
      component: Login,
      children: []
    },
    {
      path: '/',
      name: "DashBoard",
      component: DashBoard,
      meta: {rutaProtegida: true},
      children: [
        {
          path: "Inicio",
          name: "Mapa",
          component: MapaComponent,
          meta: {rutaProtegida: true}
        },


        {
          path: "Servicios",
          name: "CatalogoServicios",
          component: CatalogoServicios,
          meta: {rutaProtegida: true},
        },
        {
          path: "Blog",
          name: "Blog",
          component: Blog,
          meta: {rutaProtegida: true},
        },
        {
          path: "Blog/CrearPublicacion",
          name: "AddPub",
          component: AddPost,
          meta: {rutaProtegida: true},
        },
        {
          path: "Recurso/Add",
          name: "AddRecurso",
          component: AddRecurso,
          meta: {rutaProtegida: true},
        },
        { path: '/Blog/:id', component: BlogDetail , name:"post"},
        {
          path: "Buscador",
          name: "Buscador",
          component: BuscadorLayout,
          meta: {rutaProtegida: true},
        },

        {
          path: "Perfil",
          name: "Perfil",
          component: Perfil,
          meta: {rutaProtegida: true},
        }
      ]
    },

    {
      path: '*',
      name: "ErrorComponent",
      component: ErrorComponent,
      meta: {rutaProtegida: true},
    }
  ],
  mode: "history"
});

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes
// })

// export default router

router.beforeEach((to, from, next) => {
  // alert(to.meta.rutaProtegida)
  // console.log(to.meta.rutaProtegida)
  if(to.meta.rutaProtegida) {
    if(store.getters.loggedIn) {
      next()
    } else {
      next('/Login')
    }
  } else {
    next();
  }
})
export default router
