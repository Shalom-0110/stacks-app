<template>
  <div>
    <!-- Page Header -->
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-slate-800">The Crew</h1>
        <p class="text-slate-500 text-sm mt-1">Manage team members, roles, and permissions.</p>
      </div>
      <Button
        label="Invite Member"
        icon="pi pi-user-plus"
        class="bg-violet-600 hover:bg-violet-700 border-violet-600 text-white font-semibold rounded-xl"
      />
    </div>

    <!-- Stats Pills -->
    <div class="flex items-center gap-3 mb-6 flex-wrap">
      <div class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 rounded-full px-4 py-1.5 text-sm text-emerald-700 font-medium">
        <span class="w-2 h-2 rounded-full bg-emerald-500 inline-block"></span>
        Active: <span class="font-bold">{{ activeCount }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-slate-100 rounded-full px-4 py-1.5 text-sm text-slate-600 font-medium">
        <span class="w-2 h-2 rounded-full bg-slate-400 inline-block"></span>
        Inactive: <span class="font-bold">{{ inactiveCount }}</span>
      </div>
      <div class="inline-flex items-center gap-2 bg-slate-100 rounded-full px-4 py-1.5 text-sm text-slate-600 font-medium">
        <i class="pi pi-users text-slate-500 text-xs"></i>
        Total: <span class="font-bold">{{ USERS.length }}</span>
      </div>
    </div>

    <!-- Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
      <DataTable :value="USERS" striped-rows :show-gridlines="false" class="text-sm">
        <Column header="Member">
          <template #body="{ data }">
            <div class="flex items-center">
              <div class="w-8 h-8 rounded-full bg-violet-100 text-violet-700 flex items-center justify-center text-xs font-bold mr-3 flex-shrink-0">
                {{ data.initials }}
              </div>
              <div>
                <div class="font-medium text-slate-800 text-sm">{{ data.name }}</div>
                <div class="text-xs text-slate-400">@{{ data.username }}</div>
              </div>
            </div>
          </template>
        </Column>
        <Column field="role" header="Role">
          <template #body="{ data }">
            <Tag :severity="roleSeverity(data.role)" :value="data.role" />
          </template>
        </Column>
        <Column field="dept" header="Department">
          <template #body="{ data }">
            <span class="text-slate-600 text-sm">{{ data.dept }}</span>
          </template>
        </Column>
        <Column header="Status">
          <template #body="{ data }">
            <div class="flex items-center gap-2">
              <span
                class="w-2 h-2 rounded-full inline-block flex-shrink-0"
                :class="data.status === 'active' ? 'bg-emerald-500' : 'bg-slate-300'"
              ></span>
              <span
                class="text-sm font-medium"
                :class="data.status === 'active' ? 'text-emerald-700' : 'text-slate-400'">
                {{ data.status === 'active' ? 'Active' : 'Inactive' }}
              </span>
            </div>
          </template>
        </Column>
        <Column header="Actions">
          <template #body>
            <Button icon="pi pi-pencil" text rounded size="small" class="text-slate-400 hover:text-violet-600" />
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import { USERS } from '@/mockData.js'

export default {
  name: 'UsersView',
  data() {
    return {
      USERS,
    }
  },
  computed: {
    activeCount() {
      return USERS.filter(u => u.status === 'active').length
    },
    inactiveCount() {
      return USERS.filter(u => u.status === 'inactive').length
    },
  },
  methods: {
    roleSeverity(role) {
      if (role === 'Admin') return 'danger'
      if (role === 'Finance Manager') return 'success'
      if (role === 'Budget Manager') return 'info'
      return 'secondary'
    },
  },
}
</script>
