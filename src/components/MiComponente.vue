<template>
    <section id="content">
    <h2 class="subheader">{{ titulo }}</h2>
        <hr/>
            <h1>Este es MI COMPONENTE</h1>
            <h2> {{subtitulo}} </h2>
        <hr/>
    </section>
</template>

<script>
export default {
    name: 'MiComponente',
    data(){
        return{
            titulo: 'Mi Componente',
            subtitulo: 'Soy el subtitutlo de mi compoente'
        }
    }
}
</script>