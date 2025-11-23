<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">⚡</span>
      Extrusion Rate Smoothing (ERS)
    </h2>

    <p class="text-zinc-400 mb-8">
      Calculate ERS values for OrcaSlicer. ERS smooths extrusion rate changes during
      acceleration/deceleration, reducing pressure fluctuations.
    </p>

    <form @submit.prevent="handleCalculate" class="space-y-6">
      <!-- Acceleration -->
      <div>
        <label class="block text-sm font-medium mb-2">
          External Perimeter Acceleration (mm/s²)
        </label>
        <input
          v-model.number="store.extrusionRateSmoothing.acceleration"
          type="number"
          step="100"
          min="1000"
          max="50000"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 12000"
        />
      </div>

      <!-- Line Width -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Line Width (mm)
        </label>
        <input
          v-model.number="store.extrusionRateSmoothing.lineWidth"
          type="number"
          step="0.1"
          min="0.2"
          max="2"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 0.6"
        />
      </div>

      <!-- Layer Height -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Layer Height (mm)
        </label>
        <input
          v-model.number="store.extrusionRateSmoothing.layerHeight"
          type="number"
          step="0.05"
          min="0.1"
          max="1"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 0.2"
        />
      </div>

      <!-- Calculate Button -->
      <div class="flex gap-4">
        <button
          type="submit"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg transition"
        >
          {{ store.loading ? '⏳ Calculating...' : '🎯 Calculate ERS' }}
        </button>
        <button
          type="button"
          @click="store.resetExtrusionRateSmoothing"
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
    <div v-if="store.extrusionRateSmoothing.result" class="mt-8 space-y-6">
      <h3 class="text-xl font-semibold border-b border-zinc-700 pb-2">Results</h3>

      <div class="grid grid-cols-3 gap-4">
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">ERS Max</p>
          <p class="text-xl font-bold">{{ store.extrusionRateSmoothing.result.ers_max }} mm³/s²</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">ERS 60% (Start)</p>
          <p class="text-xl font-bold text-brand-orange">{{ store.extrusionRateSmoothing.result.ers_60_percent }}</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">ERS 80% (Aggressive)</p>
          <p class="text-xl font-bold">{{ store.extrusionRateSmoothing.result.ers_80_percent }}</p>
        </div>
      </div>

      <div class="bg-blue-500/10 border border-blue-500/50 rounded-lg p-4">
        <p class="text-sm font-semibold text-blue-400 mb-2">Recommended:</p>
        <p class="text-sm text-blue-300">{{ store.extrusionRateSmoothing.result.recommended }}</p>
      </div>

      <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
        <p class="text-zinc-500 text-xs mb-2">OrcaSlicer Configuration:</p>
        <code class="text-green-400">{{ store.extrusionRateSmoothing.result.orcaslicer_config }}</code>
        <button
          @click="copyToClipboard(store.extrusionRateSmoothing.result.orcaslicer_config)"
          class="mt-2 text-xs text-brand-orange hover:underline"
        >
          📋 Copy to clipboard
        </button>
      </div>

      <div class="bg-zinc-900/50 rounded-lg p-4">
        <p class="text-sm text-zinc-400">{{ store.extrusionRateSmoothing.result.notes }}</p>
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
  await store.calculateExtrusionRateSmoothing()
  if (store.extrusionRateSmoothing.result) {
    trackCalculatorUse('extrusion_rate_smoothing', {
      acceleration: store.extrusionRateSmoothing.acceleration,
      line_width: store.extrusionRateSmoothing.lineWidth,
      layer_height: store.extrusionRateSmoothing.layerHeight,
    })
  }
}

const copyToClipboard = (text: string) => {
  navigator.clipboard.writeText(text)
}
</script>
