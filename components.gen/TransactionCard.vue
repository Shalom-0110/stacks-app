<template>
  <div class="flex items-center justify-between p-4 bg-white rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-full flex items-center justify-center text-xl" :style="{ background: categoryColor + '20' }">
        {{ categoryIcon }}
      </div>
      <div>
        <p class="font-semibold text-slate-800 text-sm">{{ transaction.title }}</p>
        <p class="text-xs text-slate-400">{{ transaction.date }}</p>
      </div>
    </div>
    <div class="text-right">
      <p class="font-bold text-slate-800">{{ fmt(transaction.amount) }}</p>
      <p class="text-xs text-slate-400 capitalize">{{ transaction.category }}</p>
    </div>
  </div>
</template>

<script>
import { CATEGORIES } from '@/mockData.js'

export default {
  name: 'TransactionCard',
  props: {
    transaction: { type: Object, required: true },
  },
  computed: {
    category() {
      return CATEGORIES.find(c => c.id === this.transaction.category) || {}
    },
    categoryIcon() { return this.category.icon || '💸' },
    categoryColor() { return this.category.color || '#a78bfa' },
  },
  methods: {
    fmt(n) { return '₹' + new Intl.NumberFormat('en-IN').format(n) },
  },
}
</script>
