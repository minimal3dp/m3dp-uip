<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">⚙️</span>
      Pressure Advance Calculator
    </h2>

    <p class="text-zinc-400 mb-8">
      Get pressure advance recommendations based on your material type and printing parameters.
    </p>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Material Type -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Material Type
        </label>
        <select
          v-model="store.pressureAdvance.materialType"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        >
          <option value="PLA">PLA</option>
          <option value="PETG">PETG</option>
          <option value="ABS">ABS</option>
          <option value="TPU">TPU (Flexible)</option>
          <option value="ASA">ASA</option>
          <option value="NYLON">Nylon</option>
        </select>
      </div>

      <!-- Current PA (Optional) -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Current Pressure Advance (optional)
        </label>
        <input
          v-model.number="store.pressureAdvance.currentPa"
          type="number"
          step="0.001"
          min="0"
          max="1"
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 0.05"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Leave empty to start from 0
        </p>
      </div>

      <!-- Print Speed -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Print Speed (mm/s)
        </label>
        <input
          v-model.number="store.pressureAdvance.printSpeed"
          type="number"
          step="1"
          min="1"
          max="500"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Your typical printing speed
        </p>
      </div>

      <!-- Nozzle Diameter -->
      <div>
        <label class="block text-sm font-medium mb-2">
          Nozzle Diameter (mm)
        </label>
        <input
          v-model.number="store.pressureAdvance.nozzleDiameter"
          type="number"
          step="0.1"
          min="0.1"
          max="2"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        />
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
          {{ store.loading ? 'Calculating...' : 'Get Recommendations' }}
        </button>
        <button
          type="button"
          @click="store.resetPressureAdvance()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Result -->
    <div
      v-if="store.pressureAdvance.result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
        <span>✅</span> Recommendations
      </h3>

      <div class="space-y-4">
        <div>
          <p class="text-sm text-zinc-400">Recommended Range for {{ store.pressureAdvance.materialType }}:</p>
          <p class="text-3xl font-bold text-brand-orange">
            {{ store.pressureAdvance.result.recommended_range[0] }} - {{ store.pressureAdvance.result.recommended_range[1] }}
          </p>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-zinc-400">Start Value:</p>
            <p class="text-lg font-semibold">{{ store.pressureAdvance.result.start_value }}</p>
          </div>
          <div>
            <p class="text-sm text-zinc-400">Test Increment:</p>
            <p class="text-lg font-semibold">{{ store.pressureAdvance.result.increment }}</p>
          </div>
        </div>

        <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
          <p class="text-zinc-500 text-xs mb-2">Klipper Configuration (suggested):</p>
          <code class="text-green-400">{{ store.pressureAdvance.result.klipper_config }}</code>
          <button
            @click="copyToClipboard(store.pressureAdvance.result.klipper_config)"
            class="mt-2 text-xs text-brand-orange hover:underline"
          >
            📋 Copy to clipboard
          </button>
        </div>

        <div class="bg-zinc-900/50 rounded-lg p-4">
          <p class="text-sm font-semibold mb-2">Test Parameters:</p>
          <div class="grid grid-cols-2 gap-2 text-sm text-zinc-400">
            <div>Speed: {{ store.pressureAdvance.result.test_parameters.speed }} mm/s</div>
            <div>Layer Height: {{ store.pressureAdvance.result.test_parameters.layer_height }} mm</div>
            <div>Line Width: {{ store.pressureAdvance.result.test_parameters.line_width }} mm</div>
            <div>End PA: {{ store.pressureAdvance.result.test_parameters.end_pa }}</div>
          </div>
        </div>

        <div class="text-sm text-zinc-300 bg-zinc-900/50 rounded-lg p-4">
          <p class="font-semibold mb-2">Calibration Method:</p>
          {{ store.pressureAdvance.result.calibration_method }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCalculatorStore } from '~/stores/calculator'

const store = useCalculatorStore()

const handleSubmit = async () => {
  await store.calculatePressureAdvance()
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
