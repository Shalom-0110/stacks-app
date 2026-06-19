<template>
  <Loading ref="loader">
  <template #content>
  <div class="p-6 max-w-2xl mx-auto">
    <PageTitle
      title="Subscriptions"
      description="Know what's draining you every month"
      :items="[{ label: 'Subscriptions' }]"
    />

    <!-- Hero Stats -->
    <div class="grid grid-cols-3 gap-4 mb-6">
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 text-center">
        <p class="text-2xl font-black text-rose-600">{{ fmt(monthlyTotal) }}/mo</p>
        <p class="text-xs text-slate-400 mt-1">leaving every month 💸</p>
      </div>
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 text-center">
        <p class="text-2xl font-black text-amber-600">{{ fmt(monthlyTotal * 12) }}/yr</p>
        <p class="text-xs text-slate-400 mt-1">if nothing changes</p>
      </div>
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 text-center">
        <p class="text-2xl font-black text-violet-600">{{ SUBSCRIPTIONS.length }} active</p>
        <p class="text-xs text-slate-400 mt-1">subscriptions</p>
      </div>
    </div>

    <!-- Subscriptions Grid -->
    <div class="grid grid-cols-2 gap-4 mb-6">
      <div
        v-for="sub in SUBSCRIPTIONS"
        :key="sub.id"
        class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 hover:shadow-md transition"
      >
        <div class="flex items-center gap-4">
          <div
            class="rounded-2xl flex items-center justify-center text-2xl flex-shrink-0"
            :style="{ width: '52px', height: '52px', backgroundColor: sub.color + '20' }"
          >
            {{ sub.icon }}
          </div>

          <div class="flex-1 min-w-0">
            <div class="flex items-center flex-wrap gap-1">
              <span class="font-bold text-slate-800 text-sm">{{ sub.name }}</span>
              <span class="text-xs bg-rose-50 text-rose-600 px-2 py-0.5 rounded-full font-bold">
                {{ fmt(sub.amount) }}/mo
              </span>
            </div>
            <p class="text-sm text-slate-400 mt-0.5">Renews {{ fmtDate(sub.nextDate) }}</p>
          </div>

          <div class="flex-shrink-0">
            <span
              v-if="daysUntil(sub.nextDate) <= 3"
              class="bg-rose-100 text-rose-700 text-xs font-bold px-2 py-1 rounded-full whitespace-nowrap"
            >
              In {{ daysUntil(sub.nextDate) }} days ⚠️
            </span>
            <span
              v-else-if="daysUntil(sub.nextDate) <= 7"
              class="bg-amber-100 text-amber-700 text-xs font-bold px-2 py-1 rounded-full whitespace-nowrap"
            >
              In {{ daysUntil(sub.nextDate) }} days
            </span>
            <span
              v-else
              class="bg-slate-100 text-slate-500 text-xs font-bold px-2 py-1 rounded-full whitespace-nowrap"
            >
              In {{ daysUntil(sub.nextDate) }} days
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Renewing Soon -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 mb-6">
      <p class="font-bold text-slate-800 mb-3">⏰ Renewing Soon</p>
      <div>
        <div
          v-for="sub in renewingSoon"
          :key="sub.id"
          class="flex items-center gap-3 py-2.5 border-b last:border-0 border-slate-50"
        >
          <div
            class="rounded-full flex items-center justify-center text-lg flex-shrink-0"
            :style="{ width: '36px', height: '36px', backgroundColor: sub.color + '20' }"
          >
            {{ sub.icon }}
          </div>
          <span class="flex-1 font-medium text-slate-700 text-sm">{{ sub.name }}</span>
          <span class="text-sm text-slate-400">{{ fmtDate(sub.nextDate) }}</span>
          <span class="font-bold text-rose-500 text-sm">{{ fmt(sub.amount) }}</span>
        </div>
      </div>
    </div>

    <!-- Annual Savings Card -->
    <div class="bg-gradient-to-r from-violet-50 to-fuchsia-50 border border-violet-100 rounded-2xl p-5">
      <p class="font-bold text-violet-800">
        If you cancelled everything, you'd save {{ fmt(monthlyTotal * 12) }} a year 🤯
      </p>
      <p class="text-sm text-slate-500 mt-1">
        That's a MacBook, or a Goa trip every single month 😅
      </p>
    </div>
  </div>
  </template>
  </Loading>
</template>

<script>
import { SUBSCRIPTIONS } from '@/mockData.js'

export default {
  name: 'SubsView',

  data() {
    return {
      SUBSCRIPTIONS,
    }
  },

  mounted() {
    this.$refs.loader.complete()
  },

  computed: {
    sortedByDate() {
      return [...SUBSCRIPTIONS].sort((a, b) => new Date(a.nextDate) - new Date(b.nextDate))
    },
    renewingSoon() {
      return this.sortedByDate.slice(0, 3)
    },
    monthlyTotal() {
      return SUBSCRIPTIONS.reduce((s, sub) => s + sub.amount, 0)
    },
  },

  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },
    daysUntil(dateStr) {
      const start = new Date('2024-11-21')
      const end = new Date(dateStr)
      return Math.ceil((end - start) / (1000 * 60 * 60 * 24))
    },
    fmtDate(dateStr) {
      return new Date(dateStr).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })
    },
  },
}
</script>
