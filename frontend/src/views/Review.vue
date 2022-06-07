<template>
    <div>
        <a href="/map">Back</a>
        <p>hi {{ $route.params.name }}</p>
        <p>hi {{ $route.params.id }}</p>
        <div id="star_container" class="svg-container" style="width: 50%">
            <StarComponent :business_id="business_id" :svgWidth="svgWidth" />
        </div>
        <div id="star_container" class="svg-container" style="width: 50%">
            <BoxComponent :business_id="business_id" :svgWidth="svgWidth" />
        </div>
        <div id="stream_container" class="svg-container" style="width: 100%">
            <WordstreamComponent :business_id="business_id" :svgWidth="streamWidth" />
        </div>
    </div>
</template>

<script>
import StarComponent from "@/components/StarComponent";
import WordstreamComponent from "@/components/WordstreamComponent";
import BoxComponent from "@/components/BoxComponent";
export default {
    name: "Review",
    components: {
        StarComponent,
        WordstreamComponent,
        BoxComponent,
    },
    computed: {
        business_id() {
            return this.$route.params.id;
        },
    },
    data: () => ({
        svgWidth: 0,
        streamWidth: 0,
        svgMargin: { top: 10, right: 30, bottom: 30, left: 60 },
    }),
    created() {
        this.$watch(() => this.$route.params);
    },
    mounted() {
        this.svgWidth = document.getElementById("star_container").offsetWidth * 0.75;
        this.streamWidth = document.getElementById("stream_container").offsetWidth * 0.95;
    },

    methods: {}
};
</script>
