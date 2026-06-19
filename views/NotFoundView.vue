<template>
  <div class="min-h-full flex flex-col items-center justify-center text-center px-4" style="min-height: calc(100vh - 56px);">
    <div class="text-8xl font-black bg-gradient-to-r from-violet-600 to-fuchsia-500 bg-clip-text text-transparent select-none">
      404
    </div>
    <h2 class="text-2xl font-bold text-slate-800 mt-4">Lost in the sauce 🫙</h2>
    <p class="text-slate-500 max-w-xs text-center mt-2 text-sm leading-relaxed">
      This page doesn't exist in Stacks. Maybe it moved, maybe it never existed.
    </p>
    <router-link
      to="/"
      class="mt-8 bg-violet-600 hover:bg-violet-700 text-white font-semibold px-6 py-3 rounded-xl transition-colors no-underline inline-flex items-center gap-2">
      <i class="pi pi-home text-sm"></i>
      Back to Pulse
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFoundView',
}
</script>
