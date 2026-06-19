<template>
  <div>
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-slate-800">Wishlist</h1>
        <p class="text-slate-500 text-sm mt-1">Things you are saving up for.</p>
      </div>
      <router-link
        to="/wishlist/add"
        class="inline-flex items-center gap-2 bg-violet-600 hover:bg-violet-700 text-white text-sm font-semibold px-4 py-2 rounded-xl transition-colors no-underline">
        <i class="pi pi-plus text-xs"></i>
        Add Item
      </router-link>
    </div>

    <!-- Stat Pills -->
    <div class="flex items-center gap-3 mb-6 flex-wrap">
      <div class="inline-flex items-center gap-2 bg-violet-50 border border-violet-200 rounded-full px-4 py-1.5 text-sm text-violet-700 font-medium">
        <i class="pi pi-bookmark text-violet-500 text-xs"></i>
        Saving: <span class="font-bold">{{ savingCount }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 rounded-full px-4 py-1.5 text-sm text-emerald-700 font-medium">
        <i class="pi pi-check-circle text-emerald-500 text-xs"></i>
        Reached: <span class="font-bold">{{ reachedCount }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-amber-50 border border-amber-200 rounded-full px-4 py-1.5 text-sm text-amber-700 font-medium">
        <i class="pi pi-pause-circle text-amber-500 text-xs"></i>
        Paused: <span class="font-bold">{{ pausedCount }}</span>
      </div>
    </div>

    <!-- Search -->
    <div class="mb-6">
      <InputText
        v-model="search"
        placeholder="Search wishlist..."
        class="w-64"
      />
    </div>

    <!-- Wishlist Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <div
        v-for="item in filteredItems"
        :key="item.id"
        class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col gap-3 hover:shadow-md transition-shadow">

        <!-- Top Row -->
        <div class="flex items-start justify-between gap-2">
          <div class="flex items-center gap-2">
            <span class="text-2xl">{{ item.emoji }}</span>
            <span class="font-semibold text-slate-800 text-sm leading-snug">{{ item.title }}</span>
          </div>
          <Tag :severity="statusSeverity(item)" :value="statusLabel(item)" class="flex-shrink-0" />
        </div>

        <!-- Savings Progress -->
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="text-xs text-slate-400 font-medium">Savings Progress</span>
            <span class="text-xs text-slate-500">{{ fmt(item.saved) }} of {{ fmt(item.target) }}</span>
          </div>
          <ProgressBar
            :value="Math.min(100, Math.round((item.saved / item.target) * 100))"
            style="height: 6px"
            :class="progressColor(Math.round((item.saved / item.target) * 100))"
          />
          <div class="flex items-center justify-between mt-1">
            <span class="text-xs text-slate-400">{{ Math.min(100, Math.round((item.saved / item.target) * 100)) }}% saved</span>
            <span class="text-xs text-slate-400">{{ fmt(Math.max(0, item.target - item.saved)) }} to go</span>
          </div>
        </div>

        <!-- Footer -->
        <div class="flex items-center justify-between pt-1 border-t border-slate-50">
          <div>
            <span v-if="item.deadline" class="text-xs text-slate-400">
              <i class="pi pi-calendar text-xs mr-1"></i>{{ item.deadline }}
            </span>
            <span v-else class="text-xs text-slate-400">No deadline</span>
          </div>
          <router-link
            :to="`/wishlist/${item.id}`"
            class="text-violet-600 text-xs font-semibold hover:underline no-underline transition-colors">
            View <i class="pi pi-arrow-right text-xs"></i>
          </router-link>
        </div>
      </div>

      <div v-if="filteredItems.length === 0" class="col-span-3 flex flex-col items-center justify-center py-16 text-slate-400">
        <i class="pi pi-search text-4xl mb-3"></i>
        <p class="text-sm">No wishlist items match your search.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { GOALS } from '@/mockData.js'

export default {
  name: 'WishlistView',
  data() {
    return {
      GOALS,
      search: '',
    }
  },
  computed: {
    filteredItems() {
      if (!this.search) return GOALS
      const q = this.search.toLowerCase()
      return GOALS.filter(item => item.title.toLowerCase().includes(q))
    },
    savingCount() {
      return GOALS.filter(item => item.saved < item.target).length
    },
    reachedCount() {
      return GOALS.filter(item => item.saved >= item.target).length
    },
    pausedCount() {
      return GOALS.filter(item => item.status === 'paused').length
    },
  },
  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },
    statusSeverity(item) {
      if (item.status === 'paused') return 'warn'
      if (item.saved >= item.target) return 'success'
      return 'info'
    },
    statusLabel(item) {
      if (item.status === 'paused') return 'Paused'
      if (item.saved >= item.target) return 'Reached'
      return 'Saving'
    },
    progressColor(pct) {
      if (pct >= 100) return 'progress-reached'
      if (pct >= 70) return 'progress-close'
      return 'progress-saving'
    },
  },
}
</script>

<style scoped>
.progress-reached :deep(.p-progressbar-value) { background: #10b981; }
.progress-close :deep(.p-progressbar-value) { background: #7c3aed; }
.progress-saving :deep(.p-progressbar-value) { background: #a78bfa; }
</style>
