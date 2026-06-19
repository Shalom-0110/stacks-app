<template>
  <div>
    <!-- Page Header -->
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-slate-800">Tax Cuts</h1>
        <p class="text-slate-500 text-sm mt-1">TDS deduction master for all payments and vendor transactions.</p>
      </div>
      <router-link
        to="/tds/create"
        class="inline-flex items-center gap-2 bg-violet-600 hover:bg-violet-700 text-white text-sm font-semibold px-4 py-2 rounded-xl transition-colors no-underline">
        <i class="pi pi-plus text-xs"></i>
        New TDS Rule
      </router-link>
    </div>

    <!-- Summary Pill -->
    <div class="flex items-center gap-3 mb-6 flex-wrap">
      <div class="inline-flex items-center gap-2 bg-slate-100 rounded-full px-4 py-1.5 text-sm text-slate-700 font-medium">
        <i class="pi pi-percentage text-slate-500 text-xs"></i>
        Total Rules: <span class="font-bold text-slate-800">{{ tdsList.length }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 rounded-full px-4 py-1.5 text-sm text-emerald-700 font-medium">
        <span class="w-2 h-2 rounded-full bg-emerald-500 inline-block"></span>
        Active: <span class="font-bold">{{ activeCount }}</span>
      </div>
    </div>

    <!-- Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
      <DataTable :value="tdsList" :show-gridlines="false" striped-rows class="text-sm">
        <Column field="code" header="TDS Code">
          <template #body="{ data }">
            <span class="font-bold text-violet-600 font-mono text-sm">{{ data.code }}</span>
          </template>
        </Column>
        <Column field="desc" header="Description">
          <template #body="{ data }">
            <span class="font-medium text-slate-700">{{ data.desc }}</span>
          </template>
        </Column>
        <Column field="rate" header="Rate">
          <template #body="{ data }">
            <span class="font-bold text-slate-800">{{ data.rate }}%</span>
          </template>
        </Column>
        <Column field="applicableOn" header="Applicable On">
          <template #body="{ data }">
            <span class="text-sm text-slate-500">{{ data.applicableOn }}</span>
          </template>
        </Column>
        <Column field="status" header="Status">
          <template #body="{ data }">
            <Tag :severity="statusSeverity(data.status)" :value="data.status" class="capitalize" />
          </template>
        </Column>
        <Column header="Actions">
          <template #body>
            <div class="flex items-center gap-1">
              <Button icon="pi pi-pencil" text rounded size="small" class="text-slate-400 hover:text-violet-600" />
              <Button icon="pi pi-eye" text rounded size="small" class="text-slate-400 hover:text-violet-600" />
            </div>
          </template>
        </Column>
      </DataTable>
    </div>

    <!-- Info Card -->
    <div class="mt-6 bg-amber-50 border border-amber-200 rounded-2xl p-4 flex items-start gap-3">
      <i class="pi pi-info-circle text-amber-500 mt-0.5 flex-shrink-0"></i>
      <div>
        <div class="text-sm font-semibold text-amber-800">TDS Compliance Note</div>
        <div class="text-xs text-amber-700 mt-0.5">
          TDS rates are subject to changes per the Income Tax Act and annual Finance Budget. Verify with your CA before applying.
          Quarterly TDS returns must be filed in Form 24Q/26Q by the 31st of the month following each quarter.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TDSView',
  data() {
    return {
      tdsList: [
        { code: '194C', desc: 'TDS on Contractor Payments', rate: 2, applicableOn: 'Contract >Rs 30,000', status: 'active' },
        { code: '194J', desc: 'TDS on Professional Services', rate: 10, applicableOn: 'Professional fees >Rs 30,000', status: 'active' },
        { code: '194I', desc: 'TDS on Rent', rate: 10, applicableOn: 'Rent >Rs 2,40,000 p.a.', status: 'active' },
        { code: '192', desc: 'TDS on Salary', rate: 30, applicableOn: 'As per income slab', status: 'active' },
        { code: '194H', desc: 'TDS on Commission', rate: 5, applicableOn: 'Commission >Rs 15,000', status: 'inactive' },
      ],
    }
  },
  computed: {
    activeCount() {
      return this.tdsList.filter(t => t.status === 'active').length
    },
  },
  methods: {
    statusSeverity(s) {
      if (s === 'active') return 'success'
      if (s === 'inactive') return 'secondary'
      return 'secondary'
    },
  },
}
</script>
