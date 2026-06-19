<template>
  <div>

    <!-- 1. GREETING ROW -->
    <div class="flex justify-between items-start mb-8">
      <div>
        <h1 class="text-2xl font-black text-slate-800" style="margin:0;">Hey Eirene 👋</h1>
        <p class="text-sm text-slate-400 mt-0.5" style="margin:0;">Thursday, 21 November 2024</p>
      </div>
      <div class="flex items-center gap-3">
        <router-link
          to="/spend"
          class="no-underline"
          style="border:1px solid #ddd6fe;color:#7c3aed;border-radius:12px;font-size:0.875rem;padding:8px 16px;display:inline-flex;align-items:center;gap:6px;font-weight:600;background:white;transition:background 0.15s;"
        >
          <i class="pi pi-credit-card text-xs"></i>
          Log Expense
        </router-link>
        <router-link
          to="/goals"
          class="no-underline"
          style="background:#7c3aed;color:white;border-radius:12px;font-size:0.875rem;padding:8px 16px;display:inline-flex;align-items:center;gap:6px;font-weight:600;border:none;transition:background 0.15s;"
        >
          <i class="pi pi-flag text-xs"></i>
          Set a Goal
        </router-link>
      </div>
    </div>

    <!-- 2. HEALTH SCORE + QUICK STATS -->
    <div class="grid grid-cols-4 gap-4 mb-6">

      <!-- Health Score Card -->
      <div style="background:linear-gradient(135deg,#7c3aed,#a21caf);border-radius:16px;padding:20px;color:white;position:relative;overflow:hidden;">
        <p style="font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin:0 0 8px;">Financial Health</p>
        <div style="display:flex;align-items:baseline;gap:4px;margin-bottom:4px;">
          <span style="font-size:3.2rem;font-weight:900;line-height:1;">84</span>
          <span style="font-size:1rem;opacity:0.7;">/100</span>
        </div>
        <p style="font-size:0.78rem;opacity:0.85;margin:0 0 14px;">😎 You're crushing it!</p>
        <ProgressBar :value="84" :style="{ height: '6px' }" :pt="{ value: { style: 'background:rgba(255,255,255,0.9)' }, root: { style: 'background:rgba(255,255,255,0.25);border-radius:3px;' } }" />
      </div>

      <!-- Income Card -->
      <div class="card">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
          <div class="icon-circle" style="background:#ecfdf5;">
            <i class="pi pi-arrow-circle-down" style="color:#10b981;font-size:0.9rem;"></i>
          </div>
          <span style="font-size:0.75rem;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.5px;">Income</span>
        </div>
        <div style="font-size:1.5rem;font-weight:800;color:#1e1b2e;margin-bottom:4px;">₹56,200</div>
        <div style="font-size:0.75rem;color:#10b981;font-weight:600;">+₹8,200 vs Oct</div>
      </div>

      <!-- Spent Card -->
      <div class="card">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
          <div class="icon-circle" style="background:#fff1f2;">
            <i class="pi pi-credit-card" style="color:#f43f5e;font-size:0.9rem;"></i>
          </div>
          <span style="font-size:0.75rem;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.5px;">Spent</span>
        </div>
        <div style="font-size:1.5rem;font-weight:800;color:#1e1b2e;margin-bottom:4px;">₹21,987</div>
        <div style="font-size:0.75rem;color:#10b981;font-weight:600;">-17% vs Oct ✓</div>
      </div>

      <!-- Saved Card -->
      <div class="card">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
          <div class="icon-circle" style="background:#f5f3ff;">
            <i class="pi pi-shield" style="color:#7c3aed;font-size:0.9rem;"></i>
          </div>
          <span style="font-size:0.75rem;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.5px;">Saved</span>
        </div>
        <div style="font-size:1.5rem;font-weight:800;color:#1e1b2e;margin-bottom:4px;">₹34,213</div>
        <div style="font-size:0.75rem;color:#7c3aed;font-weight:600;">61% savings rate</div>
      </div>

    </div>

    <!-- 3. SPEND BREAKDOWN + RECENT -->
    <div class="grid gap-6 mb-6" style="grid-template-columns:2fr 1fr;">

      <!-- Donut Chart Card -->
      <div class="card">
        <div class="section-title">
          <span>Where it goes 💸</span>
        </div>
        <apexchart
          type="donut"
          height="280"
          :options="donutOptions"
          :series="donutSeries"
        />
      </div>

      <!-- Recent Expenses Card -->
      <div class="card">
        <div class="section-title">
          <span>Recent 🧾</span>
          <router-link to="/spend" class="no-underline" style="font-size:0.78rem;font-weight:600;color:#7c3aed;">View all →</router-link>
        </div>
        <div>
          <div
            v-for="(e, idx) in recentExpenses"
            :key="e.id"
            :style="idx < recentExpenses.length - 1 ? 'border-bottom:1px solid #f8fafc;' : ''"
            style="display:flex;align-items:center;gap:12px;padding:10px 0;"
          >
            <div
              class="icon-circle"
              :style="{ background: catColor(e.category) + '20' }"
              style="font-size:1rem;flex-shrink:0;"
            >
              {{ catIcon(e.category) }}
            </div>
            <div style="flex:1;min-width:0;">
              <div style="font-size:0.875rem;font-weight:600;color:#334155;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{{ e.title }}</div>
              <div style="font-size:0.75rem;color:#94a3b8;">{{ e.date }}</div>
            </div>
            <div style="font-size:0.875rem;font-weight:700;color:#f43f5e;flex-shrink:0;">₹{{ e.amount }}</div>
          </div>
        </div>
      </div>

    </div>

    <!-- 4. GOALS + BUDGETS -->
    <div class="grid grid-cols-2 gap-6 mb-6">

      <!-- Goals Card -->
      <div class="card">
        <div class="section-title">
          <span>My Goals 🎯</span>
          <router-link to="/goals" class="no-underline" style="font-size:0.78rem;font-weight:600;color:#7c3aed;">View all →</router-link>
        </div>
        <div>
          <div
            v-for="(g, idx) in GOALS"
            :key="g.id"
            :style="idx < GOALS.length - 1 ? 'border-bottom:1px solid #f8fafc;' : ''"
            style="display:flex;align-items:center;gap:12px;padding:10px 0;"
          >
            <span style="font-size:1.25rem;">{{ g.emoji }}</span>
            <div style="flex:1;min-width:0;">
              <div style="font-size:0.875rem;font-weight:600;color:#334155;margin-bottom:4px;">{{ g.title }}</div>
              <ProgressBar
                :value="goalPct(g)"
                style="height:4px;"
                :pt="{ value: { style: 'background:' + g.color }, root: { style: 'border-radius:2px;background:#f1f5f9;' } }"
              />
            </div>
            <div style="flex-shrink:0;font-size:0.75rem;font-weight:700;" :style="{ color: g.color }">
              <span v-if="g.saved >= g.target">✅</span>
              <span v-else>{{ goalPct(g) }}%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Budget Card -->
      <div class="card">
        <div class="section-title">
          <span>Budget Check 📊</span>
          <router-link to="/budget" class="no-underline" style="font-size:0.78rem;font-weight:600;color:#7c3aed;">Manage →</router-link>
        </div>
        <div>
          <div
            v-for="(b, idx) in BUDGETS"
            :key="b.category"
            :style="idx < BUDGETS.length - 1 ? 'border-bottom:1px solid #f8fafc;' : ''"
            style="display:flex;align-items:center;gap:8px;padding:8px 0;"
          >
            <div
              class="icon-circle"
              :style="{ background: catColor(b.category) + '20', width: '28px', height: '28px', fontSize: '0.85rem', flexShrink: '0' }"
            >
              {{ catIcon(b.category) }}
            </div>
            <span style="font-size:0.875rem;color:#334155;flex:1;">{{ catLabel(b.category) }}</span>
            <span style="font-size:0.75rem;font-weight:700;" :style="{ color: pctColor(budgetPct(b)) }">{{ budgetPct(b) }}%</span>
            <div style="width:80px;flex-shrink:0;">
              <ProgressBar
                :value="budgetPct(b)"
                style="height:4px;"
                :pt="{ value: { style: 'background:' + pctColor(budgetPct(b)) }, root: { style: 'border-radius:2px;background:#f1f5f9;' } }"
              />
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- 5. CASH FLOW CHART -->
    <div class="card mb-6">
      <div class="section-title" style="margin-bottom:4px;">
        <div>
          <div style="font-size:0.875rem;font-weight:700;color:#334155;">Cash Flow: Last 6 Months 📈</div>
          <div style="font-size:0.75rem;color:#94a3b8;margin-top:2px;">Income vs Expenses</div>
        </div>
      </div>
      <apexchart
        type="area"
        height="200"
        :options="cashFlowOptions"
        :series="cashFlowSeries"
      />
    </div>

  </div>
</template>

<script>
import { CATEGORIES, EXPENSES, GOALS, BUDGETS, MONTHLY, MONTHLY_SPEND_CHART, CAT_MAP } from '@/mockData.js'
import ProgressBar from 'primevue/progressbar'

export default {
  name: 'Home',
  components: { ProgressBar },
  data() {
    return {
      EXPENSES,
      GOALS,
      BUDGETS,
      MONTHLY,
      MONTHLY_SPEND_CHART,
    }
  },
  computed: {
    recentExpenses() {
      return EXPENSES.slice(0, 5)
    },
    donutSeries() {
      const totals = {}
      EXPENSES.forEach(e => {
        totals[e.category] = (totals[e.category] || 0) + e.amount
      })
      return CATEGORIES
        .filter(c => totals[c.id] > 0)
        .map(c => totals[c.id])
    },
    donutLabels() {
      const totals = {}
      EXPENSES.forEach(e => {
        totals[e.category] = (totals[e.category] || 0) + e.amount
      })
      return CATEGORIES
        .filter(c => totals[c.id] > 0)
        .map(c => c.label)
    },
    donutColors() {
      const totals = {}
      EXPENSES.forEach(e => {
        totals[e.category] = (totals[e.category] || 0) + e.amount
      })
      return CATEGORIES
        .filter(c => totals[c.id] > 0)
        .map(c => c.color)
    },
    donutOptions() {
      return {
        chart: {
          type: 'donut',
          toolbar: { show: false },
          fontFamily: 'inherit',
        },
        labels: this.donutLabels,
        colors: this.donutColors,
        plotOptions: {
          pie: {
            donut: {
              size: '65%',
              labels: {
                show: true,
                total: {
                  show: true,
                  label: 'Total Spent',
                  formatter: () => '₹21,987',
                  color: '#334155',
                  fontSize: '13px',
                  fontWeight: 700,
                },
                value: {
                  color: '#1e1b2e',
                  fontSize: '20px',
                  fontWeight: 800,
                },
              },
            },
          },
        },
        legend: {
          position: 'bottom',
          fontSize: '12px',
          fontWeight: 500,
        },
        dataLabels: {
          enabled: false,
        },
        tooltip: {
          y: {
            formatter: (v) => '₹' + new Intl.NumberFormat('en-IN').format(v),
          },
        },
        stroke: {
          width: 2,
          colors: ['#fff'],
        },
      }
    },
    cashFlowSeries() {
      return [
        { name: 'Income', data: MONTHLY_SPEND_CHART.income },
        { name: 'Expenses', data: MONTHLY_SPEND_CHART.expenses },
      ]
    },
    cashFlowOptions() {
      return {
        chart: {
          type: 'area',
          toolbar: { show: false },
          sparkline: { enabled: false },
          fontFamily: 'inherit',
        },
        colors: ['#10b981', '#f43f5e'],
        xaxis: {
          categories: MONTHLY_SPEND_CHART.labels,
          labels: {
            style: { fontSize: '12px', colors: '#94a3b8' },
          },
          axisBorder: { show: false },
          axisTicks: { show: false },
        },
        stroke: {
          curve: 'smooth',
          width: 2,
        },
        fill: {
          type: 'gradient',
          gradient: {
            opacityFrom: 0.3,
            opacityTo: 0.05,
          },
        },
        yaxis: {
          labels: {
            style: { fontSize: '12px', colors: '#94a3b8' },
            formatter: (v) => '₹' + (v / 1000).toFixed(0) + 'k',
          },
        },
        grid: {
          borderColor: '#f0edff',
          strokeDashArray: 4,
        },
        dataLabels: { enabled: false },
        tooltip: {
          y: {
            formatter: (v) => '₹' + new Intl.NumberFormat('en-IN').format(v),
          },
        },
        legend: {
          position: 'top',
          horizontalAlign: 'right',
          fontSize: '12px',
        },
      }
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
    goalPct(g) {
      return Math.min(Math.round((g.saved / g.target) * 100), 100)
    },
    budgetPct(b) {
      return Math.round((b.spent / b.limit) * 100)
    },
    pctColor(pct) {
      return pct >= 85 ? '#ef4444' : pct >= 65 ? '#f59e0b' : '#7c3aed'
    },
  },
}
</script>

<style scoped>
.section-title {
  font-size: 0.875rem;
  font-weight: 700;
  color: #334155;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card {
  background: white;
  border-radius: 16px;
  border: 1px solid #f1f5f9;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
  padding: 20px;
}

.icon-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
</style>
