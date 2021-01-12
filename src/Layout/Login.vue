<template >
  <v-app :style="login">
    <v-main>
      <v-container class="fill-height" fluid>

        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">

                  <v-row>
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 primary--text text--accent-2">
                          EdutechMap

                        </h1>

                        <!-- <div class="text-center" mt-4>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-facebook-f</v-icon>

                          </v-btn>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-twitter</v-icon>
                          </v-btn>
                        </div> -->

                        <h4 class="text-center mlt-4">Logueate</h4>
                        <v-form >
                          <v-text-field
                            label="Usuario"
                            name="username"
                            prepend-icon="person"
                            type="text"
                            v-model="username"
                            color="teal accent-3">
                          </v-text-field>
                          <v-text-field
                            label="Contraseña"
                            name="password"
                            v-model="password"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            v-on:keyup.enter="loginUser">
                          </v-text-field>
                        </v-form>

                        <!-- <h3 class="text-center mt-3"> ¿Olvidaste tu contraseña?</h3> -->
                        <!-- <h3 class="text-center mt-3" @click="abreOlvidoContra"> ¿Olvidaste tu contraseña?</h3> -->

                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn rounded color="primary accent-3" @click="loginUser" dark>Inicia Sesión</v-btn>
                      </div>
                    </v-col>


                    <v-col cols="12" md="4" class="primary accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Hola Bienvenido!</h1>
                        <h5 class="text-center"></h5>
                        <div class="text-center">
                          <v-btn rounded outlined="" dark @click="step++">
                            Registrate

                          </v-btn>
                        </div>

                      </v-card-text>


                    </v-col>
                  </v-row>


                </v-window-item>
                <v-window-item :value="2">

                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="primary accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Regresa</h1>
                        <h5 class="text-center"> Unete a la mayor red de recursos tecnoeducativos</h5>
                      </v-card-text>

                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step--">Regresa al Login</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text>
                        <h1 class="text-center display-2 primary--text text--accent-3">Crear Cuenta</h1>
                      <!-- <div class="text-center mt-4">
                        <v-btn class="mx-2" fab >
                          <v-icon>fab fa-facebook</v-icon>
                        </v-btn>
                      </div> -->

                        <div>
                          <h4 class="text-center ">Verifica tu correo</h4>
                          <v-form ref="form">
                            
                            <v-text-field
                            label="Correo"
                            name="email"
                            prepend-icon="email"
                            type="text"
                            color="teal accent-3"
                            v-model="datosUsuario.email"
                            :rules="emailRules">
                            </v-text-field>

                            <v-text-field
                            label="Nombre de usuario"
                            name="username"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3"
                            v-model="datosUsuario.username">
                            </v-text-field>

                            <v-text-field
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            v-model="datosUsuario.password"
                            :rules="passwordRules">
                            </v-text-field>

                            <v-text-field
                            label="Confirmar contraseña"
                            name="password_confirmation"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            v-model="datosUsuario.password_confirmation"
                            :rules="passwordRules">
                            </v-text-field>

                            <v-text-field
                            label="Nombre(s)"
                            name="first_name"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3"
                            v-model="datosUsuario.first_name"
                            :rules="nameRules">
                            </v-text-field>

                            <v-text-field
                            label="Apellidos"
                            name="last_name"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3"
                            v-model="datosUsuario.last_name"
                            :rules="nameRules">
                            </v-text-field>


                            <v-checkbox 
                            v-model="firstcheckbox" 
                            :rules="[v => !!v || 'Debes estar de acuerdo para continuar']"
                            label="Acepto los Terminos y Condiciones" 
                            @click="abreTerminosCondiciones"
                            required>
                            </v-checkbox>
                            
                            

                            
                          </v-form>
                        </div>


                      </v-card-text>
                      <div class="text-center mt-n5">
                          <v-btn color="primary" @click="postRegistro"> Registrate!</v-btn>

                      </div>

                    </v-col>
                  </v-row>


                </v-window-item>


              </v-window>

            </v-card>
          </v-col>
        </v-row>

      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Swal from 'sweetalert2'
import { getAPI } from '../Api/axios-base'
  export default {
    name: 'login',

    data() {
      return {
        step: 1,
        username: '',
        password: '',
        wrongCred: false, // activates appropriate message if set to true

        login: { 
          backgroundImage: 'url(../../static/images/Cables.jpg)' ,
          // background: 'grey'
          
        },

        datosUsuario: {
          email: '',
          username: '',
          password: '',
          password_confirmation: '',
          first_name: '',
          last_name: ''
        },

        nameRules: [
          v => !!v || 'Se requiere un nombre',
          v => (v && v.length <= 20) || 'Máximo 20 caracteres',
        ],

        emailRules: [
          v => !!v || 'Correo necesario',
          v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'El correo debe ser valido',
        ],

        passwordRules: [
          v => !!v || 'Contraseña necesaria',

          v => (v && v.length >= 8) || 'La contraseña debe contener al menos 8 caracteres',
          v => /(?=.*[A-Z])/.test(v) || 'Debe tener al menos una letra mayuscula',
          v => /(?=.*\d)/.test(v) || 'Debe tener al menos un número',
          v => /([!@$%])/.test(v) || 'Debe tener al menos un caracter especial [!@#$%]',

          v => v === this.datosUsuario.password || 'Las contraseñas no coinciden'



          // v => /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/.test(v) || 'La contraseña debe contener al menos una minuscula, un número, un caracter especial y una letra mayuscula.',
        ],

        firstcheckbox: false,

        dialog: false,
        
      }
    },
    methods: {
      loginUser() { // call loginUSer action
        this.$store.dispatch('loginUser', {
          username: this.username,
          password: this.password
        })
          .then(() => {
            this.wrongCred = false
            this.$router.push({name: 'Mapa'})
          })
          .catch(err => {
            Swal.fire({
              icon: 'error',
              title: 'ERROR...',
              text: '¡Usuario / Contraseña incorrecto!',
              footer: 'Intenta de nuevo'
            })
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
      },

      postRegistro: async function() {
        // const self = this
        // await getAPI.post("Usuarios/View/signup/",
        //     {"email":self.datosUsuario.email, "username":self.datosUsuario.username, 
        //     "password":self.datosUsuario.password,"password_confirmation":self.datosUsuario.password_confirmation, 
        //     "first_name":self.datosUsuario.first_name, "last_name": self.datosUsuario.last_name}).then((res)=> {
        //   alert(JSON.stringify(res))
          
        // });


        if(this.$refs.form.validate()) {

          const self = this
          try {
            const res = await getAPI.post("Usuarios/View/signup/",
              {"email":self.datosUsuario.email, "username":self.datosUsuario.username, 
              "password":self.datosUsuario.password,"password_confirmation":self.datosUsuario.password_confirmation, 
              "first_name":self.datosUsuario.first_name, "last_name": self.datosUsuario.last_name})

              // alert(JSON.stringify(res))

              Swal.fire({
                icon: 'success',
                title: '¡Registro exitoso!',
                text: 'Tu usuario ha sido creado en Eductech',
                footer: 'Regresa al Login para iniciar sesión'
              })

              this.step--;

              this.$refs.form.reset()
            
          } catch (error) {
            console.log(error)
            Swal.fire({
                icon: 'error',
                title: 'ERROR...',
                text: 'Algo no salio bien',
                footer: 'Intenta de nuevo'
              })
          }

        }
        

        


        // console.log(this.datosUsuario)
      },

      abreTerminosCondiciones: function() {
        console.log("Abre modal")
        // this.dialog: true
      },
      
      abreOlvidoContra: function () {
        console.log("Abre olvide contrasenia")
      },
    }
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand);

  .login-form {
    margin: 0;
    padding: 0;
  }

  .lg {
    background-color: #606366;
    text-align: center;
    color: white;
    font-family: 'Quicksand', sans-serif;
    padding: 0;
    margin: 78px 0;
  }
</style>
