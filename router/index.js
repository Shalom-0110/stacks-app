import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', name: 'home', component: () => import('./views/Home.vue'), meta: { title: 'Home' } },
  { path: '/spend', name: 'spend', component: () => import('../views/Spend/SpendView.vue'), meta: { title: 'Spend' } },
  { path: '/earn', name: 'earn', component: () => import('../views/Earn/EarnView.vue'), meta: { title: 'Earn' } },
  { path: '/goals', name: 'goals', component: () => import('../views/Goals/GoalsView.vue'), meta: { title: 'Goals' } },
  { path: '/budget', name: 'budget', component: () => import('../views/Budget/BudgetView.vue'), meta: { title: 'Budget' } },
  { path: '/subscriptions', name: 'subscriptions', component: () => import('../views/Subs/SubsView.vue'), meta: { title: 'Subscriptions' } },
  { path: '/invest', name: 'invest', component: () => import('../views/Coming/InvestView.vue'), meta: { title: 'Invest' } },
  { path: '/learn', name: 'learn', component: () => import('../views/Coming/LearnView.vue'), meta: { title: 'Learn' } },
  { path: '/challenges', name: 'challenges', component: () => import('../views/Coming/ChallengesView.vue'), meta: { title: 'Challenges' } },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: () => import('../views/NotFoundView.vue'), meta: { title: 'Not Found' } },
]

const router = createRouter({
  history: createWebHistory('/'),
  scrollBehavior() { return { top: 0 } },
  routes,
})

router.beforeEach((to, _from, next) => {
  document.title = to.meta && to.meta.title ? to.meta.title + ' | Dosh' : 'Dosh'
  next()
})

export default router
