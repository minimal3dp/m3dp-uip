<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🎯</span>
      OrcaSlicer Flow Rate (Two-Pass)
      <span class="ml-2 text-xs bg-green-500/20 text-green-400 px-2 py-1 rounded">RECOMMENDED</span>
    </h2>

    <p class="text-zinc-400 mb-4">
      Calculate optimal flow rate using OrcaSlicer's built-in two-pass calibration method.
      This provides the most accurate results.
    </p>

    <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-4 mb-8">
      <p class="text-blue-400 text-sm">
        <strong>💡 How it works:</strong> Pass 1 gets you close to the correct flow rate.
        Pass 2 fine-tunes for optimal accuracy.
      </p>
    </div>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Current Flow Rate -->
      <div>
        <label for="current-flow-pass1" class="block text-sm font-medium mb-2">
          Current Flow Rate
        </label>
        <input
          id="current-flow-pass1"
          data-testid="current-flow-pass1"
          v-model.number="store.orcaSlicerFlow.oldFlowRate"
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

      <!-- Pass 1 Slide Value -->
      <div>
        <label for="pass1-slide-value" class="block text-sm font-medium mb-2">
          Pass 1 Slide Value
        </label>
        <input
          id="pass1-slide-value"
          data-testid="pass1-slide-value"
          v-model.number="store.orcaSlicerFlow.pass1SlideValue"
          type="number"
          step="1"
          min="-50"
          max="50"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., -10"
        />
        <p class="text-xs text-zinc-500 mt-1">
          The slide number with the smoothest surface from Pass 1 (e.g., -10 for 90% slide)
        </p>
      </div>

      <!-- Pass 2 Slide Value (Optional) -->
      <div>
        <label for="pass2-slide-value" class="block text-sm font-medium mb-2">
          Pass 2 Slide Value <span class="text-zinc-500">(Optional)</span>
        </label>
        <input
          id="pass2-slide-value"
          data-testid="pass2-slide-value"
          v-model.number="store.orcaSlicerFlow.pass2SlideValue"
          type="number"
          step="1"
          min="-50"
          max="50"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., -1"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Leave empty for Pass 1 calculation only. Enter value for final Pass 2 result.
        </p>
      </div>

      <!-- Instructions -->
      <div class="bg-zinc-800/50 rounded-lg p-4 text-sm text-zinc-400 space-y-2">
        <p class="font-semibold text-zinc-300">📋 Calibration Steps:</p>
        <ol class="list-decimal list-inside space-y-1 ml-2">
          <li>Open OrcaSlicer → Calibration → Flow Rate → Pass 1</li>
          <li>Print the calibration model</li>
          <li>Feel each slide to find the smoothest surface</li>
          <li>Enter the slide number here and calculate Pass 1 flow rate</li>
          <li>Run Pass 2 using the Pass 1 flow rate</li>
          <li>Enter Pass 2 slide value for final flow rate</li>
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
          data-testid="calculate-flow-button"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition"
        >
          {{ store.loading ? 'Calculating...' : 'Calculate' }}
        </button>
        <button
          type="button"
          @click="store.resetOrcaSlicerFlow()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Result -->
    <div
      v-if="store.orcaSlicerFlow.result"
      data-testid="orcaslicer-flow-result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
        <span>✅</span> Calculation Result
      </h3>

      <div class="space-y-4">
        <div data-testid="pass1-flow-result">
          <p class="text-sm text-zinc-400">Pass 1 Flow Rate:</p>
          <p class="text-3xl font-bold text-brand-orange">
            {{ store.orcaSlicerFlow.result.pass_1_flow.toFixed(3) }}
          </p>
        </div>

        <div v-if="store.orcaSlicerFlow.result.pass_2_flow" class="border-t border-zinc-700 pt-4">
          <p class="text-sm text-zinc-400">Pass 2 Flow Rate (Final):</p>
          <p class="text-3xl font-bold text-green-400">
            {{ store.orcaSlicerFlow.result.pass_2_flow.toFixed(3) }}
          </p>
        </div>

        <div>
          <p class="text-sm text-zinc-400">Change from Original:</p>
          <p class="text-lg font-semibold" :class="Math.abs(store.orcaSlicerFlow.result.change_from_original) <= 10 ? 'text-green-400' : 'text-yellow-400'">
            {{ store.orcaSlicerFlow.result.change_from_original > 0 ? '+' : '' }}{{ store.orcaSlicerFlow.result.change_from_original.toFixed(2) }}%
          </p>
        </div>

        <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
          <p class="text-zinc-500 text-xs mb-2">OrcaSlicer Configuration:</p>
          <code class="text-green-400">{{ store.orcaSlicerFlow.result.slicer_config }}</code>
          <button
            @click="copyToClipboard(store.orcaSlicerFlow.result.slicer_config)"
            class="mt-2 text-xs text-brand-orange hover:underline"
          >
            📋 Copy to clipboard
          </button>
        </div>

        <div class="text-sm text-zinc-300 bg-zinc-900/50 rounded-lg p-4">
          {{ store.orcaSlicerFlow.result.recommendation }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCalculatorStore } from '~/stores/calculator'

const store = useCalculatorStore()

const handleSubmit = async () => {
  await store.calculateOrcaSlicerFlow()
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
