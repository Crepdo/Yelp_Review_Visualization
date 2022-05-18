<template>
    <!-- <NavBar /> -->
    <!-- <router-view>router view</router-view> -->
    <!-- <Footer /> -->
    <Map class="map"> </Map>
</template>

<script>
/*import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";*/
import Map from "@/views/Map.vue"
export default {
    name: "app",
    components: {
        Map
        /* NavBar,*/
        /* Footer*/
    }
};
</script>

<style>
html {
    position: relative;
    min-height: 100%;
}

body {
    margin-bottom: 160px !important;
    /* Height of the footer */
    padding: 0;
    height: 100%;
    width: 100%;
}

/* Override Bootstrap Styling */

.btn-primary {
    background-color: #025fce !important;
}

.map {
    height: 100%;
}
</style>
