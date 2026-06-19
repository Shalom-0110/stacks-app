<template>
  <Loading ref="loader">
    <template #content>
      <div class="flex justify-between items-center mb-6">
        <PageTitle
          :title="transaction.title || 'Transaction Detail'"
          :items="breadcrumbs"/>
        <GlobalSearch/>
      </div>

      <div class="grid grid-cols-4 gap-8">
        <div class="col-span-3">

          <!-- Attachments -->
          <div v-if="transaction.attachments?.length" class="mb-8">
            <SectionTitle title="Attachments" description="Files attached to this transaction"/>
            <Galleria
              :value="transaction.attachments"
              :num-visible="3"
              container-style="max-width: 640px;">
              <template #item="slotProps">
                <a :href="slotProps.item.file" target="_blank">
                  <img :src="slotProps.item.file" :alt="slotProps.item.name" style="height: 300px;">
                </a>
              </template>
              <template #thumbnail="slotProps">
                <img :src="slotProps.item.thumbnail" :alt="slotProps.item.name">
              </template>
            </Galleria>
          </div>

          <!-- Comments -->
          <div class="mt-4">
            <div class="flex justify-between items-center mb-4">
              <SectionTitle title="Notes & Comments" description="Add a note to this transaction"/>
              <Select
                v-model="sortOrder"
                :options="[
                  { label: 'Newest First', value: 'newest' },
                  { label: 'Oldest First', value: 'oldest' }
                ]"
                option-label="label"
                option-value="value"
                class="w-44 text-sm"/>
            </div>

            <!-- New Comment -->
            <div class="mb-6 rounded-xl p-3 bg-slate-50 border border-slate-100">
              <div class="flex items-start gap-3">
                <div class="w-9 h-9 rounded-full bg-violet-100 text-violet-700 flex items-center justify-center text-sm font-bold flex-shrink-0">
                  U
                </div>
                <div class="flex-1">
                  <div class="flex items-start gap-2 mt-1">
                    <Textarea
                      v-model="newComment"
                      rows="1"
                      class="w-full outline-none resize-none bg-transparent text-sm"
                      placeholder="Add a note..."/>
                    <button
                      :disabled="!newComment.trim() && attachments.length === 0"
                      class="p-2 bg-violet-600 hover:bg-violet-700 disabled:bg-slate-200 text-white rounded-full transition-colors"
                      @click="submitComment">
                      <i class="pi pi-send text-xs"></i>
                    </button>
                  </div>
                  <div v-if="attachments.length > 0" class="mt-2 flex flex-wrap gap-2">
                    <div
                      v-for="(file, index) in attachments"
                      :key="index"
                      class="flex items-center gap-1 border border-slate-200 rounded-lg px-2 py-1 text-xs bg-white">
                      <span class="truncate max-w-[120px]">{{ file.name }}</span>
                      <button class="text-red-400 hover:text-red-600" @click="removeAttachment(index)">
                        <i class="pi pi-times text-xs"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="flex items-center mt-3 pl-12">
                <label class="flex items-center gap-1 cursor-pointer text-sm text-slate-500 hover:text-slate-700">
                  <i class="pi pi-paperclip text-sm"></i>
                  <span>Attach</span>
                  <input type="file" multiple class="hidden" @change="onFileChange">
                </label>
              </div>
            </div>

            <!-- Comment List -->
            <div v-for="comment in sortedComments" :key="comment.id" class="mb-5 pl-2">
              <div class="flex gap-3">
                <div class="w-9 h-9 rounded-full bg-slate-200 flex items-center justify-center text-sm font-bold text-slate-600 flex-shrink-0">
                  {{ comment.user?.full_name?.charAt(0) || 'U' }}
                </div>
                <div class="flex-1">
                  <div class="flex items-center gap-2">
                    <span class="font-medium text-slate-700 text-sm">{{ comment.user?.full_name }}</span>
                    <span class="text-xs text-slate-400">{{ timeAgo(comment.created_at) }}</span>
                  </div>
                  <p class="mt-1 text-sm text-slate-600">{{ comment.comment }}</p>
                  <div v-if="comment.attachments_data?.length" class="mt-2 flex flex-wrap gap-2">
                    <a
                      v-for="file in comment.attachments_data"
                      :key="file.id"
                      :href="file.file"
                      target="_blank"
                      class="flex items-center gap-1 text-violet-600 text-xs hover:underline">
                      <i class="pi pi-file text-xs"></i>
                      {{ file.name }}
                    </a>
                  </div>
                </div>
              </div>
            </div>

            <div v-if="comments.length === 0" class="text-center py-8 text-slate-400 text-sm">
              No notes yet. Add one above.
            </div>
          </div>

        </div>

        <!-- Right Sidebar -->
        <div>
          <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 space-y-3">
            <h3 class="font-semibold text-slate-700 text-sm mb-4">Transaction Details</h3>
            <div class="flex justify-between text-sm">
              <span class="text-slate-400">Amount</span>
              <span class="font-bold text-slate-800">{{ fmt(transaction.amount) }}</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-slate-400">Category</span>
              <span class="text-slate-700 capitalize">{{ transaction.category }}</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-slate-400">Date</span>
              <span class="text-slate-700">{{ transaction.date }}</span>
            </div>
            <div v-if="transaction.note" class="flex justify-between text-sm">
              <span class="text-slate-400">Note</span>
              <span class="text-slate-700">{{ transaction.note }}</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-slate-400">Status</span>
              <Tag severity="success" value="Completed" />
            </div>
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
import SectionTitle from '@/components/SectionTitle.vue'
import { getRequest, postRequest } from '@/store/network.js'
import { EXPENSES } from '@/mockData.js'

export default {
  name: 'TransactionDetailView',
  components: { Loading, PageTitle, GlobalSearch, SectionTitle },
  data() {
    return {
      transaction: {},
      comments: [],
      newComment: '',
      attachments: [],
      sortOrder: 'newest',
    }
  },
  computed: {
    breadcrumbs() {
      return [
        { label: 'Spend', route: { name: 'spend' } },
        { label: 'Transactions', route: { name: 'transactions' } },
        { label: this.transaction.title || 'Detail' },
      ]
    },
    sortedComments() {
      return [...this.comments].sort((a, b) => {
        if (this.sortOrder === 'oldest') return new Date(a.created_at) - new Date(b.created_at)
        return new Date(b.created_at) - new Date(a.created_at)
      })
    },
  },
  async mounted() {
    const id = this.$route.params.id
    // Use mock data for now; swap with API call when backend is ready
    this.transaction = EXPENSES.find(e => e.id === Number(id)) || {}
    await this.fetchComments()
    this.$refs.loader.complete()
  },
  methods: {
    fmt(n) {
      return '₹' + new Intl.NumberFormat('en-IN').format(n || 0)
    },
    async fetchComments() {
      try {
        const res = await getRequest(`/api/v1/transaction-comments/?transaction_id=${this.$route.params.id}`)
        this.comments = res.results || []
      } catch {
        this.comments = []
      }
    },
    timeAgo(date) {
      const seconds = Math.floor((new Date() - new Date(date)) / 1000)
      if (seconds < 60) return `${seconds}s ago`
      const minutes = Math.floor(seconds / 60)
      if (minutes < 60) return `${minutes}m ago`
      const hours = Math.floor(minutes / 60)
      if (hours < 24) return `${hours}h ago`
      const days = Math.floor(hours / 24)
      if (days < 7) return `${days}d ago`
      return new Date(date).toLocaleDateString()
    },
    onFileChange(event) {
      this.attachments = [...event.target.files]
      event.target.value = ''
    },
    removeAttachment(index) {
      this.attachments.splice(index, 1)
    },
    async submitComment() {
      if (!this.newComment.trim() && this.attachments.length === 0) return
      const formData = new FormData()
      formData.append('comment', this.newComment)
      formData.append('transaction_id', this.$route.params.id)
      for (const file of this.attachments) {
        try {
          const upload = await postRequest('/api/v1/uploads/', Object.assign(new FormData(), { file }))
          formData.append('attachments', upload.id)
        } catch { /* skip failed uploads */ }
      }
      try {
        await postRequest('/api/v1/transaction-comments/', formData)
        this.newComment = ''
        this.attachments = []
        await this.fetchComments()
      } catch { /* comment failed */ }
    },
  },
}
</script>
