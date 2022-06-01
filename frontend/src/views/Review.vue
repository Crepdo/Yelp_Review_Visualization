<template>
    <div>
        <a href="/map">Back</a>
        <p>hi {{ $route.params.name }}</p>
        <p>hi {{ $route.params.id }}</p>
        <div id="container" class="svg-container" style="width: 50%">
            <StarComponent :business_id="business_id" :svgWidth="svgWidth" />
        </div>
        <div id="container" class="svg-container" style="width: 50%">
            <WordstreamComponent :business_id="business_id" :svgWidth="svgWidth" />
        </div>
    </div>
</template>

<script>
import StarComponent from "@/components/StarComponent";
import WordstreamComponent from "@/components/WordstreamComponent";
export default {
    name: "Review",
    components: {
        StarComponent,
        WordstreamComponent,
    },
    computed: {
        business_id() {
            return this.$route.params.id;
        },
    },
    data: () => ({
        svgWidth: 0,
        svgMargin: { top: 10, right: 30, bottom: 30, left: 60 },
    }),
    created() {
        this.$watch(() => this.$route.params);
    },
    mounted() {
        this.svgWidth = document.getElementById("container").offsetWidth * 0.75;
    },

    methods: {}
};
</script>
