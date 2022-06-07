<template>
    <div>
        <svg :width="svgWidth" :height="svgHeight">
            <g ref="star_svg"></g>
        </svg>
    </div>
</template>

<script>
import * as d3 from "d3";
import * as d3fetch from "d3-fetch";
import { nest } from 'd3-collection';
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
        d3fetch.json("/api/review/" + this.business_id).then((star_data) => {
            this.draw_box(star_data);
        });
    },
    methods: {
        draw_box(data) {
            var svg = d3
                .select(this.$refs.star_svg)
                .attr(
                    "transform",
                    "translate(" + this.svgMargin.left + "," + this.svgMargin.top + ")"
                );
            var sumstat = nest() // nest function allows to group the calculation per level of a factor
                .key(function (d) { return d.date; })
                .rollup(function (d) {
                    var q1 = d3.quantile(d.map(function (g) { return g.stars; }).sort(d3.ascending), .25)
                    var median = d3.quantile(d.map(function (g) { return g.Sepal_Length; }).sort(d3.ascending), .5)
                    var q3 = d3.quantile(d.map(function (g) { return g.stars; }).sort(d3.ascending), .75)
                    var interQuantileRange = q3 - q1
                    var min = q1 - 1.5 * interQuantileRange
                    var max = q3 + 1.5 * interQuantileRange
                    return ({ q1: q1, median: median, q3: q3, interQuantileRange: interQuantileRange, min: min, max: max })
                })
                .entries(data)
            // Show the X scale
            const x = d3
                .scaleTime()
                .domain(d3.extent(data, (d) => d3.timeParse("%Y-%m-%d")(d.month)))
                .range([0, this.gWidth]);
            svg
                .append("g")
                .attr("transform", "translate(0," + this.gHeight + ")")
                .call(d3.axisBottom(x))
                .selectAll("text")
                .style("text-anchor", "end")
                .style("font-size", "75%")
                .attr("dx", "-.8em")
                .attr("dy", ".15em")
                .attr("transform", function (d) {
                    return "rotate(-45)";
                })
                ;
            // Show the Y scale
            var y = d3.scaleLinear()
                .domain([0, 5])
                .range([this.gHeight, 0])
            svg.append("g").call(d3.axisLeft(y))

            // Show the main vertical line
            svg
                .selectAll("vertLines")
                .data(sumstat)
                .enter()
                .append("line")
                .attr("x1", function (d) { return (x(d.key)) })
                .attr("x2", function (d) { return (x(d.key)) })
                .attr("y1", function (d) { return (y(d.value.min)) })
                .attr("y2", function (d) { return (y(d.value.max)) })
                .attr("stroke", "black")
                .style("width", 10)
            // rectangle for the main box
            var boxWidth = 30
            svg
                .selectAll("boxes")
                .data(sumstat)
                .enter()
                .append("rect")
                .attr("x", function (d) { return (x(d.key) - boxWidth / 2) })
                .attr("y", function (d) { return (y(d.value.q3)) })
                .attr("height", function (d) { return (y(d.value.q1) - y(d.value.q3)) })
                .attr("width", boxWidth)
                .attr("stroke", "black")
                .style("fill", "#69b3a2")
            // Show the median
            svg
                .selectAll("medianLines")
                .data(sumstat)
                .enter()
                .append("line")
                .attr("x1", function (d) { return (x(d.key) - boxWidth / 2) })
                .attr("x2", function (d) { return (x(d.key) + boxWidth / 2) })
                .attr("y1", function (d) { return (y(d.value.median)) })
                .attr("y2", function (d) { return (y(d.value.median)) })
                .attr("stroke", "black")
                .style("width", 20)
            // Add individual points with jitter
            var jitterWidth = 5
            svg
                .selectAll("indPoints")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", function (d) { return (x(d.Species) - jitterWidth / 2 + Math.random() * jitterWidth) })
                .attr("cy", function (d) { return (y(d.Sepal_Length)) })
                .attr("r", 4)
                .style("fill", "white")
                .attr("stroke", "black")
        }
    }
}

</script>
