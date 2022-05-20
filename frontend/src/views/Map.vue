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
import Circle from 'ol/geom/Circle';
import Feature from "ol/Feature";
import { Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource } from "ol/source";
import { Style, Fill, Stroke, Text } from "ol/style";

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
                    zoom: 14,
                    center: fromLonLat([-90.091533, 29.951065]),
                    constrainResolution: true
                }),
            });
            var feature = new Feature({
                geometry: new Circle([-90.091533, 29.951065], 0.002).transform('EPSG:4326', "EPSG:3857"),
                name: "A mark",
            });
            var style = new Style({
            fill: new Fill({ //⽮量图层填充颜⾊，以及透明度
                color: 'rgba(255, 0, 0, 0.6)'
            }),
            stroke: new Stroke({ //边界样式
                color: '#319FD3',
                width: 5
            }),
            text: new Text({ //⽂本样式
                font: '12px Calibri,sans-serif',
                fill: new Fill({
                color: '#000'
                }),
                stroke: new Stroke({
                color: '#fff',
                width: 3
                })
            })
            });
            feature.setStyle([style]);
            var v_source = new VectorSource({
                features: [feature]
            });
            var vectorLayer = new VectorLayer({
                source: v_source
            });
            map.addLayer(vectorLayer);
            map.on('click', function(evt) {
                if (map.forEachFeatureAtPixel(evt.pixel,
                    function(feat) {
                        return feat === feature;
                    })
                ) {
                    alert('click');
                }
            });
        },
    }
};
</script>

