<template>
    <div>
        <a href="/map">Back</a>
        <p> hi {{ $route.params.id }} </p>
    </div>
</template>

<script>
export default {
    name: "Review",
    created() {
        this.$watch(
            () => this.$route.params,
        )
    }
}
</script>
