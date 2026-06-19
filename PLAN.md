# Stacks — Gen Z Personal Finance App

## Vision
Your everyday financial companion — spend smarter, save consistently, invest confidently, build lifelong money habits.

## V1 — Foundation ✅ (Current Build)
- **Home Dashboard** — Financial health score, income/spend/savings summary, spending donut chart, recent transactions, goals + budget preview
- **Spend Tracker** — Log expenses by category (Food, Cafes, Shopping, Travel, Subscriptions, Entertainment, Rent, Health, Misc), search + filter, monthly summary
- **Earn** — Income tracking (Salary, Freelance, Stipend, Side Hustle, Gifts, Refunds), cash flow view, income source breakdown
- **Goals** — Savings goals with circular progress (MacBook, Trip, Emergency Fund), deadline countdown, completion celebrations
- **Budget Planner** — Per-category limits, color-coded progress bars, overspend alerts, 50/30/20 tip
- **Subscription Tracker** — All recurring bills, renewal countdowns, annual cost projection, "renewing soon" alerts
- **Quick Add** — Global floating modal (amount → category → note → save) accessible from anywhere
- **Financial Health Score** — 84/100 style composite score shown in top bar

## V2 — Growth Layer 📋 (Next Phase)
- **Investment Starter Hub** — Mutual Funds, SIPs, Index Funds, ETFs, Gold, PPF, NPS. Learn + simulate, not trade. AI-matched to your savings rate.
- **Financial Learning Hub** — Short Duolingo-style lessons: Budgeting, Credit Cards, UPI Safety, Income Tax (India), Emergency Funds, Insurance, Inflation
- **Challenges & Gamification** — No-Spend Weekend, Save ₹100 Daily, 30-Day Budget Challenge. XP + Badges + Streaks + Levels
- **Wishlist Planner** — Save items (Phone, Laptop, Trip), estimate months to save, monthly contribution needed
- **Financial Calendar** — Upcoming bills, SIP dates, subscription renewals, salary day, goal milestones
- **Weekly & Monthly Reports** — Auto-generated summaries, month-over-month comparison, category trends
- **Smart Insights** — "You spend ₹2,400/month on coffee", "Cut food delivery 20% = save ₹28k/year", pattern detection

## V3 — AI & Integrations 💡 (Future)
- **AI Money Coach** — "Can I afford a ₹25,000 phone?", predict expenses, suggest budgets, warn about overspending
- **Bank / UPI Sync** — Auto-import transactions
- **SMS Expense Detection** — Parse bank SMS for auto-logging
- **AI Receipt Scanning / OCR** — Snap and log
- **Portfolio Tracking** — See all investments in one place
- **Credit Score Insights** — Monitor + improve score
- **Personalized Investment Recommendations** — Based on income, savings rate, risk profile

## Tech Stack
- Vue 3 + Vuex + Vue Router 4
- PrimeVue 4 (UI components)
- Tailwind CSS 4
- ApexCharts (vue3-apexcharts)
- Django 5.2 backend (SQLite dev)
- Vite 6

## Design Principles
- Mobile-first, minimal, Gen Z aesthetic
- Emoji-forward category icons
- Gamified (scores, streaks, goals)
- Zero accounting jargon
- Feels like CRED + Duolingo + Splitwise — not QuickBooks
- Indian Rupee (₹) throughout

## Category Colors
- Food: #f59e0b  |  Cafes: #8b5cf6  |  Shopping: #ec4899
- Travel: #3b82f6  |  Subscriptions: #10b981  |  Entertainment: #f43f5e
- Rent: #6b7280  |  Health: #14b8a6  |  Misc: #a78bfa
