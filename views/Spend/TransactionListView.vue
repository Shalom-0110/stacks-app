<template>
  <div>
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-slate-800">Transactions</h1>
        <p class="text-slate-500 text-sm mt-1">All your spending transactions in one place.</p>
      </div>
      <router-link
        to="/spend/add"
        class="inline-flex items-center gap-2 bg-violet-600 hover:bg-violet-700 text-white text-sm font-semibold px-4 py-2 rounded-xl transition-colors no-underline">
        <i class="pi pi-plus text-xs"></i>
        Add Transaction
      </router-link>
    </div>

    <!-- Stat Pills -->
    <div class="flex items-center gap-3 mb-6 flex-wrap">
      <div class="inline-flex items-center gap-2 bg-slate-100 rounded-full px-4 py-1.5 text-sm text-slate-700 font-medium">
        <i class="pi pi-wallet text-slate-500 text-xs"></i>
        Total Spent: <span class="font-bold text-slate-800">{{ fmt(totalSpent) }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-amber-50 border border-amber-200 rounded-full px-4 py-1.5 text-sm text-amber-700 font-medium">
        <i class="pi pi-clock text-amber-500 text-xs"></i>
        Pending: <span class="font-bold">{{ pendingCount }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 rounded-full px-4 py-1.5 text-sm text-emerald-700 font-medium">
        <i class="pi pi-check-circle text-emerald-500 text-xs"></i>
        Completed: <span class="font-bold">{{ completedCount }}</span>
      </div>
    </div>

    <!-- Filter Bar -->
    <div class="flex items-center gap-3 mb-6 flex-wrap">
      <InputText
        v-model="search"
        placeholder="Search transactions..."
        class="w-56"
      />
      <Select
        v-model="statusFilter"
        :options="statusOptions"
        option-label="label"
        option-value="value"
        placeholder="All Status"
        class="w-44"
      />
      <Select
        v-model="categoryFilter"
        :options="categoryOptions"
        option-label="label"
        option-value="value"
        placeholder="All Categories"
        class="w-56"
      />
      <button
        v-if="search || statusFilter || categoryFilter"
        @click="clearFilters"
        class="inline-flex items-center gap-1.5 text-slate-500 hover:text-slate-700 text-sm px-3 py-2 rounded-lg hover:bg-slate-100 transition-colors">
        <i class="pi pi-times text-xs"></i>
        Clear
      </button>
    </div>

    <!-- Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
      <DataTable
        :value="filteredTransactions"
        striped-rows
        :show-gridlines="false"
        responsive-layout="scroll"
        class="text-sm">
        <Column field="id" header="#">
          <template #body="{ data }">
            <span class="font-bold text-violet-600">#{{ data.id }}</span>
          </template>
        </Column>
        <Column field="title" header="Description">
          <template #body="{ data }">
            <div class="flex items-center gap-2">
              <span class="text-lg">{{ categoryIcon(data.category) }}</span>
              <span class="font-medium text-slate-700">{{ data.title }}</span>
            </div>
          </template>
        </Column>
        <Column field="category" header="Category">
          <template #body="{ data }">
            <span class="bg-slate-100 text-slate-600 text-xs px-2 py-0.5 rounded-full font-medium capitalize">{{ data.category }}</span>
          </template>
        </Column>
        <Column field="amount" header="Amount">
          <template #body="{ data }">
            <span class="font-bold text-slate-800">{{ fmt(data.amount) }}</span>
          </template>
        </Column>
        <Column field="date" header="Date">
          <template #body="{ data }">
            <span class="text-slate-500 text-sm">{{ data.date }}</span>
          </template>
        </Column>
        <Column field="status" header="Status">
          <template #body="{ data }">
            <Tag :severity="statusSeverity(data.status || 'completed')" :value="data.status || 'Completed'" />
          </template>
        </Column>
        <Column header="Actions">
          <template #body="{ data }">
            <router-link :to="`/spend/${data.id}`">
              <Button icon="pi pi-eye" text rounded size="small" class="text-slate-500 hover:text-violet-600" />
            </router-link>
          </template>
        </Column>
      </DataTable>
      <div v-if="filteredTransactions.length === 0" class="flex flex-col items-center justify-center py-16 text-slate-400">
        <i class="pi pi-inbox text-4xl mb-3"></i>
        <p class="text-sm">No transactions match your filters.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { EXPENSES, CATEGORIES } from '@/mockData.js'

export default {
  name: 'TransactionListView',
  data() {
    return {
      EXPENSES,
      CATEGORIES,
      search: '',
      statusFilter: null,
      categoryFilter: null,
      statusOptions: [
        { label: 'All Status', value: null },
        { label: 'Completed', value: 'completed' },
        { label: 'Pending', value: 'pending' },
        { label: 'Failed', value: 'failed' },
      ],
    }
  },
  computed: {
    categoryOptions() {
      return [
        { label: 'All Categories', value: null },
        ...CATEGORIES.map(c => ({ label: c.label, value: c.id })),
      ]
    },
    filteredTransactions() {
      return EXPENSES.filter(t => {
        const matchSearch = !this.search || t.title.toLowerCase().includes(this.search.toLowerCase())
        const matchStatus = !this.statusFilter || (t.status || 'completed') === this.statusFilter
        const matchCategory = !this.categoryFilter || t.category === this.categoryFilter
        return matchSearch && matchStatus && matchCategory
      })
    },
    totalSpent() {
      return EXPENSES.reduce((sum, t) => sum + t.amount, 0)
    },
    pendingCount() {
      return EXPENSES.filter(t => t.status === 'pending').length
    },
    completedCount() {
      return EXPENSES.filter(t => !t.status || t.status === 'completed').length
    },
  },
  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n)
    },
    categoryIcon(id) {
      return CATEGORIES.find(c => c.id === id)?.icon || '💸'
    },
    statusSeverity(s) {
      if (s === 'pending') return 'warn'
      if (s === 'completed') return 'success'
      if (s === 'failed') return 'danger'
      return 'secondary'
    },
    clearFilters() {
      this.search = ''
      this.statusFilter = null
      this.categoryFilter = null
    },
  },
}
</script>
