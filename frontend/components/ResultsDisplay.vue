<template>
  <div
    v-if="store.result"
    class="glass rounded-2xl p-8 bg-zinc-900 border-l-4 border-brand-orange animate-fade-in"
  >
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🔍</span>
      Diagnosis Results
    </h2>

    <!-- Classification -->
    <div class="mb-6 glass-dark rounded-xl p-6">
      <div class="flex items-start justify-between mb-4">
        <div>
          <p class="text-sm text-zinc-400 mb-1">Issue Type</p>
          <p class="text-2xl font-bold text-brand-orange">
            {{ store.result.classification || 'Analyzing...' }}
          </p>
        </div>
        <div v-if="store.result.confidence" class="text-right">
          <p class="text-sm text-zinc-400 mb-1">Confidence</p>
          <p class="text-xl font-semibold">
            {{ (store.result.confidence * 100).toFixed(0) }}%
          </p>
        </div>
      </div>

      <div v-if="store.result.category" class="text-sm">
        <span class="text-zinc-400">Category:</span>
        <span class="ml-2 px-3 py-1 bg-zinc-800 rounded-full text-white">
          {{ store.result.category }}
        </span>
      </div>
    </div>

    <!-- Analysis -->
    <div v-if="store.result.analysis" class="mb-6">
      <h3 class="text-lg font-semibold mb-3">Analysis</h3>
      <div class="glass-dark rounded-xl p-6 text-zinc-300 leading-relaxed">
        {{ store.result.analysis }}
      </div>
    </div>

    <!-- Recommendations -->
    <div v-if="store.result.recommendations" class="mb-6">
      <h3 class="text-lg font-semibold mb-3">Recommended Actions</h3>
      <div class="space-y-3">
        <div
          v-for="(rec, idx) in store.result.recommendations"
          :key="idx"
          class="glass-dark rounded-xl p-4 flex items-start gap-3"
        >
          <span class="text-brand-orange font-bold text-lg">{{ idx + 1 }}.</span>
          <p class="text-zinc-300">{{ rec }}</p>
        </div>
      </div>
    </div>

    <!-- Relevant Calculators -->
    <div v-if="store.result.suggested_calculators" class="mb-6">
      <h3 class="text-lg font-semibold mb-3">Suggested Calibrations</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <NuxtLink
          v-for="calc in store.result.suggested_calculators"
          :key="calc"
          to="/calculators"
          class="glass-dark rounded-xl p-4 hover:border-brand-orange transition group"
        >
          <p class="font-semibold group-hover:text-brand-orange transition">
            {{ formatCalculatorName(calc) }}
          </p>
          <p class="text-xs text-zinc-500 mt-1">Click to calibrate →</p>
        </NuxtLink>
      </div>
    </div>

    <!-- Knowledge Base References -->
    <div v-if="store.result.kb_references" class="mb-6">
      <h3 class="text-lg font-semibold mb-3">Knowledge Base References</h3>
      <div class="glass-dark rounded-xl p-6">
        <ul class="space-y-2 text-sm text-zinc-400">
          <li v-for="(ref, idx) in store.result.kb_references" :key="idx" class="flex items-start gap-2">
            <span class="text-brand-orange">•</span>
            <span>{{ ref }}</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- Reset Button -->
    <button
      @click="store.reset()"
      class="w-full bg-zinc-800 hover:bg-zinc-700 text-white px-6 py-3 rounded-lg font-medium transition"
    >
      ← Start New Analysis
    </button>
  </div>
</template>

<script setup lang="ts">
import { useDiagnosisStore } from '~/stores/diagnosis'

const store = useDiagnosisStore()

const formatCalculatorName = (name: string): string => {
  return name
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
}
</script>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.5s ease-out;
}
</style>
