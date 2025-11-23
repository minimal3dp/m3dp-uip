<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🎯</span>
      Adaptive Pressure Advance
    </h2>

    <p class="text-zinc-400 mb-8">
      Calculate adaptive PA range from test matrix results. Adaptive PA automatically adjusts
      pressure advance based on print speed, flow rate, and acceleration.
    </p>

    <form @submit.prevent="handleCalculate" class="space-y-6">
      <!-- PA Values -->
      <div>
        <label class="block text-sm font-medium mb-2">
          PA Test Values (comma-separated)
        </label>
        <textarea
          v-model="store.adaptivePressureAdvance.paValues"
          rows="3"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition font-mono text-sm"
          placeholder="e.g., 0.035, 0.045, 0.055, 0.065, 0.075, 0.085"
        ></textarea>
        <p class="text-xs text-zinc-500 mt-1">
          Enter all PA values that worked well across different speeds, flows, and accelerations
        </p>
      </div>

      <!-- Calculate Button -->
      <div class="flex gap-4">
        <button
          type="submit"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg transition"
        >
          {{ store.loading ? '⏳ Calculating...' : '🎯 Calculate Adaptive Range' }}
        </button>
        <button
          type="button"
          @click="store.resetAdaptivePressureAdvance"
          class="bg-zinc-800 hover:bg-zinc-700 text-white py-3 px-6 rounded-lg transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Error Message -->
    <div v-if="store.error" class="mt-6 bg-red-500/10 border border-red-500/50 rounded-lg p-4">
      <p class="text-red-400">{{ store.error }}</p>
    </div>

    <!-- Results -->
    <div v-if="store.adaptivePressureAdvance.result" class="mt-8 space-y-6">
      <h3 class="text-xl font-semibold border-b border-zinc-700 pb-2">Adaptive PA Configuration</h3>

      <div class="grid grid-cols-2 gap-4">
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">Min PA (Tested)</p>
          <p class="text-xl font-bold">{{ store.adaptivePressureAdvance.result.min_pa_tested }}</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">Max PA (Tested)</p>
          <p class="text-xl font-bold">{{ store.adaptivePressureAdvance.result.max_pa_tested }}</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">PA Range</p>
          <p class="text-xl font-bold">{{ store.adaptivePressureAdvance.result.pa_range }}</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">Step Size</p>
          <p class="text-xl font-bold">{{ store.adaptivePressureAdvance.result.adaptive_step }}</p>
        </div>
      </div>

      <div class="bg-blue-500/10 border border-blue-500/50 rounded-lg p-4">
        <p class="text-sm font-semibold text-blue-400 mb-2">Adaptive Range (with safety margins):</p>
        <div class="grid grid-cols-2 gap-4 mt-3">
          <div>
            <p class="text-xs text-blue-300 mb-1">Adaptive Min PA</p>
            <p class="text-2xl font-bold text-brand-orange">{{ store.adaptivePressureAdvance.result.adaptive_min_pa }}</p>
          </div>
          <div>
            <p class="text-xs text-blue-300 mb-1">Adaptive Max PA</p>
            <p class="text-2xl font-bold text-brand-orange">{{ store.adaptivePressureAdvance.result.adaptive_max_pa }}</p>
          </div>
        </div>
      </div>

      <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
        <p class="text-zinc-500 text-xs mb-2">OrcaSlicer Configuration:</p>
        <pre class="text-green-400 whitespace-pre-wrap">{{ store.adaptivePressureAdvance.result.orcaslicer_config }}</pre>
        <button
          @click="copyToClipboard(store.adaptivePressureAdvance.result.orcaslicer_config)"
          class="mt-2 text-xs text-brand-orange hover:underline"
        >
          📋 Copy to clipboard
        </button>
      </div>

      <div class="bg-zinc-900/50 rounded-lg p-4">
        <p class="text-sm text-zinc-400">{{ store.adaptivePressureAdvance.result.notes }}</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/50 rounded-lg p-4">
        <p class="text-sm font-semibold text-yellow-400 mb-2">⚠️ Advanced Feature</p>
        <p class="text-xs text-yellow-300">
          Adaptive PA requires extensive testing across multiple printing conditions.
          Monitor prints carefully and adjust range if issues occur.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCalculatorStore } from '~/stores/calculator'
import { useAnalytics } from '~/composables/useAnalytics'

const store = useCalculatorStore()
const { trackCalculatorUse } = useAnalytics()

const handleCalculate = async () => {
  await store.calculateAdaptivePressureAdvance()
  if (store.adaptivePressureAdvance.result) {
    const paArray = store.adaptivePressureAdvance.paValues
      .split(',')
      .map(v => parseFloat(v.trim()))
      .filter(v => !isNaN(v))

    trackCalculatorUse('adaptive_pressure_advance', {
      num_values: paArray.length,
      min_pa: Math.min(...paArray),
      max_pa: Math.max(...paArray),
    })
  }
}

const copyToClipboard = (text: string) => {
  navigator.clipboard.writeText(text)
}
</script>
