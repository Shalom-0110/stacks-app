<template>
  <div class="layout-wrapper">
    <!-- Sidebar -->
    <aside class="layout-sidebar" :class="{ 'layout-sidebar-slim': collapsed }">

      <!-- Sidebar Header -->
      <div class="sidebar-header">
        <div class="brand-row">
          <div class="brand-icon">💸</div>
          <span class="brand-name menu-text">Dosh</span>
        </div>
        <button class="collapse-btn" @click="collapsed = !collapsed" :title="collapsed ? 'Expand' : 'Collapse'">
          <i :class="collapsed ? 'pi pi-angle-double-right' : 'pi pi-angle-double-left'"></i>
        </button>
      </div>

      <!-- Nav -->
      <nav class="sidebar-nav">

        <!-- My Money -->
        <div class="nav-section">
          <span class="nav-section-label menu-text">My Money</span>
          <router-link to="/" class="nav-item" active-class="nav-active" exact>
            <i class="pi pi-home"></i>
            <span class="menu-text">Home</span>
          </router-link>
          <router-link to="/spend" class="nav-item" active-class="nav-active">
            <i class="pi pi-credit-card"></i>
            <span class="menu-text">Spend</span>
          </router-link>
          <router-link to="/earn" class="nav-item" active-class="nav-active">
            <i class="pi pi-arrow-circle-down"></i>
            <span class="menu-text">Earn</span>
          </router-link>
        </div>

        <hr class="nav-divider">

        <!-- My Plans -->
        <div class="nav-section">
          <span class="nav-section-label menu-text">My Plans</span>
          <router-link to="/goals" class="nav-item" active-class="nav-active">
            <i class="pi pi-flag"></i>
            <span class="menu-text">Goals</span>
          </router-link>
          <router-link to="/budget" class="nav-item" active-class="nav-active">
            <i class="pi pi-sliders-h"></i>
            <span class="menu-text">Budget</span>
          </router-link>
          <router-link to="/subscriptions" class="nav-item" active-class="nav-active">
            <i class="pi pi-sync"></i>
            <span class="menu-text">Subscriptions</span>
          </router-link>
        </div>

        <hr class="nav-divider">

        <!-- Level Up -->
        <div class="nav-section">
          <span class="nav-section-label menu-text">Level Up</span>
          <router-link to="/invest" class="nav-item nav-soon" active-class="nav-active">
            <i class="pi pi-chart-line"></i>
            <span class="menu-text">Invest</span>
            <span class="soon-badge menu-text">Soon</span>
          </router-link>
          <router-link to="/learn" class="nav-item nav-soon" active-class="nav-active">
            <i class="pi pi-book"></i>
            <span class="menu-text">Learn</span>
            <span class="soon-badge menu-text">Soon</span>
          </router-link>
          <router-link to="/challenges" class="nav-item nav-soon" active-class="nav-active">
            <i class="pi pi-trophy"></i>
            <span class="menu-text">Challenges</span>
            <span class="soon-badge menu-text">Soon</span>
          </router-link>
        </div>

      </nav>

      <!-- Sidebar Footer -->
      <div class="sidebar-footer">
        <div class="user-avatar-circle">E</div>
        <div class="footer-user-info menu-text">
          <span class="footer-user-name">Eirene</span>
          <span class="footer-user-role">secure the bag 💜</span>
        </div>
        <a href="/logout/" class="logout-btn" title="Logout">
          <i class="pi pi-sign-out"></i>
        </a>
      </div>

    </aside>

    <!-- Main Body -->
    <div class="layout-body">

      <!-- Top Bar -->
      <header class="top-bar">
        <div class="top-bar-left">
          <h2 class="top-bar-title">{{ $route.meta.title || 'Dosh' }}</h2>
        </div>
        <div class="top-bar-right">
          <GlobalSearch />
          <div class="health-score-chip">
            <i class="pi pi-heart-fill"></i>
            <span>84</span>
          </div>
          <button class="top-btn" @click="showAdd = true">
            <i class="pi pi-plus"></i>
          </button>
          <div class="top-avatar">AK</div>
        </div>
      </header>

      <!-- Page Content -->
      <main class="page-content">
        <router-view v-slot="{ Component }">
          <transition name="page-fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>

    </div>

    <!-- Quick Add Overlay -->
    <div v-if="showAdd" class="quick-add-overlay" @click.self="showAdd = false">
      <div class="quick-add-card">

        <!-- Header -->
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
          <h3 style="margin:0;font-size:1.1rem;font-weight:800;color:#1e1b2e;">Quick Add 💸</h3>
          <button @click="showAdd = false" style="background:none;border:none;cursor:pointer;color:#94a3b8;font-size:1.2rem;display:flex;align-items:center;padding:4px;">
            <i class="pi pi-times"></i>
          </button>
        </div>

        <!-- Amount -->
        <div style="margin-bottom:20px;">
          <label style="display:block;font-size:0.75rem;font-weight:700;color:#64748b;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">Amount (₹)</label>
          <input
            class="quick-amount-input"
            type="number"
            v-model="addForm.amount"
            placeholder="0"
          />
        </div>

        <!-- Category Grid -->
        <div style="margin-bottom:20px;">
          <label style="display:block;font-size:0.75rem;font-weight:700;color:#64748b;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">Category</label>
          <div class="cat-grid">
            <button
              v-for="cat in categories"
              :key="cat.id"
              class="cat-chip"
              :class="{ 'cat-chip-active': addForm.category === cat.id }"
              @click="addForm.category = cat.id"
              type="button"
            >
              <span>{{ cat.icon }}</span>
              <span style="font-size:0.7rem;font-weight:600;color:#475569;line-height:1.2;">{{ cat.label }}</span>
            </button>
          </div>
        </div>

        <!-- Note -->
        <div style="margin-bottom:24px;">
          <label style="display:block;font-size:0.75rem;font-weight:700;color:#64748b;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">Note</label>
          <input
            class="quick-note-input"
            v-model="addForm.note"
            placeholder="What was this for?"
          />
        </div>

        <!-- Submit -->
        <button
          @click="submitAdd"
          :disabled="!addForm.amount || !addForm.category"
          style="width:100%;padding:12px;background:#7c3aed;color:white;border:none;border-radius:12px;font-size:0.9rem;font-weight:700;cursor:pointer;transition:background 0.15s;"
          :style="(!addForm.amount || !addForm.category) ? 'opacity:0.5;cursor:not-allowed;' : ''"
        >
          Add Expense ✓
        </button>

      </div>
    </div>

  </div>
</template>

<script>
import { CATEGORIES } from '@/mockData.js'

export default {
  name: 'App',
  data() {
    return {
      collapsed: false,
      showAdd: false,
      categories: CATEGORIES,
      addForm: {
        amount: '',
        category: '',
        note: '',
      },
    }
  },
  methods: {
    submitAdd() {
      // Reset form and close modal
      this.addForm = { amount: '', category: '', note: '' }
      this.showAdd = false
    },
  },
}
</script>

<style scoped>
/* ── Sidebar Header ── */
.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 14px 14px;
  flex-shrink: 0;
}

.brand-row {
  display: flex;
  align-items: center;
  gap: 10px;
  overflow: hidden;
}

.brand-icon {
  width: 34px;
  height: 34px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.brand-name {
  color: white;
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.3px;
  white-space: nowrap;
}

.collapse-btn {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
  padding: 6px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, color 0.15s;
  flex-shrink: 0;
}
.collapse-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

/* ── Nav ── */
.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 4px 0;
}
.sidebar-nav::-webkit-scrollbar {
  width: 3px;
}
.sidebar-nav::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.nav-section {
  margin-bottom: 4px;
}

.nav-divider {
  border: none;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin: 8px 0;
}

.nav-section-label {
  display: block;
  color: rgba(255, 255, 255, 0.45);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 12px 22px 4px;
  white-space: nowrap;
  overflow: hidden;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 9px 14px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.15s;
  margin: 2px 8px;
  white-space: nowrap;
}
.nav-item .pi {
  font-size: 0.95rem;
  flex-shrink: 0;
}
.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}
.nav-active {
  background: white !important;
  color: #6d28d9 !important;
  font-weight: 700;
}

.nav-soon {
  opacity: 0.65;
}

.soon-badge {
  margin-left: auto;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.15);
  color: rgba(255, 255, 255, 0.7);
  border-radius: 4px;
  padding: 2px 5px;
  flex-shrink: 0;
}

/* ── Sidebar Footer ── */
.sidebar-footer {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 14px 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
  overflow: hidden;
}

.user-avatar-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 700;
  flex-shrink: 0;
}

.footer-user-info {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.footer-user-name {
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.footer-user-role {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.7rem;
  white-space: nowrap;
}

.logout-btn {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  padding: 6px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, color 0.15s;
  text-decoration: none;
  flex-shrink: 0;
}
.logout-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

/* ── Layout Body ── */
.layout-body {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  overflow: hidden !important;
  min-width: 0;
}

/* ── Top Bar ── */
.top-bar {
  height: 58px;
  background: white;
  border-bottom: 1px solid #f0edff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 28px;
  flex-shrink: 0;
}

.top-bar-left,
.top-bar-right {
  display: flex;
  align-items: center;
}
.top-bar-left {
  gap: 12px;
}
.top-bar-right {
  gap: 10px;
}

.top-bar-title {
  font-size: 1rem;
  font-weight: 700;
  color: #1e1b2e;
  margin: 0;
}

.health-score-chip {
  display: flex;
  align-items: center;
  gap: 5px;
  background: #fdf2f8;
  border: 1px solid #fce7f3;
  border-radius: 9999px;
  padding: 4px 10px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #be185d;
}

.top-btn {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #7c3aed;
  border: none;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  transition: background 0.15s;
}
.top-btn:hover {
  background: #6d28d9;
}

.top-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7c3aed, #ec4899);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 700;
}

/* ── Page Content ── */
.page-content {
  flex: 1 !important;
  overflow-y: auto !important;
  background: #faf9ff;
  padding: 24px 32px;
}

/* ── Quick Add Overlay ── */
.quick-add-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 10, 31, 0.55);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.quick-add-card {
  background: white;
  border-radius: 24px;
  padding: 28px;
  width: 100%;
  max-width: 420px;
  box-shadow: 0 20px 60px -10px rgba(109, 40, 217, 0.3);
}

.quick-amount-input {
  width: 100%;
  font-size: 2rem;
  font-weight: 800;
  color: #1e1b2e;
  border: none;
  border-bottom: 2px solid #e5e7eb;
  outline: none;
  padding: 4px 0;
  background: transparent;
  transition: border-color 0.15s;
  box-sizing: border-box;
}
.quick-amount-input:focus {
  border-color: #7c3aed;
}

.quick-note-input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.875rem;
  outline: none;
  transition: border-color 0.15s;
  box-sizing: border-box;
}
.quick-note-input:focus {
  border-color: #7c3aed;
}

.cat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.cat-chip {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 10px 6px;
  border-radius: 12px;
  border: 1.5px solid #e5e7eb;
  background: transparent;
  cursor: pointer;
  transition: all 0.15s;
  font-size: 1.2rem;
}
.cat-chip:hover {
  border-color: #c4b5fd;
  background: #f5f3ff;
}
.cat-chip-active {
  border-color: #7c3aed !important;
  background: #f5f3ff !important;
  color: #6d28d9 !important;
}

/* ── Page Transition ── */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.18s ease, transform 0.18s ease;
}
.page-fade-enter-from {
  opacity: 0;
  transform: translateY(6px);
}
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>

<style>
/* ── Global Layout ── */
:root {
  --sidebar-width: 260px;
  --sidebar-collapsed-width: 45px;
}

.layout-wrapper {
  display: flex !important;
  flex-direction: row !important;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.layout-sidebar {
  background: linear-gradient(160deg, #6d28d9 0%, #4c1d95 100%) !important;
  width: var(--sidebar-width);
  height: 100vh;
  display: flex !important;
  flex-direction: column !important;
  transition: width 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
  overflow: hidden;
  position: relative !important;
}

.layout-sidebar-slim {
  width: var(--sidebar-collapsed-width) !important;
}

.layout-sidebar-slim .menu-text {
  display: none !important;
}
.layout-sidebar-slim .nav-section-label {
  display: none !important;
}
.layout-sidebar-slim .nav-item {
  justify-content: center !important;
  padding: 9px !important;
  margin: 2px 4px !important;
}
.layout-sidebar-slim .sidebar-header {
  justify-content: center !important;
  padding: 18px 6px 14px !important;
}
.layout-sidebar-slim .brand-row {
  display: none !important;
}
.layout-sidebar-slim .sidebar-footer {
  justify-content: center !important;
  padding: 12px 0 !important;
}
.layout-sidebar-slim .collapse-btn {
  margin: 0 auto !important;
}
</style>
