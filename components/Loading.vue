<template>
  <div>
    <div
      v-if="isLoading"
      class="text-center">
      <ProgressSpinner
        style="width: 50px; height: 50px"
        stroke-width="4"
        fill="transparent"
        animation-duration=".5s"
        aria-label="Custom ProgressSpinner"/>
    </div>
    <slot
      v-else
      name="content"/>
  </div>
</template>

<script>
export default {
  name: "Loading",
  data() {
    return {
      isLoading: true,
    };
  },
  methods: {
    complete() {
      this.isLoading = false;
    },
    start() {
      this.isLoading = true;
    },
  },
};
</script>
