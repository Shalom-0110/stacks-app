<template>
  <div class="flex items-center gap-3 p-4 rounded-xl" :class="background">
    <i :class="icon" style="font-size: 2rem;"/>
    <div>
      <div class="font-bold text-base">{{ statusLabel }}</div>
      <div class="text-sm opacity-75">{{ subtext }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TransactionStatusBadge',
  props: {
    status: {
      type: String,
      required: true,
    },
    subtext: {
      type: String,
      default: '',
    },
  },
  computed: {
    icon() {
      if (this.status === 'completed') return 'pi pi-verified'
      if (this.status === 'failed') return 'pi pi-times'
      return 'pi pi-spinner pi-spin'
    },
    background() {
      if (this.status === 'completed') return 'bg-emerald-50 text-emerald-700'
      if (this.status === 'failed') return 'bg-red-50 text-red-700'
      return 'bg-amber-50 text-amber-700'
    },
    statusLabel() {
      if (this.status === 'completed') return 'Completed'
      if (this.status === 'failed') return 'Failed'
      return 'Pending'
    },
  },
}
</script>
