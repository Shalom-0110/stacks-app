<template>
  <Loading ref="loader">
  <template #content>
  <div class="p-6 max-w-6xl mx-auto">
    <PageTitle
      title="Budget"
      description="Stay in control, category by category"
      :items="[{ label: 'Budget' }]"
    />

    <!-- Hero Status Card -->
    <div class="relative bg-gradient-to-br from-violet-600 to-fuchsia-600 rounded-2xl p-6 text-white mb-6 overflow-hidden">
      <p class="text-xl font-black">You're on track with 4 of 6 categories 🎯</p>
      <div class="flex gap-6 mt-3 text-sm text-white/80 flex-wrap">
        <span>Total budgeted: ₹25,000</span>
        <span>Spent: ₹11,888</span>
        <span>Remaining: ₹13,112</span>
      </div>
      <p class="absolute right-6 top-1/2 -translate-y-1/2 text-7xl font-black text-white/20 select-none">
        78%
      </p>
    </div>

    <!-- Category Budget Grid -->
    <div class="grid grid-cols-2 gap-4 mb-6">
      <div
        v-for="b in BUDGETS"
        :key="b.category"
        class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5"
      >
        <!-- Top Row -->
        <div class="flex items-center gap-3 mb-3">
          <div
            class="w-9 h-9 rounded-full flex items-center justify-center text-lg flex-shrink-0"
            :style="{ background: catData(b).color + '20' }"
          >
            {{ catData(b).icon }}
          </div>
          <span class="font-semibold text-slate-700 flex-1">{{ catData(b).label }}</span>

          <span
            class="text-xs font-bold px-2 py-0.5 rounded-full"
            :style="{
              color: pctColor(pct(b)),
              background: pctColor(pct(b)) + '15',
            }"
          >
            {{ pct(b) }}%
          </span>

          <button class="text-slate-300 hover:text-slate-500 transition-colors">
            <i class="pi pi-pencil text-sm"></i>
          </button>
        </div>

        <!-- Progress Bar -->
        <ProgressBar
          :value="pct(b)"
          style="height: 8px"
          :class="progClass(pct(b))"
        />

        <div class="flex items-center justify-between mt-2">
          <span class="text-sm text-slate-500">
            {{ fmt(b.spent) }} <span class="text-slate-400">of {{ fmt(b.limit) }}</span>
          </span>
          <span class="text-xs text-slate-400">9 days left</span>
        </div>

        <div
          v-if="pct(b) >= 85"
          class="bg-rose-50 text-rose-600 text-xs rounded-lg px-3 py-2 mt-2 flex items-center gap-1"
        >
          <span>⚠️</span>
          <span>Almost at your limit</span>
        </div>
      </div>

      <!-- Add category card -->
      <div
        class="border-2 border-dashed border-slate-200 rounded-2xl p-6 text-center cursor-pointer hover:border-violet-300 hover:bg-violet-50 transition-colors flex flex-col items-center justify-center gap-2"
      >
        <i class="pi pi-plus text-2xl text-slate-300"></i>
        <p class="text-sm text-slate-400">Set a new budget category</p>
      </div>
    </div>

    <!-- Tips Card -->
    <div class="bg-amber-50 border border-amber-200 rounded-2xl p-5">
      <p class="font-bold text-amber-800 mb-2">💡 Budget tip of the day</p>
      <p class="text-sm text-amber-700">
        The 50/30/20 rule: 50% needs, 30% wants, 20% savings.
        Your current split: 68% / 20% / 12%.
      </p>
    </div>
  </div>
  </template>
  </Loading>
</template>

<script>
import { BUDGETS, CAT_MAP } from '@/mockData.js'

export default {
  name: 'BudgetView',

  data() {
    return {
      BUDGETS,
    }
  },

  mounted() {
    this.$refs.loader.complete()
  },

  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },

    catData(b) {
      return CAT_MAP[b.category] || { icon: '💸', label: b.category, color: '#a78bfa' }
    },

    pct(b) {
      return Math.round((b.spent / b.limit) * 100)
    },

    pctColor(pct) {
      return pct >= 85 ? '#ef4444' : pct >= 65 ? '#f59e0b' : '#7c3aed'
    },

    progClass(pct) {
      return pct >= 85 ? 'prog-danger' : pct >= 65 ? 'prog-warn' : 'prog-ok'
    },
  },
}
</script>

<style scoped>
.prog-ok :deep(.p-progressbar-value) {
  background: #7c3aed;
}

.prog-warn :deep(.p-progressbar-value) {
  background: #f59e0b;
}

.prog-danger :deep(.p-progressbar-value) {
  background: #ef4444;
}
</style>
