<template>
  <div class="bg-white rounded-2xl border p-4 flex flex-col gap-3 transition-all"
    :class="isOver ? 'border-red-200' : isWarning ? 'border-amber-200' : 'border-slate-100 shadow-sm'">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-xl">{{ categoryIcon }}</span>
        <span class="font-medium text-slate-700 text-sm capitalize">{{ budget.category }}</span>
      </div>
      <span class="text-xs font-semibold"
        :class="isOver ? 'text-red-600' : isWarning ? 'text-amber-600' : 'text-slate-400'">
        {{ pct }}%
      </span>
    </div>

    <div>
      <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
        <div
          class="h-1.5 rounded-full transition-all"
          :style="{ width: Math.min(100, pct) + '%' }"
          :class="isOver ? 'bg-red-500' : isWarning ? 'bg-amber-400' : 'bg-violet-500'"/>
      </div>
      <div class="flex justify-between mt-1.5 text-xs text-slate-400">
        <span>{{ fmt(budget.spent) }} spent</span>
        <span>{{ fmt(budget.limit) }} limit</span>
      </div>
    </div>

    <p v-if="isOver" class="text-xs text-red-500 font-medium">Over limit by {{ fmt(budget.spent - budget.limit) }}</p>
    <p v-else-if="isWarning" class="text-xs text-amber-500 font-medium">Approaching limit</p>
  </div>
</template>

<script>
import { CATEGORIES } from '@/mockData.js'

export default {
  name: 'BudgetCategoryCard',
  props: {
    budget: { type: Object, required: true },
  },
  computed: {
    pct() { return Math.round((this.budget.spent / this.budget.limit) * 100) },
    isOver() { return this.pct > 100 },
    isWarning() { return this.pct >= 85 && this.pct <= 100 },
    categoryIcon() {
      return CATEGORIES.find(c => c.id === this.budget.category)?.icon || '💸'
    },
  },
  methods: {
    fmt(n) { return '₹' + new Intl.NumberFormat('en-IN').format(n) },
  },
}
</script>
