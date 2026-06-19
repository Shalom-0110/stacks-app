<template>
  <Loading ref="loader">
    <template #content>
      <div>
        <div class="flex justify-between items-center mb-6">
          <PageTitle
            :title="refund.title || 'Refund Detail'"
            :description="refund.note"
            :items="[
              { label: 'Earn', route: { name: 'earn' } },
              { label: 'Refunds', route: { name: 'refunds' } },
              { label: refund.title || '' },
            ]"/>
          <GlobalSearch/>
        </div>

        <div class="grid grid-cols-3 gap-8">
          <!-- Main Content -->
          <div class="col-span-2 space-y-5">
            <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
              <h3 class="font-semibold text-slate-700 mb-4">Refund Details</h3>
              <div class="space-y-3">
                <div class="flex justify-between text-sm">
                  <span class="text-slate-400">Amount</span>
                  <span class="font-bold text-emerald-600 text-lg">{{ fmt(refund.amount) }}</span>
                </div>
                <div class="flex justify-between text-sm">
                  <span class="text-slate-400">Type</span>
                  <span class="text-slate-700 capitalize">{{ refund.type }}</span>
                </div>
                <div class="flex justify-between text-sm">
                  <span class="text-slate-400">Date</span>
                  <span class="text-slate-700">{{ refund.date }}</span>
                </div>
                <div class="flex justify-between text-sm">
                  <span class="text-slate-400">Status</span>
                  <Tag severity="success" value="Received" />
                </div>
              </div>
            </div>
          </div>

          <!-- Sidebar -->
          <div class="space-y-4">
            <Button
              label="Download Receipt"
              icon="pi pi-download"
              class="w-full"
              @click="downloadReceipt"/>
          </div>
        </div>
      </div>
    </template>
  </Loading>
</template>

<script>
import Loading from '@/components/Loading.vue'
import PageTitle from '@/components/PageTitle.vue'
import GlobalSearch from '@/components/GlobalSearch.vue'
import { INCOME } from '@/mockData.js'

export default {
  name: 'RefundDetailView',
  components: { Loading, PageTitle, GlobalSearch },
  data() {
    return { refund: {} }
  },
  async mounted() {
    const id = this.$route.params.id
    this.refund = INCOME.find(i => i.id === Number(id) && i.type === 'refund') || {}
    this.$refs.loader.complete()
  },
  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n || 0)
    },
    async downloadReceipt() {
      try {
        const response = await fetch(`/api/v1/refunds/${this.$route.params.id}/download-pdf/`)
        if (!response.ok) throw new Error('Failed to fetch PDF')
        const blob = await response.blob()
        const url = window.URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = 'Refund_Receipt.pdf'
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
        window.URL.revokeObjectURL(url)
      } catch {
        this.$toast.add({ severity: 'error', summary: 'Error', detail: 'Could not download receipt.', life: 3000 })
      }
    },
  },
}
</script>
