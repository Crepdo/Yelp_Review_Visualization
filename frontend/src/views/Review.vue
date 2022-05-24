<template>
    <div>
        <a href="/map">Back</a>
        <p> hi {{ $route.params.id }} </p>
        <div id="container" class="svg-container" align="center" style="width: 30%">
            <svg :width="svgWidth" :height="svgHeight">
                <g ref="star_svg">
                </g>
            </svg>
        </div>
    </div>
</template>

<script>
import * as d3 from "d3";
export default {
    name: "Review",
    computed: {
        business_id() {
            return this.$route.params.id
        },
        svgHeight() {
            return this.svgWidth / 1.61803398875;
        }
    },
    data: () => ({
        svgWidth: 0,
    }),
    created() {
        this.$watch(
            () => this.$route.params,
        );
    },
    mounted() {
        this.svgWidth = document.getElementById("container").offsetWidth * 0.75;
        this.fetch_stars(this.$route.params.id).then((star_data) => { this.draw_star(star_data) });
    },

    methods: {
        async fetch_stars(id) {
            return fetch("/api/star/" + id)
                .then((response) => {
                    if (!response.ok) {
                        throw Error(response.statusText);
                    }
                    return response.json();
                })
        },
        draw_star(star_data) {
            var svg = d3.select(this.$refs.star_svg);
            console.log(star_data);
            for (var i = 0; i < star_data.length; i++) {
                console.log(star_data[i]);
                console.log(star_data[i].month);
                console.log(star_data[i].star);

            }
            console.log(d3.extent(star_data, d => d.month));
            const x = d3.scaleTime()
                .domain(d3.extent(star_data, d => d3.timeParse("%Y-%m-%d")(d.month)))
                .range([0, this.svgWidth]);
            svg.append("g")
                .attr("transform", "translate(0," + this.svgHeight + ")")
                .call(d3.axisBottom(x));
            const y = d3.scaleLinear()
                .domain([0, 5])
                .range([this.svgHeight, 0]);
            svg.append("g")
                .call(d3.axisLeft(y));
            svg.append("path")
                .datum(star_data)
                .attr("fill", "none")
                .attr("stroke", "#69b3a2")
                .attr("stroke-width", 1.5)
                .attr("d", d3.line()
                    .x(d => x(d3.timeParse("%Y-%m-%d")(d.month)))
                    .y(d => y(d.star))
                );
            svg
                .append("g")
                .selectAll("dot")
                .data(star_data)
                .join("circle")
                .attr("cx", d => x(d3.timeParse("%Y-%m-%d")(d.month)))
                .attr("cy", d => y(d.star))
                .attr("r", 5)
                .attr("fill", "#69b3a2");
        }
    }
}
</script>
