<template>
<v-app>
    <NavBar/>
    <v-main>
        <v-container>
            <h1 class="subheader">Página no encontrada</h1>
            <h2>LA página que biscas no existe</h2>
            <h3>
                Intenta ir a
                <router-link :to="{path: '/Inicio' }">Inicio</router-link>
            </h3>
        </v-container>
    </v-main>
</v-app>

</template>

<script>
import NavBar from './NavBar';

export default {
    name: 'ErrorComponent',
    components: {
        NavBar
    }
}
</script>

<style scoped>

</style>