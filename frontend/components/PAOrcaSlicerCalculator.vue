<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🔬</span>
      PA & OrcaSlicer Calculator
    </h2>

    <p class="text-zinc-400 mb-8">
      Calculate Pressure Advance from OrcaSlicer test pattern height measurement.
      This uses a linear ramp test where PA increases with Z height.
    </p>

    <form @submit.prevent="handleCalculate" class="space-y-6">
      <!-- Measured Height -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Measured Height (mm)
        </label>
        <input
          v-model.number="store.paOrcaSlicer.measuredHeight"
          type="number"
          step="0.1"
          min="0"
          max="100"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 30.3"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Z height where corners look best on test print
        </p>
      </div>

      <!-- Extruder Type -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Extruder Type
        </label>
        <select
          v-model="store.paOrcaSlicer.extruderType"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        >
          <option value="direct_drive">Direct Drive (0.002 step)</option>
          <option value="bowden">Bowden (0.02 step)</option>
        </select>
      </div>

      <!-- Calculate Button -->
      <div class="flex gap-4">
        <button
          type="submit"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg transition"
        >
          {{ store.loading ? '⏳ Calculating...' : '🎯 Calculate PA' }}
        </button>
        <button
          type="button"
          @click="store.resetPAOrcaSlicer"
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
    <div v-if="store.paOrcaSlicer.result" class="mt-8 space-y-6">
      <h3 class="text-xl font-semibold border-b border-zinc-700 pb-2">Results</h3>

      <div class="grid grid-cols-2 gap-4">
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">Calculated PA</p>
          <p class="text-2xl font-bold text-brand-orange">{{ store.paOrcaSlicer.result.calculated_pa }}</p>
        </div>
        <div class="bg-zinc-950 rounded-lg p-4">
          <p class="text-sm text-zinc-500 mb-1">Step Used</p>
          <p class="text-2xl font-bold">{{ store.paOrcaSlicer.result.step_used }}</p>
        </div>
      </div>

      <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
        <p class="text-zinc-500 text-xs mb-2">Klipper Configuration:</p>
        <code class="text-green-400">{{ store.paOrcaSlicer.result.klipper_config }}</code>
        <button
          @click="copyToClipboard(store.paOrcaSlicer.result.klipper_config)"
          class="mt-2 text-xs text-brand-orange hover:underline"
        >
          📋 Copy to clipboard
        </button>
      </div>

      <div class="bg-zinc-900/50 rounded-lg p-4">
        <p class="text-sm text-zinc-400">{{ store.paOrcaSlicer.result.notes }}</p>
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
  await store.calculatePAOrcaSlicer()
  if (store.paOrcaSlicer.result) {
    trackCalculatorUse('pa_orcaslicer', {
      measured_height: store.paOrcaSlicer.measuredHeight,
      extruder_type: store.paOrcaSlicer.extruderType,
    })
  }
}

const copyToClipboard = (text: string) => {
  navigator.clipboard.writeText(text)
}
</script>
