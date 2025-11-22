<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🛠️</span>
      Input Shaping Calculator
    </h2>

    <p class="text-zinc-400 mb-6 text-sm">
      Recommend Klipper input shaper types based on measured resonance frequencies. Placeholder heuristic pending full CSV formula integration.
    </p>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <div>
        <label for="test-type" class="block text-sm font-medium mb-2">Test Method</label>
        <select
          id="test-type"
          data-testid="input-shaping-test-type"
          v-model="store.inputShaping.testType"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        >
          <option value="ADXL345">ADXL345 (Accelerometer)</option>
          <option value="manual">Manual (Printed test)</option>
        </select>
      </div>

      <div>
        <label for="x-frequency" class="block text-sm font-medium mb-2">X Axis Frequency (Hz)</label>
        <input
          id="x-frequency"
          data-testid="x-frequency"
          v-model.number="store.inputShaping.xFrequency"
          type="number"
          step="0.1"
          min="20"
          max="120"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 45.2"
        />
      </div>

      <div>
        <label for="y-frequency" class="block text-sm font-medium mb-2">Y Axis Frequency (Hz)</label>
        <input
          id="y-frequency"
          data-testid="y-frequency"
          v-model.number="store.inputShaping.yFrequency"
          type="number"
          step="0.1"
          min="20"
          max="120"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 37.8"
        />
      </div>

      <div
        v-if="store.error"
        data-testid="input-shaping-error"
        class="bg-red-500/10 border border-red-500/50 rounded-lg p-4 text-red-400 text-sm"
      >
        {{ store.error }}
      </div>

      <div class="flex gap-4">
        <button
          type="submit"
          data-testid="calculate-input-shaping-button"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition"
        >
          {{ store.loading ? 'Calculating...' : 'Get Recommendations' }}
        </button>
        <button
          type="button"
          data-testid="reset-input-shaping-button"
          @click="store.resetInputShaping()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <div
      v-if="store.inputShaping.result"
      data-testid="input-shaping-result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2"><span>✅</span> Recommendations</h3>
      <div class="grid grid-cols-2 gap-4 mb-4 text-sm">
        <div>
          <p class="text-zinc-400">X Shaper:</p>
          <p class="text-lg font-semibold">{{ store.inputShaping.result.shaper_x }}</p>
        </div>
        <div>
          <p class="text-zinc-400">Y Shaper:</p>
          <p class="text-lg font-semibold">{{ store.inputShaping.result.shaper_y }}</p>
        </div>
        <div>
          <p class="text-zinc-400">Max Accel:</p>
          <p class="text-lg font-semibold">{{ store.inputShaping.result.max_accel }} mm/s²</p>
        </div>
        <div>
          <p class="text-zinc-400">Square Corner Velocity:</p>
          <p class="text-lg font-semibold">{{ store.inputShaping.result.square_corner_velocity }} mm/s</p>
        </div>
      </div>
      <div class="bg-zinc-950 rounded-lg p-4 font-mono text-xs">
        <p class="text-zinc-500 text-[10px] mb-2">Klipper Configuration:</p>
        <code class="text-green-400 whitespace-pre-line">{{ store.inputShaping.result.klipper_config }}</code>
        <button
          @click="copyToClipboard(store.inputShaping.result.klipper_config)"
          class="mt-2 text-xs text-brand-orange hover:underline"
        >📋 Copy to clipboard</button>
      </div>
      <div class="text-xs text-zinc-300 bg-zinc-900/50 rounded-lg p-4 mt-4">
        {{ store.inputShaping.result.notes }}
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
  await store.calculateInputShaping()
  if (store.inputShaping.result) {
    trackCalculatorUse('input_shaping', {
      shaper_x: store.inputShaping.result.shaper_x,
      shaper_y: store.inputShaping.result.shaper_y,
      max_accel: store.inputShaping.result.max_accel,
    })
  }
}

const copyToClipboard = async (text: string) => {
  try { await navigator.clipboard.writeText(text) } catch (e) { console.error(e) }
}
</script>

<style scoped>
@keyframes fade-in { from { opacity:0; transform:translateY(10px) } to { opacity:1; transform:translateY(0) } }
.animate-fade-in { animation: fade-in 0.3s ease-out; }
</style>
