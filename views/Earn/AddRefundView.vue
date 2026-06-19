<template>
  <div>
    <PageTitle
      title="Add Refund"
      description="Log a refund or cashback you received"
      :items="[{ label: 'Earn', route: { name: 'earn' } }, { label: 'Refunds', route: { name: 'refunds' } }]"/>

    <div class="max-w-lg mt-6">
      <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 space-y-5">
        <div class="flex flex-col gap-1">
          <label class="text-sm font-medium text-slate-600">Title</label>
          <InputText v-model="form.title" placeholder="e.g. Amazon refund" class="w-full"/>
          <small v-if="errors.title" class="text-red-500">{{ errors.title }}</small>
        </div>

        <div class="flex flex-col gap-1">
          <label class="text-sm font-medium text-slate-600">Amount (₹)</label>
          <InputNumber v-model="form.amount" placeholder="0" :min="0" class="w-full"/>
          <small v-if="errors.amount" class="text-red-500">{{ errors.amount }}</small>
        </div>

        <div class="flex flex-col gap-1">
          <label class="text-sm font-medium text-slate-600">Date</label>
          <DatePicker v-model="form.date" date-format="yy-mm-dd" class="w-full"/>
        </div>

        <div class="flex flex-col gap-1">
          <label class="text-sm font-medium text-slate-600">Note (optional)</label>
          <Textarea v-model="form.note" rows="2" placeholder="Any details..." class="w-full"/>
        </div>

        <div class="flex gap-3 pt-2">
          <Button label="Save Refund" icon="pi pi-check" class="flex-1" @click="submit"/>
          <Button label="Cancel" severity="secondary" text @click="$router.back()"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/PageTitle.vue'

export default {
  name: 'AddRefundView',
  components: { PageTitle },
  data() {
    return {
      form: { title: '', amount: null, date: null, note: '' },
      errors: {},
    }
  },
  methods: {
    validate() {
      this.errors = {}
      if (!this.form.title.trim()) this.errors.title = 'Title is required'
      if (!this.form.amount || this.form.amount <= 0) this.errors.amount = 'Enter a valid amount'
      return Object.keys(this.errors).length === 0
    },
    async submit() {
      if (!this.validate()) return
      try {
        // API call goes here when backend is ready
        this.$toast.add({ severity: 'success', summary: 'Saved', detail: 'Refund logged successfully.', life: 3000 })
        this.$router.push({ name: 'earn' })
      } catch {
        this.$toast.add({ severity: 'error', summary: 'Error', detail: 'Could not save refund.', life: 3000 })
      }
    },
  },
}
</script>
