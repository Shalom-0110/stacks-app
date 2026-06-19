<template>
  <div class="p-6 max-w-2xl mx-auto">
    <!-- Header -->
    <div class="flex items-center gap-3 mb-6">
      <h1 class="text-2xl font-black text-slate-800">Challenges</h1>
      <div class="flex gap-2">
        <span class="bg-gradient-to-r from-amber-500 to-orange-500 text-white text-sm font-bold px-3 py-1 rounded-full">
          🏆 Level Up
        </span>
        <span class="bg-slate-100 text-slate-500 text-sm font-semibold px-3 py-1 rounded-full">
          Coming in V2
        </span>
      </div>
    </div>

    <!-- Intro Card -->
    <div class="bg-gradient-to-br from-amber-500 to-orange-600 rounded-3xl p-8 text-white mb-6">
      <div class="text-5xl mb-3">🔥</div>
      <h2 class="text-2xl font-black mb-2">Build streaks. Earn XP. Level up.</h2>
      <p class="text-white/80">
        Gamified money challenges that make saving fun, and actually keep you accountable.
      </p>
    </div>

    <!-- Challenge Cards Grid -->
    <div class="grid grid-cols-2 gap-4 mb-8">
      <!-- No-Spend Weekend -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">🚫</div>
        <p class="font-bold text-slate-800">No-Spend Weekend</p>
        <p class="text-sm text-slate-500 mt-1">48 hours, zero non-essential spending</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          200 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>

      <!-- Skip One Coffee -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">☕</div>
        <p class="font-bold text-slate-800">Skip One Coffee</p>
        <p class="text-sm text-slate-500 mt-1">Save ₹180 today</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          50 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>

      <!-- Save ₹100 Daily -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">💰</div>
        <p class="font-bold text-slate-800">Save ₹100 Daily</p>
        <p class="text-sm text-slate-500 mt-1">30-day streak = ₹3,000 saved</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          150 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>

      <!-- Cook Instead -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">🍳</div>
        <p class="font-bold text-slate-800">Cook Instead</p>
        <p class="text-sm text-slate-500 mt-1">No food delivery for 7 days</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          300 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>

      <!-- App Detox -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">📱</div>
        <p class="font-bold text-slate-800">App Detox</p>
        <p class="text-sm text-slate-500 mt-1">No shopping apps for 3 days</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          100 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>

      <!-- Save First -->
      <div class="relative bg-white rounded-2xl border border-slate-100 shadow-sm p-5">
        <div class="text-2xl mb-2">💸</div>
        <p class="font-bold text-slate-800">Save First</p>
        <p class="text-sm text-slate-500 mt-1">Transfer savings before spending</p>
        <span class="inline-block bg-amber-100 text-amber-700 text-xs font-bold px-2 py-0.5 rounded-full mt-2">
          250 XP
        </span>
        <div class="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
          <span class="text-sm font-bold text-slate-500">🔒 Coming in V2</span>
        </div>
      </div>
    </div>

    <!-- Gamification Preview -->
    <div class="bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-2xl p-6">
      <p class="font-bold text-amber-800 mb-4">🏅 Earn rewards as you go</p>
      <div class="grid grid-cols-4 gap-4 text-center">
        <div>
          <div
            class="w-14 h-14 rounded-full bg-amber-100 flex items-center justify-center text-2xl mx-auto mb-2"
          >
            🔥
          </div>
          <p class="text-xs font-semibold text-amber-700">Saver</p>
        </div>
        <div>
          <div
            class="w-14 h-14 rounded-full bg-amber-100 flex items-center justify-center text-2xl mx-auto mb-2"
          >
            💎
          </div>
          <p class="text-xs font-semibold text-amber-700">Budget Master</p>
        </div>
        <div>
          <div
            class="w-14 h-14 rounded-full bg-amber-100 flex items-center justify-center text-2xl mx-auto mb-2"
          >
            🚀
          </div>
          <p class="text-xs font-semibold text-amber-700">Investor</p>
        </div>
        <div>
          <div
            class="w-14 h-14 rounded-full bg-amber-100 flex items-center justify-center text-2xl mx-auto mb-2"
          >
            ⚡
          </div>
          <p class="text-xs font-semibold text-amber-700">No-Spender</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChallengesView',
}
</script>
