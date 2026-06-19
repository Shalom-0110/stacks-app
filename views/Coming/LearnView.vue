<template>
  <div class="p-6 max-w-2xl mx-auto">
    <!-- Header -->
    <div class="flex items-center gap-3 mb-6">
      <h1 class="text-2xl font-black text-slate-800">Learn</h1>
      <span class="bg-slate-100 text-slate-500 text-sm font-semibold px-3 py-1 rounded-full">
        Coming in V2
      </span>
    </div>

    <!-- Hero -->
    <div class="bg-gradient-to-br from-indigo-600 to-violet-700 rounded-3xl p-8 text-white mb-6">
      <div class="text-5xl mb-3">🧠</div>
      <h2 class="text-2xl font-black mb-2">Level up your money IQ</h2>
      <p class="text-white/80 mb-6">
        Short, engaging lessons. Built like Duolingo, not a finance textbook.
      </p>

      <!-- Topics List -->
      <div class="grid grid-cols-2 gap-2">
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          💳 Credit Cards &amp; Interest:don't get trapped
        </div>
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          📲 UPI Safety:protect your money
        </div>
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          📊 Budget Basics:the 50/30/20 rule
        </div>
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          📈 Investing for Beginners
        </div>
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          🛡️ Emergency Funds:why &amp; how much
        </div>
        <div class="bg-white/10 rounded-xl p-3 text-sm flex items-center gap-2">
          🏦 Income Tax Basics:India edition
        </div>
      </div>
    </div>

    <!-- Locked Lesson Cards -->
    <div>
      <p class="font-bold text-slate-700 mb-4">Preview Lessons 📖</p>
      <div class="grid grid-cols-2 gap-4">
        <!-- Card 1 -->
        <div class="relative rounded-2xl overflow-hidden h-32">
          <div class="bg-gradient-to-br from-emerald-400 to-teal-500 p-4 h-full text-white flex flex-col justify-between">
            <span class="font-bold text-sm">What is SIP?</span>
            <span class="bg-white/20 text-xs px-2 py-0.5 rounded-full self-start">5 min</span>
          </div>
          <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
            <span class="bg-black/50 text-white text-sm font-bold rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="relative rounded-2xl overflow-hidden h-32">
          <div class="bg-gradient-to-br from-violet-400 to-purple-500 p-4 h-full text-white flex flex-col justify-between">
            <span class="font-bold text-sm">Credit Score 101</span>
            <span class="bg-white/20 text-xs px-2 py-0.5 rounded-full self-start">7 min</span>
          </div>
          <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
            <span class="bg-black/50 text-white text-sm font-bold rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="relative rounded-2xl overflow-hidden h-32">
          <div class="bg-gradient-to-br from-amber-400 to-orange-500 p-4 h-full text-white flex flex-col justify-between">
            <span class="font-bold text-sm">Budget Like a Pro</span>
            <span class="bg-white/20 text-xs px-2 py-0.5 rounded-full self-start">4 min</span>
          </div>
          <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
            <span class="bg-black/50 text-white text-sm font-bold rounded-full px-4 py-2">
              🔒 Coming in V2
            </span>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="relative rounded-2xl overflow-hidden h-32">
          <div class="bg-gradient-to-br from-sky-400 to-blue-500 p-4 h-full text-white flex flex-col justify-between">
            <span class="font-bold text-sm">Emergency Fund Math</span>
            <span class="bg-white/20 text-xs px-2 py-0.5 rounded-full self-start">6 min</span>
          </div>
          <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
            <span class="bg-black/50 text-white text-sm font-bold rounded-full px-4 py-2">
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
  name: 'LearnView',
}
</script>
