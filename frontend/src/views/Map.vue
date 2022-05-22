<template>
    <div>
        <!-- <img class="mb-3" src="@/assets/GreyBox.svg" alt="Default Grey Box" /> -->
        <div ref="map" style="width:100%; height:100%"></div>
        <div ref="popup" class="ol-popup">
            <a href="#" ref="popupcloser" class="ol-popup-closer"></a>
            <div ref="popupcontent"></div>
        </div>
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
import Overlay from 'ol/Overlay';
import { toLonLat } from 'ol/proj';
import { toStringHDMS } from 'ol/coordinate';

export default {
    name: "Map",

    components: {},
    props: {},

    mounted() {
        this.createMap();
    },

    methods: {
        createMap() {
            const container = this.$refs.popup;
            const closer = this.$refs.popupcloser;
            const content = this.$refs.popupcontent;
            var overlay = new Overlay({
                element: container,
                autoPan: {
                    animation: { duration: 250 }
                }
            });
            closer.onclick = function () {
                overlay.setPosition(undefined);
                closer.blur();
                return false;
            };
            var map = new Map({
                target: this.$refs['map'],
                layers: [new TileLayer({ source: new OSM() })],
                view: new View({
                    zoom: 14,
                    center: fromLonLat([-90.091533, 29.951065]),
                    constrainResolution: true
                }),
                overlays: [overlay],
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
            map.on('click', function (evt) {
                if (map.forEachFeatureAtPixel(evt.pixel,
                    function (feat) {
                        return feat === feature;
                    })
                ) {
                    alert('click');
                    const coordinate = evt.coordinate;
                    const hdms = toStringHDMS(toLonLat(coordinate));

                    content.innerHTML = '<p>You clicked here:</p><code>' + hdms + '</code>';
                    overlay.setPosition(coordinate);
                }
            });
        },
    }
};
</script>

<style>
.ol-popup {
    position: absolute;
    background-color: white;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #cccccc;
    bottom: 12px;
    left: -50px;
    min-width: 280px;
}

.ol-popup:after,
.ol-popup:before {
    top: 100%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
}

.ol-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
}

.ol-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
}

.ol-popup-closer {
    text-decoration: none;
    position: absolute;
    top: 2px;
    right: 8px;
}

.ol-popup-closer:after {
    content: "✖";
}
</style>
