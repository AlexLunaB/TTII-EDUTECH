import Vue from 'vue'
import Router from 'vue-router'
import Login from "../Layout/Login";
import DashBoard from "../Layout/DashBoard";
import CatalogoServicios from "../Layout/CatalogoServicios";
import ErrorComponent from "../components/ErrorComponent";
import MapaComponent from "../components/MapaComponent";
import InfoMaterialEstado from "../components/InfoMaterialEstado"
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
          path: "Inicio",
          name: "Mapa",
          component: MapaComponent,
          children: []
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
        },
        {
          path: "InfoMaterialEstado",
          name: "InfoMaterialEstado",
          component: InfoMaterialEstado
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
