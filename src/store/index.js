import Vue from 'vue'
import Vuex from 'vuex'
import {axiosBase} from '../Api/axios-base'
import router from '../router'
import Swal from "sweetalert2";

Vue.use(Vuex)


export default new Vuex.Store({
  state: {





    buscador:'',



    accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
    // refreshing the page
    refreshToken: localStorage.getItem('refresh_token') || null,
    APIData: '',// received data from the backend API is stored here.
    user: {}
  },
  getters: {
    loggedIn(state) {

      return state.accessToken != null
    }
  },
  mutations: {
    updateLocalStorage(state, {access, refresh, user}) {
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
      localStorage.setItem('Usuario', user)
      state.accessToken = access
      state.refreshToken = refresh
      state.user = user
    },
    updateAccess(state, access) {
      state.accessToken = access
      localStorage.setItem('access_token', access)

    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
    },
    ActualizaBuscador(state,search) {
      state.buscador = search
    }


  },
  actions: {
    // run the below action to get a new access token on expiration
    refreshToken(context) {
      return new Promise((resolve, reject) => {
        axiosBase.post('Usuarios/api/token/refresh/', {
          refresh: context.state.refreshToken
        }) // send the stored refresh token to the backend API
          .then(response => { // if API sends back new access and refresh token update the store
            console.log('New access successfully generated')
            context.commit('updateAccess', response.data.access)

            resolve(response.data.access)
          })
          .catch(err => {
            router.push({name: 'Login'})
            console.log('error in refreshToken Task')


            reject(err) // error generating new access and refresh token because refresh token has expired


          })
      })
    },
    registerUser(context, data) {
      return new Promise((resolve, reject) => {
        axiosBase.post('/register', {
          name: data.name,
          email: data.email,
          username: data.username,
          password: data.password,
          confirm: data.confirm
        })
          .then(response => {
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    logoutUser(context) {
      if (context.getters.loggedIn) {
        try {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          context.commit('destroyToken')
          router.push({name: 'Login'})
        } catch (error) {
          console.log(error)
        }

        // return new Promise((resolve, reject) => {
        //   axiosBase.post('/api/token/logout/')
        //     .then(response => {
        //       localStorage.removeItem('access_token')
        //       localStorage.removeItem('refresh_token')
        //       context.commit('destroyToken')
        //       router.push({name: 'Login'})
        //     })
        //     .catch(err => {
        //       localStorage.removeItem('access_token')
        //       localStorage.removeItem('refresh_token')
        //       context.commit('destroyToken')
        //       router.push({name: 'Login'})
        //       resolve(err)
        //     })
        // })
      }
    },
    loginUser(context, credentials) {
      return new Promise((resolve, reject) => {
        // send the username and password to the backend API:
        axiosBase.post('Usuarios/api/token/', {


          username: credentials.username,
          password: credentials.password
        })
          // if successful update local storage:
          .then(response => {
            context.commit('updateLocalStorage', {
              access: response.data.access,
              refresh: response.data.refresh,
              user: JSON.stringify(response.data.user)
            }) // store the access and refresh token in localstorage

            resolve()
          })
          // console.log(state.accessToken)
          // console.log(state.refreshToken)
          .catch(err => {
            reject(err)
          })
      })
    }
  }
})
