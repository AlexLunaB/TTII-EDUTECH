<template>
    <!-- <div id="inicio">
        <HeaderComponent></HeaderComponent>
        <Slider></Slider>
        <div class="center">
            <router-view></router-view>
            <Sidebar></Sidebar>
            <div class="clearfix"></div>
        </div>
        <FooterComponent></FooterComponent>
    </div> -->
    <div id="inicio" >
        <NavegacionBar></NavegacionBar>


        <!-- <FooterComponent></FooterComponent> -->
    </div>
</template>

<script>
import HeaderComponent from './HeaderComponent';
import Slider from './Slider';
import Sidebar from './Sidebar';
import FooterComponent from './FooterComponent';
import NavBar from './NavBar';


export default {
    name: "app",
    components: {
        HeaderComponent,
        Slider,
        Sidebar,
        FooterComponent,
        NavBar,
    }
};
</script>

<style>
    @import '../assets/css/styles.css';
</style>