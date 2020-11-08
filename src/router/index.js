import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import DashBoard from "../Layout/DashBoard";
import Home from "../Layout/Home";
import CatalogoServicios from "../Layout/CatalogoServicios";
import Inicio from "../components/Inicio";
import ErrorComponent from "../components/ErrorComponent";
import MapaComponent from "../components/MapaComponent";
import Blog from "../components/Blog";

Vue.use(Router)
export default new Router({
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
      children: [
        {
          path: "dashboard",
          name: "Dashboard",
          component: MapaComponent
        },
        {
          path: "Servicios",
          name: "CatalogoServicios",
          component: CatalogoServicios

        },
        {
          path: "Blog",
          name: "Blog",
          component: Blog
        }
      ]
    },


    {
      path: '*',
      name: "ErrorComponent",
      component: ErrorComponent
    }
  ],
  mode: "history"
});
