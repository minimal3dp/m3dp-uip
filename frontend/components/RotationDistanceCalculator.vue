<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">🔧</span>
      Rotation Distance Calculator
    </h2>

    <p class="text-zinc-400 mb-8">
      Calculate the correct rotation_distance value for your extruder stepper motor.
      This calibration ensures accurate extrusion amounts.
    </p>

    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Current Rotation Distance -->
      <div>
        <label for="current-rotation-distance" class="block text-sm font-medium mb-2">
          Current Rotation Distance (from printer.cfg)
        </label>
        <input
          id="current-rotation-distance"
          data-testid="current-rotation-distance"
          v-model.number="store.rotationDistance.currentRotationDistance"
          type="number"
          step="0.001"
          min="0"
          max="100"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 33.5"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Default: 33.5 for BMG, 22.7 for Orbiter
        </p>
      </div>

      <!-- Requested Extrusion -->
      <div>
        <label for="requested-extrusion" class="block text-sm font-medium mb-2">
          Requested Extrusion Distance (mm)
        </label>
        <input
          id="requested-extrusion"
          data-testid="requested-extrusion"
          v-model.number="store.rotationDistance.requestedExtrusion"
          type="number"
          step="1"
          min="50"
          max="150"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Standard calibration uses 100mm
        </p>
      </div>

      <!-- Actual Extrusion -->
      <div>
        <label for="actual-extrusion" class="block text-sm font-medium mb-2">
          Actual Extruded Distance (measured with calipers)
        </label>
        <input
          id="actual-extrusion"
          data-testid="actual-extrusion"
          v-model.number="store.rotationDistance.actualExtrusion"
          type="number"
          step="0.1"
          min="0"
          max="500"
          required
          class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition"
          placeholder="e.g., 98.5"
        />
        <p class="text-xs text-zinc-500 mt-1">
          Measure remaining distance from 120mm mark after extruding
        </p>
      </div>

      <!-- Error Message -->
      <div v-if="store.error" class="bg-red-500/10 border border-red-500/50 rounded-lg p-4 text-red-400 text-sm">
        {{ store.error }}
      </div>

      <!-- Actions -->
      <div class="flex gap-4">
        <button
          type="submit"
          data-testid="calculate-button"
          :disabled="store.loading"
          class="flex-1 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition"
        >
          {{ store.loading ? 'Calculating...' : 'Calculate' }}
        </button>
        <button
          type="button"
          @click="store.resetRotationDistance()"
          class="px-6 py-3 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition"
        >
          Reset
        </button>
      </div>
    </form>

    <!-- Result -->
    <div
      v-if="store.rotationDistance.result"
      data-testid="rotation-distance-result"
      class="mt-8 glass-dark rounded-xl p-6 border-l-4 border-brand-orange animate-fade-in"
    >
      <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
        <span>✅</span> Calculation Result
      </h3>

      <div class="space-y-4">
        <div>
          <p class="text-sm text-zinc-400">New Rotation Distance:</p>
          <p class="text-3xl font-bold text-brand-orange">
            {{ store.rotationDistance.result.new_rotation_distance }}
          </p>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-zinc-400">Change:</p>
            <p class="text-lg font-semibold">
              {{ store.rotationDistance.result.change_percent.toFixed(2) }}%
            </p>
          </div>
          <div>
            <p class="text-sm text-zinc-400">Tolerance:</p>
            <p class="text-lg font-semibold" :class="store.rotationDistance.result.within_tolerance ? 'text-green-400' : 'text-yellow-400'">
              {{ store.rotationDistance.result.within_tolerance ? '✓ Within ±2mm' : '⚠ Outside ±2mm' }}
            </p>
          </div>
        </div>

        <div class="bg-zinc-950 rounded-lg p-4 font-mono text-sm">
          <p class="text-zinc-500 text-xs mb-2">Klipper Configuration:</p>
          <code class="text-green-400">{{ store.rotationDistance.result.klipper_config }}</code>
          <button
            @click="copyToClipboard(store.rotationDistance.result.klipper_config)"
            class="mt-2 text-xs text-brand-orange hover:underline"
          >
            📋 Copy to clipboard
          </button>
        </div>

        <div class="text-sm text-zinc-300 bg-zinc-900/50 rounded-lg p-4">
          {{ store.rotationDistance.result.recommendation }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCalculatorStore } from '~/stores/calculator'

const store = useCalculatorStore()

const handleSubmit = async () => {
  await store.calculateRotationDistance()
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
    // Could add a toast notification here
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
