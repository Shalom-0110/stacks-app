import {deleteRequest, getRequest, getUrl, postRequest} from "./network";
import Types from "./types.js";

export default {
  async getUser({ commit }) {
    const url = getUrl("user/me");
    const response = await getRequest(url);
    commit(Types.SET_USER, response);
  },

  async listUser() {
    const url = getUrl("user");
    return await getRequest(url);
  },

  async login(ctx, credentials) {
    const url = getUrl("token-login");
    return await postRequest(url, credentials);
  },

  async logout() {
    const url = getUrl("logout");
    await postRequest(url);
    window.location.href = "/login/";
  },

  async importTaskAndBudget(ctx, formData) {
    const url = getUrl("import-task-and-budget");
    return await postRequest(url, formData);
  },

  async importExpenseClaim(ctx, formData) {
    const url = getUrl("import-expense-claim");
    return await postRequest(url, formData);
  },

  async importMultiExpenseClaimLineItem(ctx, formData) {
    const url = getUrl("import-multi-expense-claim-line-item");
    return await postRequest(url, formData);
  },

  async refreshMasters(ctx) {
    const url = getUrl("refresh-masters");
    return await postRequest(url);
  },

  async deleteReviewSheetAttachment(ctx, {id, formData}) {
    const url = getUrl(`review-sheet/${id}/delete-attachment`);
    return await postRequest(url, formData);
  },

  async fetchClaimReversal(ctx, id) {
    const url = getUrl(`claim-reversals/${id}`);
    return await getRequest(url);
  },

  async addMultiExpenseCreditAccount(ctx, {id, formData}) {
    const url = getUrl(`multi-expense-claim/${id}/update-credit-account`);
    return await postRequest(url, formData);
  },

  async fetchReminder(ctx, id) {
    const url = getUrl(`reminders/${id}`);
    return await getRequest(url);
  },

  async execRemindersDryRun(ctx, id) {
    const url = getUrl(`reminders/${id}/exec-dry-run`);
    return await postRequest(url);
  },
};
