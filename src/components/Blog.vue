<template>
<v-container>
    <h1>BLOG</h1>
    <LastArticles></LastArticles>
</v-container>
</template>

<script>
import NavBar from './NavBar';
import LastArticles from './LastArticles';


export default {
    name: "Blog",
    components: {
        NavBar,
        LastArticles,
    }
};
</script>

<style scoped>

</style>