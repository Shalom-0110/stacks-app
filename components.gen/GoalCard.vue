<template>
  <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col gap-3">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-2xl">{{ goal.emoji }}</span>
        <span class="font-semibold text-slate-800 text-sm">{{ goal.title }}</span>
      </div>
      <span v-if="isReached" class="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Reached!</span>
    </div>

    <!-- Circular progress -->
    <div class="flex items-center gap-4">
      <svg class="w-14 h-14 flex-shrink-0" viewBox="0 0 36 36">
        <path class="text-slate-100" stroke="currentColor" stroke-width="3" fill="none"
          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>
        <path :stroke="goal.color || '#7c3aed'" stroke-width="3" fill="none" stroke-linecap="round"
          :stroke-dasharray="`${pct}, 100`"
          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>
        <text x="18" y="20.35" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="bold">{{ pct }}%</text>
      </svg>
      <div class="text-sm space-y-1">
        <div class="text-slate-400">Saved <span class="font-bold text-slate-700">{{ fmt(goal.saved) }}</span></div>
        <div class="text-slate-400">Target <span class="font-bold text-slate-700">{{ fmt(goal.target) }}</span></div>
        <div v-if="!isReached" class="text-slate-400">Need <span class="font-semibold text-violet-600">{{ fmt(goal.target - goal.saved) }}</span></div>
      </div>
    </div>

    <div v-if="goal.deadline" class="text-xs text-slate-400 border-t border-slate-50 pt-2">
      <i class="pi pi-calendar text-xs mr-1"></i>{{ goal.deadline }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'GoalCard',
  props: {
    goal: { type: Object, required: true },
  },
  computed: {
    pct() { return Math.min(100, Math.round((this.goal.saved / this.goal.target) * 100)) },
    isReached() { return this.goal.saved >= this.goal.target },
  },
  methods: {
    fmt(n) { return '₹' + new Intl.NumberFormat('en-IN').format(n) },
  },
}
</script>
