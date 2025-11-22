<template>
  <NuxtLayout>
    <div class="max-w-4xl mx-auto p-6">
      <!-- Hero Section -->
      <div class="mb-12 text-center">
        <h1 class="text-4xl font-bold mb-4">What needs tuning today?</h1>
        <p class="text-zinc-400 max-w-xl mx-auto">
          Upload a failure photo or describe your issue. We'll cross-reference your problem against the Minimal 3DP Knowledge Base.
        </p>
      </div>

      <!-- Feature Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <NuxtLink to="/calculators" class="glass-dark rounded-xl p-6 hover:border-brand-orange transition group">
          <h2 class="text-2xl font-semibold mb-2 group-hover:text-brand-orange transition">🔧 Calculators</h2>
          <p class="text-zinc-400 text-sm">
            Rotation distance, pressure advance, and flow rate tools
          </p>
        </NuxtLink>

        <NuxtLink to="/diagnosis" class="glass-dark rounded-xl p-6 hover:border-brand-orange transition group">
          <h2 class="text-2xl font-semibold mb-2 group-hover:text-brand-orange transition">🔍 Diagnosis</h2>
          <p class="text-zinc-400 text-sm">
            AI-powered image and text analysis for troubleshooting
          </p>
        </NuxtLink>

        <a href="https://minimal3dp.com" target="_blank" class="glass-dark rounded-xl p-6 hover:border-brand-orange transition group">
          <h2 class="text-2xl font-semibold mb-2 group-hover:text-brand-orange transition">📚 Resources</h2>
          <p class="text-zinc-400 text-sm">
            Klipper guides, OrcaSlicer tips, and more
          </p>
        </a>
      </div>

      <!-- Quick Stats -->
      <div class="glass rounded-2xl p-8">
        <h3 class="text-xl font-bold mb-6">Platform Status</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="text-center">
            <div class="text-3xl font-bold text-brand-orange mb-2">63</div>
            <div class="text-sm text-zinc-400">Defect Types</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-brand-orange mb-2">6</div>
            <div class="text-sm text-zinc-400">CSV Knowledge Bases</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-brand-orange mb-2">5</div>
            <div class="text-sm text-zinc-400">Active Calculators</div>
          </div>
        </div>
      </div>

      <!-- Tech Stack Info -->
      <div class="mt-8 text-center text-zinc-500 text-sm">
        <p>Vue 3 + Nuxt + Pinia + Tailwind CSS</p>
        <p class="mt-1">Backend: FastAPI + Gemini Vision AI + Semantic Router</p>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
// Home page
</script>
