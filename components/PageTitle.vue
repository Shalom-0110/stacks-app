<template>
  <div class="mb-10">
    <Breadcrumb
      class="text-sm pb-2!"
      :home="{label: 'Home', icon: 'pi pi-home', route: {name: 'home'}}"
      :model="items">
      <template #item="{ item, props }">
        <router-link
          v-if="item.route"
          :to="item.route">
          <span
            v-if="item.icon"
            :class="[item.icon, 'text-primary', 'mr-2']"/>
          <span class="text-primary font-semibold">{{ item.label }}</span>
        </router-link>
        <a
          v-else-if="item.url"
          :href="item.url"
          :target="item.target"
          v-bind="props.action">
          <span
            v-if="item.icon"
            :class="[item.icon, 'text-slate-400', 'mr-2']"/>
          <span class="text-slate-400">{{ item.label }}</span>
        </a>
        <span
          v-else
          class="text-slate-400">
          <span
            v-if="item.icon"
            :class="[item.icon, 'text-slate-400', 'mr-2']"/>
          {{ item.label }}
        </span>
      </template>
    </Breadcrumb>
    <div class="flex justify-between mb-6">
      <div>
        <h1 class="text-3xl">
          {{ title }}
        </h1>
        <p
          v-if="description"
          class="text-sm text-slate-500 pt-2">
          {{ description }}
        </p>
      </div>
      <div v-if="actionTo">
        <router-link :to="actionTo">
          <Button
            :label="actionLabel"
            :icon="actionIcon"/>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageTitle",
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: false,
      default: () => null,
    },
    items: {
      type: Array,
      required: true,
    },
    actionTo: {
      type: Object,
      required: false,
      default: () => null,
    },
    actionLabel: {
      type: String,
      required: false,
      default: () => null,
    },
    actionIcon: {
      type: String,
      required: false,
      default: () => null,
    },
  },
};
</script>
