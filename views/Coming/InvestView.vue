<template>
  <div class="p-6 max-w-2xl mx-auto">
    <!-- Header -->
    <div class="flex items-center gap-3 mb-6">
      <h1 class="text-2xl font-black text-slate-800">Invest</h1>
      <span class="bg-slate-100 text-slate-500 text-sm font-semibold px-3 py-1 rounded-full">
        Coming in V2
      </span>
    </div>

    <!-- Hero Card -->
    <div class="bg-gradient-to-br from-violet-600 via-purple-600 to-indigo-700 rounded-3xl p-8 text-white mb-6">
      <div class="text-5xl mb-3">🚀</div>
      <h2 class="text-2xl font-black mb-2">Your money should work harder than you do.</h2>
      <p class="text-white/80 text-base mb-6">
        We're building the Investment Starter Hub, built for beginners who want to grow their money without the jargon.
      </p>

      <!-- Feature List -->
      <div class="grid grid-cols-2 gap-3 mb-6">
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          📈 Mutual Funds &amp; SIPs:start with ₹500
        </div>
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          🏆 Index Funds:the lazy genius way
        </div>
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          🪙 Gold ETFs:digital gold without the locker
        </div>
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          🏦 PPF &amp; NPS:tax-saving + retirement combo
        </div>
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          🤖 AI Picks:based on your savings rate
        </div>
        <div class="bg-white/10 rounded-2xl p-4 text-sm">
          📊 Portfolio Tracker:all in one place
        </div>
      </div>

      <!-- Notify Section -->
      <div class="mt-6 flex gap-3">
        <input
          type="email"
          placeholder="your@email.com"
          disabled
          class="bg-white/20 text-white placeholder:text-white/50 border border-white/30 rounded-xl px-4 py-2.5 text-sm outline-none flex-1"
        />
        <button
          disabled
          class="bg-white text-violet-700 font-bold rounded-xl px-5 py-2.5 text-sm disabled:opacity-60 cursor-not-allowed"
        >
          Notify me
        </button>
      </div>
    </div>

    <!-- Teaser Lesson Cards -->
    <div>
      <p class="font-bold text-slate-700 mb-4">Get a head start 📚</p>
      <div class="grid grid-cols-3 gap-4">
        <!-- Card 1 -->
        <div class="relative overflow-hidden rounded-2xl">
          <div class="bg-gradient-to-br from-emerald-400 to-teal-500 p-5 h-36 flex flex-col justify-end">
            <p class="font-bold text-white text-sm">Mutual Funds 101</p>
            <p class="text-white/80 text-xs mt-1">What they are &amp; how they grow</p>
          </div>
          <div class="absolute inset-0 bg-black/40 rounded-2xl flex items-center justify-center">
            <span class="text-white font-bold text-sm bg-black/50 rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="relative overflow-hidden rounded-2xl">
          <div class="bg-gradient-to-br from-violet-400 to-purple-500 p-5 h-36 flex flex-col justify-end">
            <p class="font-bold text-white text-sm">What is a SIP?</p>
            <p class="text-white/80 text-xs mt-1">Invest small, grow big</p>
          </div>
          <div class="absolute inset-0 bg-black/40 rounded-2xl flex items-center justify-center">
            <span class="text-white font-bold text-sm bg-black/50 rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="relative overflow-hidden rounded-2xl">
          <div class="bg-gradient-to-br from-amber-400 to-orange-500 p-5 h-36 flex flex-col justify-end">
            <p class="font-bold text-white text-sm">Index vs Active</p>
            <p class="text-white/80 text-xs mt-1">Which is better for you?</p>
          </div>
          <div class="absolute inset-0 bg-black/40 rounded-2xl flex items-center justify-center">
            <span class="text-white font-bold text-sm bg-black/50 rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InvestView',
}
</script>
