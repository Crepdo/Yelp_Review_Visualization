<template>
    <svg :width="svgWidth" :height="svgHeight">
        <g ref="star_svg"></g>
    </svg>
</template>

<script>
// import * as d3 from "d3";
import * as d3fetch from "d3-fetch";
export default {
    name: "StarComponent",
    props: {
        business_id: {
            type: String,
            required: true
        },
        svgWidth: {
            type: Number,
            required: true
        },
    },
    computed: {
        svgHeight() {
            return this.svgWidth / 1.61803398875;
        },
        gWidth() {
            return this.svgWidth - this.svgMargin.left - this.svgMargin.right;
        },
        gHeight() {
            return this.svgHeight - this.svgMargin.top - this.svgMargin.bottom;
        },
    },
    data: () => ({
        svgMargin: { top: 10, right: 30, bottom: 30, left: 60 },
    }),
    mounted() {
        d3fetch.json("/api/stream/" + this.business_id).then((words_data) => {
            this.draw_stream(words_data);
        });
    },
    methods: {
        draw_stream(words_data) {
            console.log(words_data);
        },
    },
};
</script>
