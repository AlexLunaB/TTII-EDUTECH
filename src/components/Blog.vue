<template>
<v-container fluid>
    <HeaderBlog></HeaderBlog>
    <v-btn
        block
        elevation="2"
        color = "primary"
        @click="handleStateClick"
    >
        ¿Agregar recurso? Click aqui
    </v-btn>
    <SingleComponent></SingleComponent>
    <SingleComponent></SingleComponent>
    <!-- <div v-if="visible">

        <RecursoArticulo></RecursoArticulo>
        
    </div> -->

    <RecursoArticulo ref="addResource"></RecursoArticulo>
    
</v-container>
</template>

<script>
import NavBar from './NavBar';
import HeaderBlog from './BlogComponents/HeaderBlog';
import SingleComponent from './BlogComponents/SingleComponent';
import RecursoArticulo from './Recursos/RecursoArticulo';


export default {
    name: "Blog",
    data() {
        return {
            visible: false
        }
    },
    components: {
        NavBar,
        HeaderBlog,
        SingleComponent,
        RecursoArticulo
    },
    methods: {
        handleStateClick: function () {

            this.$refs.addResource.showAddResource();
        }, 
    }
};
</script>

<style scoped>

</style>