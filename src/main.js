// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from "vuex"
import store from "./store/index"

import BlockUI from 'vue-blockui'


import VueToast from 'vue-toast-notification';
// Import any of available themes
import 'vue-toast-notification/dist/theme-sugar.css';
//import 'vue-toast-notification/dist/dist/theme-sugar.css';

import VueNativeSock from "vue-native-websocket";


Vue.use(VueNativeSock, 'ws://'+process.env.VUE_APP_BASE_URL+'/ws/servicio/' + '?token=' + localStorage.getItem("access_token"), {
  store: store,
  format: 'json',
  reconnection: true, // (Boolean) whether to reconnect automatically (false)
  //reconnectionAttempts: 5, // (Number) number of reconnection attempts before giving up (Infinity),
  reconnectionDelay: 3000 ,// (Number) how long to initially wait before attempting a new (1000)
  connectManually: true,

});
Vue.use(VueToast);
Vue.$toast.open({
        message: "Test message from Vue",
        type: "success",
        duration: 5000,
        dismissible: true
      })

Vue.use(BlockUI)
Vue.use(Vuex)
Vue.config.productionTip = false

import vuetify from "../plugins/vuetify";
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  vuetify,
  components: { App },
  template: '<App/>'
})
