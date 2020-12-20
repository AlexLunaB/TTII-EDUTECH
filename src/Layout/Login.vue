<template>
  <v-app>
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
                        <h1 class="text-center display-2 teal--text text--accent-2">
                          EdutechMap

                        </h1>

                        <div class="text-center" mt-4>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-facebook-f</v-icon>

                          </v-btn>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-twitter</v-icon>
                          </v-btn>
                        </div>

                        <h4 class="text-center mlt-4">Logueate</h4>
                        <v-form>
                          <v-text-field
                            label="Correo"
                            name="username"
                            prepend-icon="email"
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
                            color="teal accent-3">
                          </v-text-field>
                        </v-form>

                        <h3 class="text-center mt-3"> ¿Olvidaste tu contraseña?</h3>

                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn rounded color="teal accent-3" @click="loginUser" dark>Inicia Sesión</v-btn>
                      </div>
                    </v-col>


                    <v-col cols="12" md="4" class="teal accent-3">
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
                    <v-col cols="12" md="4" class="teal accent-3">
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
                        <h1 class="text-center display-2 teal--text text--accent-3">Crear Cuenta</h1>
                      <div class="text-center mt-4">
                        <v-btn class="mx-2" fab >
                          <v-icon>fab fa-facebook</v-icon>
                        </v-btn>
                      </div>

                        <div>
                          <h4 class="text-center ">Verifica tu correo</h4>
                          <v-form>
                            <v-text-field
                            label="Nombre"
                            name="Nombre"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3">

                            </v-text-field>
                            <v-text-field
                            label="Correo"
                            name="correo"
                            prepend-icon="email"
                            type="text"
                            color="teal accent-3">

                            </v-text-field><v-text-field
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="text"
                            color="teal accent-3">

                            </v-text-field>
                          </v-form>
                        </div>


                      </v-card-text>
                      <div class="text-center mt-n5">
                          <v-btn color="teal "> Registrate!</v-btn>

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

  export default {
    name: 'login',

    data() {
      return {
        step: 1,
        username: '',
        password: '',
        wrongCred: false // activates appropriate message if set to true
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
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
      }
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
