<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">⚡</span>
      OrcaSlicer Flow YOLO (Quick)
      <span class="ml-2 text-xs bg-yellow-500/20 text-yellow-400 px-2 py-1 rounded">FAST</span>
    </h2>

    <p class="text-zinc-400 mb-4">
      Calculate flow rate using OrcaSlicer's YOLO (single-pass) calibration method.
      Faster but less accurate than the two-pass method.
    </p>

    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-4 mb-8">
      <p class="text-yellow-400 text-sm">
        <strong>⚠️ Note:</strong> YOLO is faster but less accurate.
        For best results, use the two-pass calibration method above.
      </p>
    </div>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Current Flow Rate -->
      <div>
        <label for="current-flow-yolo" class="block text-sm font-medium mb-2">
          Current Flow Rate
        </label>
        <input
          id="current-flow-yolo"
          data-testid="current-flow-yolo"
          v-model.number="store.orcaSlicerFlowYolo.oldFlowRate"
          type="number"
          step="0.01"
          min="0.5"
          max="2"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 1.0 (100%)"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Default is 1.0 (100%). Check your filament profile in OrcaSlicer.
        </p>
      </div>

      <!-- YOLO Slide Value -->
      <div>
        <label for="yolo-slide-value" class="block text-sm font-medium mb-2">
          YOLO Slide Value
        </label>
        <input
          id="yolo-slide-value"
          data-testid="yolo-slide-value"
          v-model.number="store.orcaSlicerFlowYolo.yoloSlideValue"
          type="number"
          step="0.001"
          min="-1"
          max="1"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., -0.035"
        />
        <p class="text-xs text-zinc-500 mt-1">
          The slide value with the smoothest surface (e.g., -0.035)
        </p>
      </div>

      <!-- Instructions -->
      <div class="bg-zinc-800/50 rounded-lg p-4 text-sm text-zinc-400 space-y-2">
        <p class="font-semibold text-zinc-300">📋 Calibration Steps:</p>
        <ol class="list-decimal list-inside space-y-1 ml-2">
          <li>Open OrcaSlicer → Calibration → Flow Rate → YOLO</li>
          <li>Print the calibration model</li>
          <li>Feel each slide to find the smoothest surface</li>
          <li>Note the slide value (e.g., -0.035)</li>
          <li>Enter the value here to calculate new flow rate</li>
        </ol>
      </div>

      <!-- Error Message -->
      <div v-if="store.error" class="bg-red-500/10 border border-red-500/50 rounded-lg p-4 text-red-400 text-sm">
        {{ store.error }}
      </div>

      <!-- Actions -->
      <div class="flex gap-4">
        <button
          type="submit"
          data-testid="calculate-yolo-button"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition"
        >
          {{ store.loading ? 'Calculating...' : 'Calculate' }}
        </button>
        <button
          type="button"
          @click="store.resetOrcaSlicerFlowYolo()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Result -->
    <div
      v-if="store.orcaSlicerFlowYolo.result"
      data-testid="yolo-flow-result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
        <span>✅</span> Calculation Result
      </h3>

      <div class="space-y-4">
        <div>
          <p class="text-sm text-zinc-400">New Flow Rate:</p>
          <p class="text-3xl font-bold text-brand-orange">
            {{ store.orcaSlicerFlowYolo.result.new_flow.toFixed(3) }}
          </p>
        </div>

        <div>
          <p class="text-sm text-zinc-400">Change from Original:</p>
          <p class="text-lg font-semibold" :class="Math.abs(store.orcaSlicerFlowYolo.result.change_from_original) <= 10 ? 'text-green-400' : 'text-yellow-400'">
            {{ store.orcaSlicerFlowYolo.result.change_from_original > 0 ? '+' : '' }}{{ store.orcaSlicerFlowYolo.result.change_from_original.toFixed(2) }}%
          </p>
        </div>

        <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
          <p class="text-zinc-500 text-xs mb-2">OrcaSlicer Configuration:</p>
          <code class="text-green-400">{{ store.orcaSlicerFlowYolo.result.slicer_config }}</code>
          <button
            @click="copyToClipboard(store.orcaSlicerFlowYolo.result.slicer_config)"
            class="mt-2 text-xs text-brand-orange hover:underline"
          >
            📋 Copy to clipboard
          </button>
        </div>

        <div class="text-sm text-zinc-300 bg-zinc-900/50 rounded-lg p-4">
          {{ store.orcaSlicerFlowYolo.result.recommendation }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCalculatorStore } from '~/stores/calculator'
import { useAnalytics } from '~/composables/useAnalytics'

const store = useCalculatorStore()

const { trackCalculatorUse } = useAnalytics()
const handleSubmit = async () => {
  await store.calculateOrcaSlicerFlowYolo()
  if (store.orcaSlicerFlowYolo.result) {
    trackCalculatorUse('orcaslicer_flow_yolo', {
      new_flow: store.orcaSlicerFlowYolo.result.new_flow,
      change_from_original: store.orcaSlicerFlowYolo.result.change_from_original,
    })
  }
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.3s ease-out;
}
</style>
