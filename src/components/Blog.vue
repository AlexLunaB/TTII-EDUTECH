<template>
<v-container fluid>
    <HeaderBlog></HeaderBlog>
    <SingleComponent></SingleComponent>
    <SingleComponent></SingleComponent>
</v-container>
</template>

<script>
import NavBar from './NavBar';
import HeaderBlog from './BlogComponents/HeaderBlog';
import SingleComponent from './BlogComponents/SingleComponent';

export default {
    name: "Blog",
    components: {
        NavBar,
        HeaderBlog,
        SingleComponent
    }
};
</script>

<style scoped>

</style>