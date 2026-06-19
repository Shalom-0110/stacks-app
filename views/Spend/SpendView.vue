<template>
  <Loading ref="loader">
  <template #content>
  <div class="p-6 max-w-6xl mx-auto">
    <PageTitle
      title="Spend"
      description="Track where every rupee goes"
      :items="[{ label: 'Spend' }]"
    />

    <!-- Stats Row -->
    <div class="grid grid-cols-3 gap-4 mb-6">
      <!-- Total this month -->
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-arrow-down-circle text-rose-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">Total this month</span>
        </div>
        <p class="text-2xl font-black text-rose-500">₹21,987</p>
      </div>

      <!-- vs Last month -->
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-chart-line text-emerald-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">vs Last month</span>
        </div>
        <p class="text-2xl font-black text-emerald-500">-17% less 🎉</p>
        <p class="text-xs text-slate-400 mt-1">Spent ₹26,400 in Oct</p>
      </div>

      <!-- Top category -->
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="flex items-center gap-2 mb-2">
          <i class="pi pi-tag text-slate-400 text-lg"></i>
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">Top category</span>
        </div>
        <p class="text-2xl font-black text-slate-700">🏠 Rent & Bills</p>
        <p class="text-xs text-slate-400 mt-1">₹13,200</p>
      </div>
    </div>

    <!-- By Category -->
    <div class="mb-6">
      <h2 class="font-bold text-slate-700 mb-3">Where it went</h2>
      <div class="grid grid-cols-3 gap-3">
        <div
          v-for="cat in categoryTotals"
          :key="cat.id"
          class="bg-white rounded-2xl border border-slate-100 p-4 cursor-pointer hover:shadow-md transition-shadow"
          :class="selectedCat === cat.id ? 'ring-2 ring-violet-400' : ''"
          @click="selectedCat = selectedCat === cat.id ? null : cat.id"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-10 h-10 rounded-full flex items-center justify-center text-xl flex-shrink-0"
              :style="{ background: cat.color + '20' }"
            >
              {{ cat.icon }}
            </div>
            <div class="min-w-0">
              <p class="text-sm font-semibold text-slate-700 truncate">{{ cat.label }}</p>
              <p class="text-lg font-black" :style="{ color: cat.color }">{{ fmt(cat.total) }}</p>
              <p class="text-xs text-slate-400">{{ cat.count }} transactions</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Filter Row -->
    <div class="flex gap-3 mb-4 flex-wrap items-center">
      <InputText
        v-model="search"
        placeholder="Search transactions..."
        class="w-56"
      />

      <span
        v-if="selectedCat"
        class="inline-flex items-center gap-1.5 bg-violet-100 text-violet-700 rounded-full px-3 py-1 text-sm font-medium"
      >
        <span>{{ catIcon(selectedCat) }}</span>
        <span>{{ catLabel(selectedCat) }}</span>
        <button
          @click="selectedCat = null"
          class="ml-1 text-violet-400 hover:text-violet-700 leading-none"
        >&times;</button>
      </span>

      <button
        v-if="search || selectedCat"
        @click="search = ''; selectedCat = null"
        class="text-sm text-slate-400 hover:text-slate-600 underline"
      >
        Clear all
      </button>
    </div>

    <!-- Transaction List -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
      <DataTable
        :value="filteredExpenses"
        striped-rows
        :show-gridlines="false"
        responsive-layout="scroll"
      >
        <!-- Category icon column -->
        <Column header="" style="width: 3rem">
          <template #body="{ data }">
            <div
              class="w-9 h-9 rounded-full flex items-center justify-center text-lg"
              :style="{ background: catColor(data.category) + '20' }"
            >
              {{ catIcon(data.category) }}
            </div>
          </template>
        </Column>

        <!-- Title + note -->
        <Column header="Description" style="min-width: 200px">
          <template #body="{ data }">
            <p class="font-medium text-slate-700">{{ data.title }}</p>
            <p v-if="data.note" class="text-xs text-slate-400 italic mt-0.5">{{ data.note }}</p>
          </template>
        </Column>

        <!-- Date -->
        <Column field="date" header="Date">
          <template #body="{ data }">
            <span class="text-slate-400 text-sm">{{ data.date }}</span>
          </template>
        </Column>

        <!-- Amount -->
        <Column header="Amount" style="text-align: right">
          <template #body="{ data }">
            <span class="font-bold text-rose-500 block text-right">{{ fmt(data.amount) }}</span>
          </template>
        </Column>
      </DataTable>

      <!-- Empty state -->
      <div
        v-if="filteredExpenses.length === 0"
        class="flex flex-col items-center justify-center py-12 text-slate-400"
      >
        <i class="pi pi-search text-3xl mb-3"></i>
        <p class="font-medium">Nothing found</p>
        <p class="text-sm mt-1">Try adjusting your filters</p>
      </div>
    </div>
  </div>
  </template>
  </Loading>
</template>

<script>
import { EXPENSES, CATEGORIES, CAT_MAP } from '@/mockData.js'

export default {
  name: 'SpendView',

  data() {
    return {
      EXPENSES,
      CATEGORIES,
      search: '',
      selectedCat: null,
    }
  },

  mounted() {
    this.$refs.loader.complete()
  },

  computed: {
    categoryTotals() {
      return CATEGORIES
        .map(c => ({
          ...c,
          total: EXPENSES.filter(e => e.category === c.id).reduce((s, e) => s + e.amount, 0),
          count: EXPENSES.filter(e => e.category === c.id).length,
        }))
        .filter(c => c.total > 0)
    },

    filteredExpenses() {
      return EXPENSES
        .filter(e => {
          const matchSearch = !this.search || e.title.toLowerCase().includes(this.search.toLowerCase())
          const matchCat = !this.selectedCat || e.category === this.selectedCat
          return matchSearch && matchCat
        })
        .slice()
        .sort((a, b) => new Date(b.date) - new Date(a.date))
    },
  },

  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },

    catColor(id) {
      return CAT_MAP[id]?.color || '#a78bfa'
    },

    catIcon(id) {
      return CAT_MAP[id]?.icon || '💸'
    },

    catLabel(id) {
      return CAT_MAP[id]?.label || id
    },
  },
}
</script>
