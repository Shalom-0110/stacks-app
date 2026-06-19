<template>
  <div class="relative w-64">
    <div class="relative">
      <i class="pi pi-search absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs pointer-events-none"></i>
      <input
        v-model="query"
        type="text"
        placeholder="Search anything..."
        class="w-full pl-8 pr-8 py-2 text-sm border border-slate-200 rounded-xl bg-slate-50 focus:outline-none focus:ring-2 focus:ring-violet-400 focus:border-transparent focus:bg-white transition-all"
        @input="onInput"
        @keydown.esc="clear"
        @keydown.down.prevent="moveDown"
        @keydown.up.prevent="moveUp"
        @keydown.enter.prevent="selectHighlighted"
      />
      <button
        v-if="query"
        class="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
        @click="clear"
      >
        <i class="pi pi-times text-xs"></i>
      </button>
    </div>

    <!-- Dropdown -->
    <div
      v-if="query.length >= 1 && showDropdown"
      class="absolute top-full left-0 right-0 mt-1.5 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 overflow-hidden max-h-80 overflow-y-auto"
    >
      <!-- No results -->
      <div v-if="groups.length === 0" class="px-4 py-6 text-center text-sm text-slate-400">
        <i class="pi pi-search-minus block text-2xl mb-2 text-slate-300"></i>
        Nothing found for "{{ query }}"
      </div>

      <!-- Results grouped by type -->
      <template v-for="group in groups" :key="group.type">
        <div class="px-3 pt-3 pb-1">
          <span class="text-xs font-bold uppercase tracking-widest text-slate-400">{{ group.label }}</span>
        </div>
        <div
          v-for="(item, idx) in group.items"
          :key="group.type + idx"
          :class="[
            'flex items-center gap-3 px-3 py-2.5 cursor-pointer transition-colors',
            highlightedIdx === item._flatIdx ? 'bg-violet-50' : 'hover:bg-slate-50'
          ]"
          @click="navigate(item)"
          @mouseenter="highlightedIdx = item._flatIdx"
        >
          <span
            class="w-8 h-8 rounded-xl flex items-center justify-center text-base flex-shrink-0"
            :style="{ background: item.color + '20' }"
          >{{ item.icon }}</span>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-slate-700 truncate" v-html="highlight(item.title)"></p>
            <p v-if="item.sub" class="text-xs text-slate-400 truncate">{{ item.sub }}</p>
          </div>
          <span class="text-xs font-semibold flex-shrink-0" :style="{ color: item.color }">{{ item.badge }}</span>
        </div>
      </template>

      <div class="px-4 py-2 border-t border-slate-50 text-xs text-slate-300 text-right">
        ↑↓ navigate · ↵ open · esc close
      </div>
    </div>
  </div>
</template>

<script>
import { EXPENSES, GOALS, SUBSCRIPTIONS, INCOME, CAT_MAP } from '@/mockData.js'

export default {
  name: 'GlobalSearch',
  data() {
    return {
      query: '',
      showDropdown: false,
      highlightedIdx: -1,
    }
  },
  computed: {
    flatResults() {
      if (!this.query || this.query.length < 1) return []
      const q = this.query.toLowerCase()

      const results = []

      // Expenses
      EXPENSES.filter(e => e.title.toLowerCase().includes(q) || (e.note || '').toLowerCase().includes(q))
        .slice(0, 4)
        .forEach(e => {
          const cat = CAT_MAP[e.category] || {}
          results.push({
            type: 'expense',
            title: e.title,
            sub: e.date + (e.note ? ' · ' + e.note : ''),
            icon: cat.icon || '💸',
            color: cat.color || '#a78bfa',
            badge: '₹' + e.amount.toLocaleString('en-IN'),
            route: '/spend',
          })
        })

      // Goals
      GOALS.filter(g => g.title.toLowerCase().includes(q))
        .slice(0, 3)
        .forEach(g => {
          const pct = Math.round((g.saved / g.target) * 100)
          results.push({
            type: 'goal',
            title: g.title,
            sub: pct + '% saved · ₹' + g.saved.toLocaleString('en-IN') + ' of ₹' + g.target.toLocaleString('en-IN'),
            icon: g.emoji,
            color: g.color,
            badge: pct + '%',
            route: '/goals',
          })
        })

      // Subscriptions
      SUBSCRIPTIONS.filter(s => s.name.toLowerCase().includes(q))
        .slice(0, 3)
        .forEach(s => {
          results.push({
            type: 'sub',
            title: s.name,
            sub: 'Renews ' + new Date(s.nextDate).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' }),
            icon: s.icon,
            color: s.color,
            badge: '₹' + s.amount + '/mo',
            route: '/subscriptions',
          })
        })

      // Income
      INCOME.filter(i => i.title.toLowerCase().includes(q))
        .slice(0, 2)
        .forEach(i => {
          results.push({
            type: 'income',
            title: i.title,
            sub: i.date + ' · ' + i.type,
            icon: i.icon,
            color: '#10b981',
            badge: '+₹' + i.amount.toLocaleString('en-IN'),
            route: '/earn',
          })
        })

      return results.map((r, idx) => ({ ...r, _flatIdx: idx }))
    },

    groups() {
      const TYPE_META = {
        expense:    { label: 'Transactions' },
        goal:       { label: 'Goals' },
        sub:        { label: 'Subscriptions' },
        income:     { label: 'Income' },
      }
      const map = {}
      this.flatResults.forEach(r => {
        if (!map[r.type]) map[r.type] = { type: r.type, label: TYPE_META[r.type]?.label || r.type, items: [] }
        map[r.type].items.push(r)
      })
      return Object.values(map)
    },
  },
  mounted() {
    document.addEventListener('click', this.handleOutsideClick)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleOutsideClick)
  },
  methods: {
    handleOutsideClick(e) {
      if (!this.$el.contains(e.target)) this.showDropdown = false
    },
    onInput() {
      this.showDropdown = true
      this.highlightedIdx = -1
    },
    clear() {
      this.query = ''
      this.showDropdown = false
      this.highlightedIdx = -1
    },
    navigate(item) {
      this.$router.push(item.route)
      this.clear()
    },
    highlight(text) {
      if (!this.query) return text
      const escaped = this.query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
      return text.replace(new RegExp(`(${escaped})`, 'gi'), '<mark class="bg-violet-100 text-violet-700 rounded px-0.5">$1</mark>')
    },
    moveDown() {
      if (this.highlightedIdx < this.flatResults.length - 1) this.highlightedIdx++
    },
    moveUp() {
      if (this.highlightedIdx > 0) this.highlightedIdx--
    },
    selectHighlighted() {
      const item = this.flatResults[this.highlightedIdx]
      if (item) this.navigate(item)
    },
  },
}
</script>
