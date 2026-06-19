<template>
  <div class="space-y-4">
    <div class="flex flex-col gap-1">
      <label class="text-sm font-medium text-slate-600">Amount (₹)</label>
      <InputNumber v-model="form.amount" placeholder="0" :min="0" class="w-full"/>
      <small v-if="errors.amount" class="text-red-500">{{ errors.amount }}</small>
    </div>

    <div class="flex flex-col gap-1">
      <label class="text-sm font-medium text-slate-600">Category</label>
      <div class="grid grid-cols-3 gap-2">
        <button
          v-for="cat in categories"
          :key="cat.id"
          @click="form.category = cat.id"
          class="flex flex-col items-center gap-1 p-3 rounded-xl border text-sm transition-all"
          :class="form.category === cat.id
            ? 'border-violet-400 bg-violet-50 text-violet-700 font-semibold'
            : 'border-slate-100 bg-white text-slate-600 hover:bg-slate-50'">
          <span class="text-xl">{{ cat.icon }}</span>
          <span class="text-xs">{{ cat.label }}</span>
        </button>
      </div>
      <small v-if="errors.category" class="text-red-500">{{ errors.category }}</small>
    </div>

    <div class="flex flex-col gap-1">
      <label class="text-sm font-medium text-slate-600">Title</label>
      <InputText v-model="form.title" placeholder="e.g. Zomato order" class="w-full"/>
    </div>

    <div class="flex flex-col gap-1">
      <label class="text-sm font-medium text-slate-600">Note (optional)</label>
      <InputText v-model="form.note" placeholder="Any details..." class="w-full"/>
    </div>

    <Button label="Save" icon="pi pi-check" class="w-full" @click="submit"/>
  </div>
</template>

<script>
import { CATEGORIES } from '@/mockData.js'

export default {
  name: 'TransactionForm',
  emits: ['success'],
  data() {
    return {
      categories: CATEGORIES,
      form: { amount: null, category: null, title: '', note: '' },
      errors: {},
    }
  },
  methods: {
    validate() {
      this.errors = {}
      if (!this.form.amount || this.form.amount <= 0) this.errors.amount = 'Enter a valid amount'
      if (!this.form.category) this.errors.category = 'Pick a category'
      return Object.keys(this.errors).length === 0
    },
    async submit() {
      if (!this.validate()) return
      this.$emit('success', { ...this.form })
      this.form = { amount: null, category: null, title: '', note: '' }
    },
  },
}
</script>
