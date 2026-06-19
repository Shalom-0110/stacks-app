<template>
  <div class="mb-5">
    <div>
      <div class="mb-5 flex items-center space-x-2">
        <label for="switchToggle">Apply TDS</label>
        <ToggleSwitch
          id="switchToggle"
          v-model="isActive"/>
      </div>
      <div
        v-if="isActive"
        class="grid grid-cols-[repeat(auto-fill,_minmax(300px,_1fr))] gap-4 mb-4">
        <div class="">
          <label
            for="tds"
            class="mb-1 block">Income Tax Section</label>
          <AutoComplete
            :value="modelValue.tds"
            name="tds__ac"
            option-label="section"
            :suggestions="tdsFiltered"
            fluid
            :invalid="errors.tds"
            placeholder="Income Tax Section"
            input-id="tds"
            @item-select="notifyModelChange('tds', $event.value)"
            @complete="tdsSearch"/>
          <input
            type="hidden"
            name="tds"
            :value="modelValue.tds?.id">
          <input
            id="tds__ackey"
            type="hidden"
            name="tds__ackey"
            value="id">
          <Message
            v-if="errors.tds"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.tds.join(" ") }}
          </Message>
        </div>
        <div class="">
          <label
            for="base_amount"
            class="mb-1 block">Base Amount for TDS</label>
          <InputNumber
            :model-value="modelValue.base_amount"
            name="base_amount"
            type="number"
            placeholder="Base Amount for TDS"
            fluid
            :invalid="errors.base_amount"
            :use-grouping="false"
            input-id="base_amount"
            inputmode="decimal"
            :step="0.01"
            :max-fraction-digits="2"
            @input="notifyModelChange('base_amount', $event.value)"/>

          <Message
            v-if="errors.base_amount"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.base_amount.join(" ") }}
          </Message>
        </div>
        <div class="">
          <label
            for="tds_account"
            class="mb-1 block">TDS Account</label>
          <AutoComplete
            :value="modelValue.tds_account"
            name="tds_account__ac"
            option-label="name"
            :suggestions="tds_accountFiltered"
            fluid
            :invalid="errors.tds_account"
            placeholder="TDS Account"
            input-id="tds_account"
            @item-select="notifyModelChange('tds_account', $event.value)"
            @complete="tds_accountSearch"/>
          <input
            type="hidden"
            name="tds_account"
            :value="modelValue.tds_account?.id">
          <input
            id="tds_account__ackey"
            type="hidden"
            name="tds_account__ackey"
            value="id">
          <Message
            v-if="errors.tds_account"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.tds_account.join(" ") }}
          </Message>
        </div>
        <div class="">
          <label
            for="pan_number"
            class="mb-1 block">PAN Number</label>
          <InputText
            :model-value="panNumberDisplay"
            readonly="readonly"
            name="pan_number"
            type="text"
            placeholder="PAN Number"
            fluid
            :invalid="errors.pan_number"
            input-id="pan_number"/>
          <Message
            v-if="errors.pan_number"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.pan_number.join(" ") }}
          </Message>
        </div>
        <div class="">
          <label
            for="tds_amount"
            class="mb-1 block">TDS Amount</label>
          <InputNumber
            :model-value="modelValue.tds_amount"
            readonly="readonly"
            name="tds_amount"
            type="number"
            placeholder="TDS Amount"
            fluid
            :invalid="errors.tds_amount"
            :use-grouping="false"
            input-id="tds_amount"
            inputmode="decimal"
            :step="0.01"
            :max-fraction-digits="2"/>

          <Message
            v-if="errors.tds_amount"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.tds_amount.join(" ") }}
          </Message>
        </div>
        <div class="">
          <label
            for="tds_rate"
            class="mb-1 block">TDS Rate</label>
          <InputText
            :model-value="tdsRateDisplay"
            readonly="readonly"
            name="tds_rate_display"
            placeholder="TDS Rate"
            fluid
            :invalid="errors.tds_rate"
            :use-grouping="false"
            input-id="tds_rate_display"/>
          <input
            type="hidden"
            name="tds_rate"
            :value="modelValue.tds_rate">
          <Message
            v-if="errors.tds_rate"
            severity="error"
            size="small"
            variant="simple"
            class="pt-2">
            {{ errors.tds_rate.join(" ") }}
          </Message>
        </div>
      </div>
      <div
        v-if="isActive && showPanInfoMessage">
        <div
          class="flex items-center p-5 w-1/1"
          :class="background">
          <i
            :class="icon"
            class="mr-6"
            style="font-size: 3rem;"/>

          <div
            class="flex items-center justify-between w-1/1">
            <div>
              <div class="text-xl font-bold">
                PAN not configured for Vendor or User
              </div>
              <div>
                Please update PAN details in the master and refresh the screen.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ToggleSwitch from 'primevue/toggleswitch';
import {getRequest} from "@/components.gen/assets/network.js";

export default {
  name: "TDSForm",
  props: {
    modelValue: {
      type: Object,
      required: true,
    },
    errors: {
      type: Object,
      required: true,
    },
  },
  emits: ['update:modelValue'],
  data() {
    return {
      isActive: false,
      tds_accountFiltered: [],
      tdsFiltered: [],
    };
  },
  computed: {
    icon() {
      return "pi pi-info-circle";
    },
    background() {
      return 'bg-green-50 text-green-700';
    },
    tdsRateDisplay() {
      if (this.modelValue.tds_rate) {
        const v = parseFloat(this.modelValue.tds_rate) * 100;
        return v.toString() + "%";
      }
      return '';
    },
    panNumberDisplay() {
      let obj = this.modelValue;
      if (obj.expense_claim) {
        obj = obj.expense_claim;
      }

      if (obj.vendor) {
        return obj.vendor.pan_number;
      } else if (obj.user) {
        return obj.user.pan_number;
      }

      return '';
    },
    showPanInfoMessage() {
      let obj = this.modelValue;

      if (obj.expense_claim) {
        obj = obj.expense_claim;
      }

      return !(
        (obj.vendor && obj.vendor.pan_number) ||
        (obj.user && obj.user.pan_number)
      );
    }
  },
  methods: {
    notifyModelChange(name, value) {
      const obj = {...this.modelValue};
      obj[name] = value;
      if (name === 'tds') {
        obj["tds_rate"] = value?.rate || 0;
        this.$emit('update:modelValue', obj);
      } else if (name === 'base_amount') {
        const baseAmt = parseFloat(value);
        if (Number.isFinite(baseAmt) && !Number.isNaN(baseAmt) && this.modelValue.tds_rate) {
          obj["tds_amount"] = Math.ceil(baseAmt * this.modelValue.tds_rate);
          this.$emit('update:modelValue', obj);
        }
      } else {
        this.$emit('update:modelValue', obj);
      }
    },
    async tdsSearch(event) {
      try {
        if (event.query.trim().length) {
          const query = new URLSearchParams();
          query.append("search", event.query.trim());
          if (this.autocompleteInject?.tds) {
            Object.keys(this.autocompleteInject.tds).forEach((key) => {
              query.append(key, this.autocompleteInject.tds[key]);
            });
          }
          const response = await getRequest("/api/v1/tds/", query);
          this.tdsFiltered = response?.results || [];
        }
      } catch (e) {
        console.error(e);
      }
    },
    async tds_accountSearch(event) {
      try {
        if (event.query.trim().length) {
          const query = new URLSearchParams();
          query.append("search", event.query.trim());
          if (this.autocompleteInject?.tds_account) {
            Object.keys(this.autocompleteInject.tds_account).forEach((key) => {
              query.append(key, this.autocompleteInject.tds_account[key]);
            });
          }
          const response = await getRequest("/api/v1/chart-of-accounts/", query);
          this.tds_accountFiltered = response?.results || [];
        }
      } catch (e) {
        this.$toast.add({
          severity: "error",
          summary: "Error",
          detail: e.data,
          life: 3000,
        });
      }
    },

  },
};
</script>
