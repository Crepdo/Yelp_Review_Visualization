<template>
    <div>
        <!-- <img class="mb-3" src="@/assets/GreyBox.svg" alt="Default Grey Box" /> -->
        <div ref="map" style="width:100%; height:100%"></div>
    </div>
</template>

<script>
import View from "ol/View";
import Map from "ol/Map";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { fromLonLat } from "ol/proj";
import "ol/ol.css";
import Point from "ol/geom/Point";
import Feature from "ol/Feature";
import { Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource } from "ol/source";
import { Style, Icon } from "ol/style"

export default {
    name: "Map",

    components: {},
    props: {},

    mounted() {
        this.createMap();
    },

    methods: {
        createMap() {
            var map = new Map({
                target: this.$refs['map'],
                layers: [new TileLayer({ source: new OSM() })],
                view: new View({
                    zoom: 5,
                    center: fromLonLat([120, 30]),
                    constrainResolution: true
                }),
            });
            var viewProjection = map.getView().getProjection();
            var feature = new Feature({
                geometry: new Point([120, 30.03]).transform('EPSG:4326', viewProjection),
                name: "A mark"
            });
            feature.setStyle([
                new Style({
                    image: new Icon({
                        anchor: [0.5, 1],
                        size: [32, 32],
                        src: require("../assets/地图.svg")
                    })
                })
            ]);
            var v_source = new VectorSource({
                features: [feature]
            });
            var vectorLayer = new VectorLayer({
                source: v_source
            });
            map.addLayer(vectorLayer);
        },
    }
};
</script>

