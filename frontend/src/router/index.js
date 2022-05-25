import Vue from "vue";
import VueRouter from "vue-router";

import Grid from "@/views/Grid.vue";
import Map from "@/views/Map.vue";
import Review from "@/views/Review.vue";
Vue.use(VueRouter);

// TODO Web Template Studio: Add routes for your new pages here.
export default new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: Grid },
        { path: "/map", component: Map },
        { path: "/review/:id/:name", sensitive: false, component: Review },
    ]
});
