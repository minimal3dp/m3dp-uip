<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🔥</span>
      Max Volumetric Speed Calculator
    </h2>

    <p class="text-zinc-400 mb-8">
      Determine your hotend's maximum flow rate to optimize print speeds without underextrusion. Use OrcaSlicer's "Max Flowrate" calibration test.
    </p>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Start Value -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Start Value (mm³/s)
        </label>
        <input
          v-model.number="store.maxVolumetricSpeed.startValue"
          type="number"
          step="0.5"
          min="1"
          max="20"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 5.0"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Starting speed from OrcaSlicer test (typically 5-10 mm³/s)
        </p>
      </div>

      <!-- Step Value -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Step Value (mm³/s)
        </label>
        <input
          v-model.number="store.maxVolumetricSpeed.stepValue"
          type="number"
          step="0.1"
          min="0.1"
          max="2"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 0.5"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Increment between test sections (0.5 recommended)
        </p>
      </div>

      <!-- Height Measured -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Height Measured (mm)
        </label>
        <input
          v-model.number="store.maxVolumetricSpeed.heightMeasured"
          type="number"
          step="0.01"
          min="1"
          max="200"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 27.23"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Height where print quality starts degrading (measure with calipers)
        </p>
      </div>

      <!-- Temperature (Optional) -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Test Temperature (°C) - Optional
        </label>
        <input
          v-model.number="store.maxVolumetricSpeed.temperature"
          type="number"
          step="5"
          min="150"
          max="300"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 240"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Hotend temperature during test for reference
        </p>
      </div>

      <!-- Hotend Type (Optional) -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Hotend Type - Optional
        </label>
        <select
          v-model="store.maxVolumetricSpeed.hotendType"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        >
          <option value="">Select hotend (optional)</option>
          <option value="E3D V6">E3D V6</option>
          <option value="E3D Revo">E3D Revo</option>
          <option value="Dragon SF">Dragon SF</option>
          <option value="Dragon HF">Dragon HF</option>
          <option value="Rapido HF">Rapido HF</option>
          <option value="Rapido UHF">Rapido UHF</option>
          <option value="Mosquito">Mosquito</option>
          <option value="Mosquito Magnum">Mosquito Magnum</option>
          <option value="Other">Other</option>
        </select>
      </div>

      <!-- Error Message -->
      <div v-if="store.error" class="bg-red-500/10 border border-red-500/50 rounded-lg p-4 text-red-400 text-sm">
        {{ store.error }}
      </div>

      <!-- Actions -->
      <div class="flex gap-4">
        <button
          type="submit"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition"
        >
          {{ store.loading ? 'Calculating...' : 'Calculate Max Flow' }}
        </button>
        <button
          type="button"
          @click="store.resetMaxVolumetricSpeed()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Result -->
    <div
      v-if="store.maxVolumetricSpeed.result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
        <span>✅</span> Results
      </h3>

      <div class="space-y-4">
        <!-- Max Flow -->
        <div>
          <p class="text-sm text-zinc-400">Maximum Volumetric Speed:</p>
          <p class="text-3xl font-bold text-brand-orange">
            {{ store.maxVolumetricSpeed.result.max_flow }} mm³/s
          </p>
        </div>

        <!-- Safe Values -->
        <div class="grid grid-cols-2 gap-4">
          <div class="bg-zinc-950 rounded-lg p-4">
            <p class="text-sm text-zinc-400">Safe Flow (95%) - Recommended</p>
            <p class="text-2xl font-bold text-green-400">{{ store.maxVolumetricSpeed.result.safe_flow_95 }} mm³/s</p>
            <p class="text-xs text-zinc-500 mt-1">Use this in your slicer</p>
          </div>
          <div class="bg-zinc-950 rounded-lg p-4">
            <p class="text-sm text-zinc-400">Safe Flow (90%) - Conservative</p>
            <p class="text-2xl font-bold text-blue-400">{{ store.maxVolumetricSpeed.result.safe_flow_90 }} mm³/s</p>
            <p class="text-xs text-zinc-500 mt-1">For critical prints</p>
          </div>
        </div>

        <!-- Hotend Comparison -->
        <div class="bg-zinc-900/50 rounded-lg p-4">
          <p class="text-sm font-semibold mb-2">Hotend Comparison:</p>
          <p class="text-zinc-300 mb-2">
            Your result ({{ store.maxVolumetricSpeed.result.comparison.your_max_flow }} mm³/s) is similar to a
            <span class="font-bold text-brand-orange">{{ store.maxVolumetricSpeed.result.comparison.closest_hotend }}</span>
            ({{ store.maxVolumetricSpeed.result.comparison.closest_flow }} mm³/s)
          </p>
          <details class="text-sm text-zinc-400">
            <summary class="cursor-pointer hover:text-white">Common Hotend Flow Rates</summary>
            <ul class="mt-2 space-y-1 ml-4">
              <li v-for="(flow, hotend) in store.maxVolumetricSpeed.result.comparison.common_hotends" :key="hotend">
                {{ hotend }}: {{ flow }} mm³/s
              </li>
            </ul>
          </details>
        </div>

        <!-- Slicer Config -->
        <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
          <p class="text-zinc-500 text-xs mb-2">Slicer Configuration (95% safe value):</p>
          <code class="text-green-400">{{ store.maxVolumetricSpeed.result.slicer_config }}</code>
          <button
            @click="copyToClipboard(store.maxVolumetricSpeed.result.slicer_config)"
            class="mt-2 text-xs text-brand-orange hover:underline"
          >
            📋 Copy to clipboard
          </button>
        </div>

        <!-- Recommendation -->
        <div class="text-sm text-zinc-300 bg-zinc-900/50 rounded-lg p-4">
          <p class="font-semibold mb-2">💡 Recommendation:</p>
          {{ store.maxVolumetricSpeed.result.recommendation }}
        </div>

        <!-- Speed Calculator Helper -->
        <div class="bg-blue-950/30 border border-blue-500/30 rounded-lg p-4 text-sm">
          <p class="font-semibold text-blue-400 mb-2">📐 Speed Formula:</p>
          <p class="text-zinc-300 mb-1">
            <code class="bg-zinc-900 px-2 py-1 rounded">max_speed = max_flow / layer_height / line_width</code>
          </p>
          <p class="text-zinc-400 text-xs">
            Example: {{ store.maxVolumetricSpeed.result.safe_flow_95 }} mm³/s / 0.2mm / 0.4mm =
            <span class="font-bold text-blue-400">{{ (store.maxVolumetricSpeed.result.safe_flow_95 / 0.2 / 0.4).toFixed(0) }} mm/s</span>
          </p>
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
  await store.calculateMaxVolumetricSpeed()
  if (store.maxVolumetricSpeed.result) {
    trackCalculatorUse('max_volumetric_speed', {
      max_flow: store.maxVolumetricSpeed.result.max_flow,
      safe_flow_95: store.maxVolumetricSpeed.result.safe_flow_95,
      closest_hotend: store.maxVolumetricSpeed.result.comparison.closest_hotend,
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
