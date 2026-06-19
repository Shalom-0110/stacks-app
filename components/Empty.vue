<template>
  <div
    class="flex items-center border-neutral-200 border-1 border-solid rounded-sm"
    :class="shadeClass()">
    <i
      style="font-size: 2rem;"
      class="mr-4"
      :class="icon"/>
    <div>
      <h4 class="fw-bold text-uppercase text-lg mb-1">
        {{ title }}
      </h4>
      <div>
        <div
          class="small"
          v-html="text"/>
        <slot name="extra"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Empty",
  props: {
    kind: {
      type: String,
      required: false,
      default: () => null
    },
    icon: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
  },
  methods: {
    shadeClass() {
      if (this.kind && this.kind.length) {
        return `alert alert-${this.kind} p-4`;
      }

      return "alert alert-secondary p-4";
    },
  }
};
</script>
