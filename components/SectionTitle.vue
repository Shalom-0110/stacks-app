<template>
  <div
    class="section-title"
    :class="{'mb-6': hasMarginBottom}">
    <h6 class="font-bold uppercase mb-1">
      {{ title }}
    </h6>
    <p class="text-gray-400 text-sm">
      {{ description }}
    </p>
  </div>
</template>

<script>
export default {
  name: "SectionTitle",
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true,
    },
    hasMarginBottom: {
      type: Boolean,
      required: false,
      default: () => true
    },
  }
};
</script>
