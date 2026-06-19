<template>
  <Loading ref="loader">
  <template #content>
  <div class="p-6 max-w-6xl mx-auto">
    <PageTitle
      title="Earn"
      description="All the money coming in"
      :items="[{ label: 'Earn' }]"
    />

    <!-- Hero Card -->
    <div class="bg-gradient-to-br from-emerald-500 to-teal-600 rounded-3xl p-8 text-white mb-6">
      <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-6">
        <div>
          <p class="text-white/70 text-xs uppercase tracking-widest font-semibold mb-2">
            Total income this month
          </p>
          <p class="text-5xl font-black">₹56,200</p>
          <p class="text-emerald-100 text-sm mt-1">↑ ₹8,200 more than last month</p>

          <div class="flex gap-4 mt-4 flex-wrap">
            <div class="bg-white/10 rounded-2xl px-4 py-3">
              <p class="text-white/70 text-xs mb-1">💼 Salary</p>
              <p class="font-bold text-white">₹45,000</p>
            </div>
            <div class="bg-white/10 rounded-2xl px-4 py-3">
              <p class="text-white/70 text-xs mb-1">💻 Freelance</p>
              <p class="font-bold text-white">₹8,000</p>
            </div>
            <div class="bg-white/10 rounded-2xl px-4 py-3">
              <p class="text-white/70 text-xs mb-1">Other</p>
              <p class="font-bold text-white">₹3,200</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Cash Flow Cards -->
    <div class="grid grid-cols-3 gap-4 mb-6">
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-arrow-circle-down text-emerald-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">This month</span>
        </div>
        <p class="text-2xl font-black text-emerald-500">₹56,200</p>
        <p class="text-xs text-slate-400 mt-1">Total income</p>
      </div>

      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-arrow-circle-up text-rose-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">Spent this month</span>
        </div>
        <p class="text-2xl font-black text-rose-500">₹21,987</p>
        <p class="text-xs text-slate-400 mt-1">Total expenses</p>
      </div>

      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-shield text-violet-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">Saved</span>
        </div>
        <p class="text-2xl font-black text-violet-600">₹34,213</p>
        <p class="text-xs text-slate-400 mt-1">61% savings rate</p>
      </div>
    </div>

    <!-- Income Sources + History Row -->
    <div class="grid grid-cols-2 gap-6">
      <!-- Donut Chart -->
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <h2 class="font-bold text-slate-700 mb-4">Income Sources</h2>
        <VueApexCharts
          type="donut"
          height="240"
          :options="chartOptions"
          :series="chartSeries"
        />
      </div>

      <!-- Income History -->
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center justify-between mb-4">
          <h2 class="font-bold text-slate-700">Income History</h2>
          <Button label="Add Income" size="small" class="p-button-sm" />
        </div>

        <div>
          <div
            v-for="item in INCOME"
            :key="item.id"
            class="flex items-center gap-3 py-3 border-b last:border-0 border-slate-50"
          >
            <div class="w-10 h-10 rounded-full bg-emerald-50 flex items-center justify-center text-xl flex-shrink-0">
              {{ item.icon }}
            </div>

            <div class="flex-1 min-w-0">
              <p class="font-medium text-slate-700 truncate">{{ item.title }}</p>
              <Tag :severity="typeSeverity(item.type)" :value="item.type" class="mt-1 text-xs capitalize" />
            </div>

            <span class="text-sm text-slate-400 flex-shrink-0">{{ item.date }}</span>
            <span class="font-bold text-emerald-600 flex-shrink-0">{{ fmt(item.amount) }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  </Loading>
</template>

<script>
import { INCOME, MONTHLY } from '@/mockData.js'

export default {
  name: 'EarnView',

  data() {
    return {
      INCOME,
      MONTHLY,
      chartSeries: [45000, 8000, 3000, 200],
      chartOptions: {
        labels: ['Salary', 'Freelance', 'Gift', 'Refund'],
        colors: ['#7c3aed', '#10b981', '#f59e0b', '#3b82f6'],
        plotOptions: {
          pie: {
            donut: {
              size: '65%',
              labels: {
                show: true,
                total: {
                  show: true,
                  label: 'Total',
                  formatter: () => '₹56,200',
                },
              },
            },
          },
        },
        legend: {
          position: 'bottom',
        },
        dataLabels: {
          enabled: false,
        },
      },
    }
  },

  mounted() {
    this.$refs.loader.complete()
  },

  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },

    typeSeverity(type) {
      return (
        { salary: 'success', freelance: 'info', gift: 'warn', refund: 'secondary' }[type] ||
        'secondary'
      )
    },
  },
}
</script>
