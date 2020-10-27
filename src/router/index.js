import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import DashBoard from "../Layout/DashBoard";
import Home from "../Layout/Home";
import CatalogoServicios from "../Layout/CatalogoServicios";


Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/',
      name: 'Login',
      component: Login,
      children: []
    },

    {

      path: '/Inicio',
      name: "DashBoard",
      component: DashBoard,
      children: [
        {
          path: "dashboard",
          name: "Dashboard",
          component: Home
        },
        {
          path: "Servicios",
          name: "CatalogoServicios",
          component: CatalogoServicios

        }
      ]
    }
  ],
  mode: "history"
});
