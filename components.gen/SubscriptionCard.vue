<template>
  <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col gap-3">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-slate-100 flex items-center justify-center text-xl">
          {{ sub.icon || '📱' }}
        </div>
        <div>
          <p class="font-semibold text-slate-800 text-sm">{{ sub.name }}</p>
          <p class="text-xs text-slate-400">Renews {{ sub.renewalDate }}</p>
        </div>
      </div>
      <div class="text-right">
        <p class="font-bold text-slate-800">{{ fmt(sub.amount) }}</p>
        <p class="text-xs text-slate-400">/month</p>
      </div>
    </div>
    <div
      v-if="daysLeft <= 7"
      class="flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-full w-fit"
      :class="daysLeft <= 3 ? 'bg-red-50 text-red-600' : 'bg-amber-50 text-amber-600'">
      <i class="pi pi-clock text-xs"></i>
      Renews in {{ daysLeft }} day{{ daysLeft !== 1 ? 's' : '' }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SubscriptionCard',
  props: {
    sub: { type: Object, required: true },
  },
  computed: {
    daysLeft() {
      const diff = new Date(this.sub.renewalDate) - new Date()
      return Math.ceil(diff / (1000 * 60 * 60 * 24))
    },
  },
  methods: {
    fmt(n) { return '₹' + new Intl.NumberFormat('en-IN').format(n) },
  },
}
</script>
