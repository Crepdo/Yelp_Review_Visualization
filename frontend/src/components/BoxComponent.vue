<template>
    <div>
        <svg :width="svgWidth" :height="svgHeight">
            <g ref="star_svg"></g>
        </svg>
    </div>
    <div>

    </div>
</template>

<script>
import * as d3 from "d3";
import * as d3fetch from "d3-fetch";

export default {
    name: "BoxComponent",
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
        d3fetch.json("/api/box/" + this.business_id).then((star_data) => {
            this.draw_box(star_data);
        });
    },
    methods: {
        draw_box(box_data) {
            
        }
    }
}

</script>