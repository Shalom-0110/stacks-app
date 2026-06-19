<template>
  <Loading ref="loader">
  <template #content>
  <div class="p-6 max-w-6xl mx-auto">
    <PageTitle
      title="Goals"
      description="Dream it. Save it. Get it."
      :items="[{ label: 'Goals' }]"
    />

    <!-- Summary Pills -->
    <div class="flex gap-3 mb-6 flex-wrap">
      <span class="bg-slate-100 text-slate-600 rounded-full px-4 py-1.5 text-sm font-semibold">
        4 Goals
      </span>
      <span class="bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-full px-4 py-1.5 text-sm font-semibold">
        1 Completed ✅
      </span>
      <span class="bg-violet-50 text-violet-700 border border-violet-200 rounded-full px-4 py-1.5 text-sm font-semibold">
        ₹2,77,000 target total
      </span>
    </div>

    <!-- Goals Grid -->
    <div class="grid grid-cols-2 gap-6">
      <div
        v-for="g in GOALS"
        :key="g.id"
        class="bg-white rounded-3xl border border-slate-100 shadow-sm p-6"
        :class="g.saved >= g.target ? 'border-emerald-200 bg-emerald-50' : ''"
      >
        <!-- Top Row -->
        <div class="flex items-start justify-between mb-4">
          <div>
            <p class="text-4xl">{{ g.emoji }}</p>
            <p class="text-xl font-black text-slate-800 mt-1">{{ g.title }}</p>
          </div>
          <div>
            <span
              v-if="g.saved >= g.target"
              class="bg-emerald-100 text-emerald-700 text-xs font-bold px-3 py-1 rounded-full"
            >
              ✅ Reached!
            </span>
            <span
              v-else-if="g.deadline"
              class="text-xs font-bold px-3 py-1 rounded-full"
              :class="daysLeft(g.deadline) !== null && daysLeft(g.deadline) < 30
                ? 'bg-amber-100 text-amber-700'
                : 'bg-slate-100 text-slate-500'"
            >
              {{ daysLeftLabel(g.deadline) }}
            </span>
          </div>
        </div>

        <!-- SVG Circle Progress -->
        <div class="flex justify-center mb-4">
          <svg width="120" height="120" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="none" stroke="#e5e7eb" stroke-width="8" />
            <circle
              cx="50"
              cy="50"
              r="40"
              fill="none"
              :stroke="g.color"
              stroke-width="8"
              stroke-linecap="round"
              stroke-dasharray="251.2"
              :stroke-dashoffset="circumference - (goalPct(g) / 100) * circumference"
              transform="rotate(-90 50 50)"
            />
            <text
              x="50"
              y="50"
              dominant-baseline="middle"
              text-anchor="middle"
              font-weight="bold"
              font-size="18"
              :fill="g.color"
            >
              {{ goalPct(g) }}%
            </text>
          </svg>
        </div>

        <!-- Amounts -->
        <div class="text-center mb-4">
          <p>
            <span class="font-bold text-slate-800">{{ fmt(g.saved) }} saved</span>
            <span class="text-slate-400"> of {{ fmt(g.target) }}</span>
          </p>
          <p v-if="g.saved < g.target" class="text-sm text-slate-400 mt-1">
            {{ fmt(g.target - g.saved) }} more to go
          </p>
          <p v-else class="text-sm font-bold text-emerald-600 mt-1">
            You nailed it! 🔥
          </p>
        </div>

        <!-- Progress Bar -->
        <ProgressBar
          :value="goalPct(g)"
          style="height: 8px"
          :pt="{ value: { style: 'background:' + g.color } }"
        />
      </div>
    </div>

    <!-- V2 Teaser -->
    <div class="mt-6 border border-dashed border-slate-200 rounded-2xl p-6 text-center">
      <p class="text-sm text-slate-400">
        🤖 Auto contributions and smart reminders, coming in V2
      </p>
    </div>
  </div>
  </template>
  </Loading>
</template>

<script>
import { GOALS } from '@/mockData.js'

export default {
  name: 'GoalsView',

  data() {
    return {
      GOALS,
      circumference: 251.2,
    }
  },

  mounted() {
    this.$refs.loader.complete()
  },

  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },

    goalPct(g) {
      return Math.min(Math.round((g.saved / g.target) * 100), 100)
    },

    daysLeft(deadline) {
      if (!deadline) return null
      const today = new Date('2024-11-21')
      const end = new Date(deadline)
      const diff = Math.ceil((end - today) / (1000 * 60 * 60 * 24))
      return diff
    },

    daysLeftLabel(deadline) {
      if (!deadline) return 'No deadline'
      const days = this.daysLeft(deadline)
      if (days <= 0) return '✅ Reached!'
      return days + ' days left'
    },
  },
}
</script>
