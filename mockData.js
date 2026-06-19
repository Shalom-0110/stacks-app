export const CATEGORIES = [
  { id: 'food',     label: 'Food & Dining',  icon: '🍜', color: '#f59e0b' },
  { id: 'cafe',     label: 'Cafes',          icon: '☕', color: '#8b5cf6' },
  { id: 'shopping', label: 'Shopping',       icon: '🛍️', color: '#ec4899' },
  { id: 'travel',   label: 'Travel',         icon: '✈️', color: '#3b82f6' },
  { id: 'subs',     label: 'Subscriptions',  icon: '📱', color: '#10b981' },
  { id: 'entertain',label: 'Entertainment',  icon: '🎬', color: '#f43f5e' },
  { id: 'rent',     label: 'Rent & Bills',   icon: '🏠', color: '#6b7280' },
  { id: 'health',   label: 'Health',         icon: '💊', color: '#14b8a6' },
  { id: 'misc',     label: 'Miscellaneous',  icon: '💸', color: '#a78bfa' },
]

export const EXPENSES = [
  { id: 1,  title: 'Zomato Order',      category: 'food',     amount: 345,   date: '2024-11-20', note: 'Dinner with Siya' },
  { id: 2,  title: 'Blue Tokai Coffee', category: 'cafe',     amount: 180,   date: '2024-11-20', note: 'Morning fix' },
  { id: 3,  title: 'H&M',               category: 'shopping', amount: 2400,  date: '2024-11-19', note: '' },
  { id: 4,  title: 'Uber',              category: 'travel',   amount: 210,   date: '2024-11-19', note: 'Office' },
  { id: 5,  title: 'Netflix',           category: 'subs',     amount: 649,   date: '2024-11-18', note: '' },
  { id: 6,  title: 'PVR Tickets',       category: 'entertain',amount: 500,   date: '2024-11-17', note: 'Interstellar rerun' },
  { id: 7,  title: 'Rent',              category: 'rent',     amount: 12000, date: '2024-11-01', note: 'November' },
  { id: 8,  title: 'Swiggy Instamart',  category: 'food',     amount: 890,   date: '2024-11-16', note: 'Groceries' },
  { id: 9,  title: 'Spotify',           category: 'subs',     amount: 119,   date: '2024-11-15', note: '' },
  { id: 10, title: 'Amazon Order',      category: 'shopping', amount: 1200,  date: '2024-11-14', note: 'Books + earbuds' },
  { id: 11, title: 'Rapido',            category: 'travel',   amount: 95,    date: '2024-11-14', note: '' },
  { id: 12, title: 'Pharmacy',          category: 'health',   amount: 380,   date: '2024-11-13', note: '' },
  { id: 13, title: 'Boba & Bowls',      category: 'cafe',     amount: 320,   date: '2024-11-12', note: 'Study session' },
  { id: 14, title: 'ChatGPT Plus',      category: 'subs',     amount: 1699,  date: '2024-11-10', note: '' },
  { id: 15, title: 'Electricity Bill',  category: 'rent',     amount: 1200,  date: '2024-11-05', note: '' },
]

export const INCOME = [
  { id: 1, title: 'Salary',            amount: 45000, date: '2024-11-01', type: 'salary',   icon: '💼' },
  { id: 2, title: 'Freelance Project', amount: 8000,  date: '2024-11-10', type: 'freelance',icon: '💻' },
  { id: 3, title: 'Gift from parents', amount: 3000,  date: '2024-11-12', type: 'gift',     icon: '🎁' },
  { id: 4, title: 'Cashback refund',   amount: 200,   date: '2024-11-18', type: 'refund',   icon: '💰' },
]

export const GOALS = [
  { id: 1, title: 'MacBook Pro',    target: 150000, saved: 45000, emoji: '💻', deadline: '2025-06-01', color: '#7c3aed' },
  { id: 2, title: 'Goa Trip',       target: 25000,  saved: 12000, emoji: '🌊', deadline: '2025-02-15', color: '#0ea5e9' },
  { id: 3, title: 'Emergency Fund', target: 100000, saved: 30000, emoji: '🛡️', deadline: null,         color: '#10b981' },
  { id: 4, title: 'New iPhone 16',  target: 90000,  saved: 90000, emoji: '📱', deadline: '2024-12-25', color: '#f59e0b' },
]

export const BUDGETS = [
  { category: 'food',     limit: 8000, spent: 4230 },
  { category: 'cafe',     limit: 2000, spent: 1580 },
  { category: 'shopping', limit: 5000, spent: 3600 },
  { category: 'travel',   limit: 3000, spent: 1240 },
  { category: 'subs',     limit: 2000, spent: 768  },
  { category: 'entertain',limit: 2500, spent: 500  },
]

export const SUBSCRIPTIONS = [
  { id: 1, name: 'Netflix',      amount: 649,  icon: '🎬', color: '#ef4444', nextDate: '2024-12-18' },
  { id: 2, name: 'Spotify',      amount: 119,  icon: '🎵', color: '#22c55e', nextDate: '2024-12-15' },
  { id: 3, name: 'ChatGPT Plus', amount: 1699, icon: '🤖', color: '#8b5cf6', nextDate: '2024-12-20' },
  { id: 4, name: 'Prime Video',  amount: 299,  icon: '📦', color: '#f59e0b', nextDate: '2025-01-05' },
  { id: 5, name: 'Google One',   amount: 130,  icon: '☁️', color: '#3b82f6', nextDate: '2024-12-22' },
  { id: 6, name: 'Apple Music',  amount: 99,   icon: '🎵', color: '#fb7185', nextDate: '2024-12-10' },
]

export const MONTHLY = {
  income: 56200,
  expenses: 21987,
  savings: 34213,
  savingsRate: 61,
  healthScore: 84,
  prevExpenses: 26400,
  prevSavings: 29000,
}

export const MONTHLY_SPEND_CHART = {
  labels: ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
  income:   [42000, 45000, 43000, 48000, 52000, 56200],
  expenses: [28000, 31000, 27000, 24000, 26400, 21987],
}

export const CAT_MAP = Object.fromEntries(
  CATEGORIES.map(c => [c.id, c])
)
