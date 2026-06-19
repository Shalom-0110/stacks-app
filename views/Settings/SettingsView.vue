<template>
  <div>
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-2xl font-bold text-slate-800">Tune Up</h1>
      <p class="text-slate-500 text-sm mt-1">Configure how Stacks works for your org.</p>
    </div>

    <!-- Tabs -->
    <Tabs value="0">
      <TabList>
        <Tab value="0">
          <i class="pi pi-cog mr-2"></i>General
        </Tab>
        <Tab value="1">
          <i class="pi pi-bell mr-2"></i>Notifications
        </Tab>
        <Tab value="2">
          <i class="pi pi-shield mr-2"></i>Fund Rules
        </Tab>
      </TabList>

      <TabPanels>
        <!-- General -->
        <TabPanel value="0">
          <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 mt-4 max-w-2xl">
            <h2 class="text-base font-bold text-slate-800 mb-6">Organisation Settings</h2>
            <div class="flex flex-col gap-5">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1.5">Organisation Name</label>
                <InputText v-model="orgName" class="w-full" placeholder="Enter organisation name" />
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1.5">Financial Year Start</label>
                <Select
                  v-model="fyStart"
                  :options="fyOptions"
                  option-label="label"
                  option-value="value"
                  class="w-full"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1.5">Default Currency</label>
                <InputText value="Rs (Indian Rupee)" disabled class="w-full bg-slate-50 text-slate-400" />
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1.5">Date Format</label>
                <InputText value="DD/MM/YYYY" disabled class="w-full bg-slate-50 text-slate-400" />
              </div>
              <div class="pt-2">
                <Button
                  label="Save Settings"
                  icon="pi pi-check"
                  class="bg-violet-600 hover:bg-violet-700 border-violet-600 text-white font-semibold rounded-xl"
                  @click="saveSettings"
                />
              </div>
            </div>
          </div>
        </TabPanel>

        <!-- Notifications -->
        <TabPanel value="1">
          <div class="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 mt-4 max-w-2xl">
            <h2 class="text-base font-bold text-slate-800 mb-2">Notification Preferences</h2>
            <p class="text-slate-400 text-sm mb-6">Choose which events trigger email notifications.</p>
            <div class="flex flex-col divide-y divide-slate-50">
              <div class="flex items-center justify-between py-4">
                <div>
                  <div class="text-sm font-medium text-slate-700">Expense claim submitted</div>
                  <div class="text-xs text-slate-400 mt-0.5">Notify when a new claim is submitted for review</div>
                </div>
                <ToggleSwitch v-model="notif.submitted" />
              </div>
              <div class="flex items-center justify-between py-4">
                <div>
                  <div class="text-sm font-medium text-slate-700">Claim approved</div>
                  <div class="text-xs text-slate-400 mt-0.5">Notify the claimant when their claim is approved</div>
                </div>
                <ToggleSwitch v-model="notif.approved" />
              </div>
              <div class="flex items-center justify-between py-4">
                <div>
                  <div class="text-sm font-medium text-slate-700">Claim rejected</div>
                  <div class="text-xs text-slate-400 mt-0.5">Notify the claimant when their claim is rejected</div>
                </div>
                <ToggleSwitch v-model="notif.rejected" />
              </div>
              <div class="flex items-center justify-between py-4">
                <div>
                  <div class="text-sm font-medium text-slate-700">Budget threshold alerts (80%)</div>
                  <div class="text-xs text-slate-400 mt-0.5">Alert when a project reaches 80% of its budget</div>
                </div>
                <ToggleSwitch v-model="notif.budget" />
              </div>
            </div>
          </div>
        </TabPanel>

        <!-- Fund Rules -->
        <TabPanel value="2">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
            <!-- FCRA Rules -->
            <div class="bg-white rounded-2xl border border-violet-100 shadow-sm p-6">
              <div class="flex items-center gap-2 mb-4">
                <div class="w-8 h-8 rounded-lg bg-violet-100 flex items-center justify-center">
                  <i class="pi pi-shield text-violet-600 text-sm"></i>
                </div>
                <h2 class="text-base font-bold text-slate-800">FCRA Compliance Rules</h2>
              </div>
              <ul class="flex flex-col gap-3">
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-violet-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Funds must be utilised for the specific purpose stated to the donor.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-violet-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Form 15CA/15CB required for all foreign outward remittances above Rs 5 lakh.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-violet-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Annual return to be filed with MHA in Form FC-4 by 31st December.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-violet-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Admin expenditure capped at 20% of total FCRA receipts.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-violet-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Maintain separate FCRA bank account; no commingling with local funds.
                </li>
              </ul>
            </div>

            <!-- Local Fund Rules -->
            <div class="bg-white rounded-2xl border border-emerald-100 shadow-sm p-6">
              <div class="flex items-center gap-2 mb-4">
                <div class="w-8 h-8 rounded-lg bg-emerald-100 flex items-center justify-center">
                  <i class="pi pi-building text-emerald-600 text-sm"></i>
                </div>
                <h2 class="text-base font-bold text-slate-800">Local Fund Rules</h2>
              </div>
              <ul class="flex flex-col gap-3">
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-emerald-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Utilisation flexibility up to 10% reallocation between budget heads without donor approval.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-emerald-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Internal audit mandatory for expenses exceeding Rs 1 lakh per claim.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-emerald-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Annual statutory audit report to be submitted to the board by 30th September.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-emerald-500 text-xs mt-0.5 flex-shrink-0"></i>
                  All cash payments above Rs 10,000 require Finance Manager sign-off.
                </li>
                <li class="flex items-start gap-2 text-sm text-slate-600">
                  <i class="pi pi-check-circle text-emerald-500 text-xs mt-0.5 flex-shrink-0"></i>
                  Vendor empanelment required for recurring vendors before payment processing.
                </li>
              </ul>
            </div>
          </div>
        </TabPanel>
      </TabPanels>
    </Tabs>
  </div>
</template>

<script>
export default {
  name: 'SettingsView',
  data() {
    return {
      orgName: 'My NGO',
      fyStart: 'april',
      fyOptions: [
        { label: 'April (Indian FY)', value: 'april' },
        { label: 'January (Calendar)', value: 'january' },
      ],
      notif: {
        submitted: true,
        approved: true,
        rejected: true,
        budget: false,
      },
    }
  },
  methods: {
    saveSettings() {
      // Save logic here
    },
  },
}
</script>
