//TODO Web Template Studio: Add a new link in the NavBar for your page here. 
// A skip link is included as an accesibility best practice. For more information visit https://www.w3.org/WAI/WCAG21/Techniques/general/G1. 
<template>
    <div>
        <!-- <div class="skipLink"> -->
        <!--     <a href="/map">Goto the map</a> -->
        <!-- </div> -->
        <div class="navbar navbar-expand-sm navbar-light border-bottom justify-content-between">
            <a class="navbar-brand" href="/map" role="heading" aria-level="1">Map</a>
            <b-nav class="navbar-nav">
                <b-nav-item class="nav-item nav-link active" to="/review/DcBLYSvOuWcNReolRVr12A/Drago's">
                    Chosen store
                </b-nav-item>
                <b-nav-item class="nav-item nav-link active" to="/ind">
                    Industry page
                </b-nav-item>
            </b-nav>
        </div>
    </div>
</template> 
 
<script>
export default {
    name: "NavBar"
}; 
</script> 
 
<style scoped>
.skipLink a {
    position: absolute;
    left: -100px;
    top: -100px;
}

.skipLink a:focus {
    position: fixed;
    z-index: 1000;
    top: 0;
    left: 0;
    padding: 10px;
    color: #ffffff;
    background: #000000;
}
</style> 
