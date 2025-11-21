<template>
  <div class="min-h-screen flex flex-col bg-zinc-950">
    <!-- Header -->
    <header class="border-b border-zinc-800 bg-zinc-900/50 sticky top-0 z-50 backdrop-blur-sm">
      <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <NuxtLink to="/" class="flex items-center gap-2 hover:opacity-80 transition">
          <div class="w-8 h-8 bg-brand-orange rounded-lg flex items-center justify-center text-white font-bold">
            M3
          </div>
          <span class="font-bold text-lg tracking-tight hidden sm:inline">
            Minimal <span class="text-brand-orange">3DP</span> Analysis
          </span>
        </NuxtLink>

        <nav class="text-sm font-medium text-zinc-400 flex gap-4">
          <NuxtLink to="/" class="hover:text-white transition">Dashboard</NuxtLink>
          <NuxtLink to="/calculators" class="hover:text-white transition">Calculators</NuxtLink>
          <NuxtLink to="/diagnosis" class="hover:text-white transition">Diagnosis</NuxtLink>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="border-t border-zinc-800 bg-zinc-900/50 mt-auto">
      <div class="max-w-6xl mx-auto px-4 py-6 text-center text-sm text-zinc-500">
        <p>Part of the <a href="https://minimal3dp.com" target="_blank" class="text-brand-orange hover:underline">minimal3dp.com</a> ecosystem</p>
        <p class="mt-1">Phase 3: Vue 3 + Nuxt Frontend</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
// Default layout
</script>
