import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router/index.js";
import store from "@/store/index.js";

// PrimeVue + theme
import PrimeVue from "primevue/config";
import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura";
import ToastService from "primevue/toastservice";
import ConfirmationService from "primevue/confirmationservice";

// Charts
import VueApexCharts from "vue3-apexcharts";

// App components registered globally so every view can use them without importing
import Loading from "@/components/Loading.vue";
import PageTitle from "@/components/PageTitle.vue";
import SectionTitle from "@/components/SectionTitle.vue";
import Empty from "@/components/Empty.vue";
import GlobalSearch from "@/components/GlobalSearch.vue";

// Styles
import "@/styles/imports.css";
import "@/styles/style.scss";

/* ------------------------------------------------------------------
   Dosh theme — violet primary so every PrimeVue component matches
   the brand. tailwindcss-primeui maps --color-primary-* off this.
   ------------------------------------------------------------------ */
const DoshPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: "#f5f3ff",
      100: "#ede9fe",
      200: "#ddd6fe",
      300: "#c4b5fd",
      400: "#a78bfa",
      500: "#8b5cf6",
      600: "#7c3aed",
      700: "#6d28d9",
      800: "#5b21b6",
      900: "#4c1d95",
      950: "#2e1065",
    },
  },
});

const app = createApp(App);

// Register app-level components globally
app.component("Loading", Loading);
app.component("PageTitle", PageTitle);
app.component("SectionTitle", SectionTitle);
app.component("Empty", Empty);
app.component("GlobalSearch", GlobalSearch);

app.use(router);
app.use(store);
app.use(PrimeVue, {
  theme: {
    preset: DoshPreset,
    options: {
      darkModeSelector: ".dark",
      cssLayer: {
        name: "primevue",
        order: "theme, base, primevue",
      },
    },
  },
});
app.use(ToastService);
app.use(ConfirmationService);
app.use(VueApexCharts);
app.component("apexchart", VueApexCharts);

/* ------------------------------------------------------------------
   Register the PrimeVue components used as global tags across views
   (templates use <Select>, <DataTable> … without local imports).
   ------------------------------------------------------------------ */
const registerGlobals = async () => {
  const modules = {
    Button: () => import("primevue/button"),
    Select: () => import("primevue/select"),
    MultiSelect: () => import("primevue/multiselect"),
    DataTable: () => import("primevue/datatable"),
    Column: () => import("primevue/column"),
    ColumnGroup: () => import("primevue/columngroup"),
    Row: () => import("primevue/row"),
    Paginator: () => import("primevue/paginator"),
    Breadcrumb: () => import("primevue/breadcrumb"),
    InputText: () => import("primevue/inputtext"),
    InputNumber: () => import("primevue/inputnumber"),
    Textarea: () => import("primevue/textarea"),
    Checkbox: () => import("primevue/checkbox"),
    RadioButton: () => import("primevue/radiobutton"),
    Dialog: () => import("primevue/dialog"),
    Card: () => import("primevue/card"),
    Panel: () => import("primevue/panel"),
    Tag: () => import("primevue/tag"),
    Toast: () => import("primevue/toast"),
    ConfirmDialog: () => import("primevue/confirmdialog"),
    DatePicker: () => import("primevue/datepicker"),
    FileUpload: () => import("primevue/fileupload"),
    ProgressSpinner: () => import("primevue/progressspinner"),
    Menu: () => import("primevue/menu"),
    Avatar: () => import("primevue/avatar"),
    Divider: () => import("primevue/divider"),
    Message: () => import("primevue/message"),
    ToggleSwitch: () => import("primevue/toggleswitch"),
    IconField: () => import("primevue/iconfield"),
    InputIcon: () => import("primevue/inputicon"),
    ProgressBar: () => import("primevue/progressbar"),
    Tabs: () => import("primevue/tabs"),
    TabList: () => import("primevue/tablist"),
    Tab: () => import("primevue/tab"),
    TabPanels: () => import("primevue/tabpanels"),
    TabPanel: () => import("primevue/tabpanel"),
    Chip: () => import("primevue/chip"),
    Badge: () => import("primevue/badge"),
  };

  await Promise.all(
    Object.entries(modules).map(async ([name, loader]) => {
      try {
        const mod = await loader();
        app.component(name, mod.default);
      } catch (e) {
        // Component not installed — skip rather than block app mount.
        // eslint-disable-next-line no-console
        console.warn(`[Dosh] PrimeVue component "${name}" not registered:`, e?.message);
      }
    })
  );
};

registerGlobals().finally(() => {
  app.mount("#app");
});
