<template>
<v-container fluid>
    <HeaderBlog></HeaderBlog>
    <SingleComponent></SingleComponent>
    <SingleComponent></SingleComponent>
    <RecursoArticulo></RecursoArticulo>
</v-container>
</template>

<script>
import NavBar from './NavBar';
import HeaderBlog from './BlogComponents/HeaderBlog';
import SingleComponent from './BlogComponents/SingleComponent';
import RecursoArticulo from './Recursos/RecursoArticulo';


export default {
    name: "Blog",
    components: {
        NavBar,
        HeaderBlog,
        SingleComponent,
        RecursoArticulo
    },
    methods: {

    }, 
};
</script>

<style scoped>

</style>