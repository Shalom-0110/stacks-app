import { createStore } from "vuex";
import actions from "./actions";
import mutations from "./mutations";

const state = {
  user: {
    username: "",
    groups: [],
  },
};

const getters = {
  isBudgetManager: (state) => {
    return state.user.groups?.includes('Budget Manager');
  },

  isFinanceManager: (state) => {
    return state.user.groups?.includes('Finance Manager');
  },

  isStaff: (state) => {
    return state.user.groups?.includes('Staff');
  },

  currentUser: (state) => {
    return state.user.email;
  },
};


const store = createStore({
  state: state,
  actions: actions,
  mutations: mutations,
  getters: getters,
});

export default store;
