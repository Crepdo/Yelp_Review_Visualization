<template>
    <div ref="map" style="width:100%; height:100%"></div>
</template>

<script>
import View from "ol/View";
import Map from "ol/Map";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { fromLonLat } from "ol/proj.js";
import "ol/ol.css";

export default {
    name: "Map",

    components: {},
    props: {},

    mounted() {
        this.createMap();
    },

    methods: {
        createMap() {
            new Map({
                target: this.$refs['map'],
                layers: [
                    new TileLayer({
                        source: new OSM()
                    }),
                ],
                view: new View({
                    zoom: 5,
                    center: fromLonLat([120, 30]),
                    constrainResolution: true
                }),
            })
        },
    }
};
</script>

