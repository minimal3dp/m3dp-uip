<template>
  <div class="xy-offsets-calculator bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
      X and Y Offsets Calculator
    </h2>
    <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">
      Calculate BLTouch/CR Touch probe X and Y offsets. Formula: x_offset = probe_x - nozzle_x, y_offset = probe_y - nozzle_y.
      <a
        href="https://www.klipper3d.org/Probe_Calibrate.html#calibrating-probe-x-and-y-offsets"
        target="_blank"
        rel="noopener noreferrer"
        class="text-blue-600 dark:text-blue-400 hover:underline"
      >
        Reference: Klipper Docs
      </a>
    </p>

    <!-- Instructions -->
    <div class="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 mb-6 border border-blue-200 dark:border-blue-800">
      <h3 class="text-md font-semibold text-blue-900 dark:text-blue-100 mb-2">
        📋 Step-by-Step Instructions
      </h3>
      <ol class="text-sm text-blue-800 dark:text-blue-200 space-y-1 list-decimal list-inside">
        <li>Home printer with G28</li>
        <li>Issue <code class="bg-blue-100 dark:bg-blue-900 px-1 rounded">PROBE</code> command in terminal</li>
        <li>Issue <code class="bg-blue-100 dark:bg-blue-900 px-1 rounded">GET_POSITION</code> and record toolhead X/Y</li>
        <li>Mark the bed at the probe point (use tape)</li>
        <li>Manually jog nozzle tip to the marked spot</li>
        <li>Issue <code class="bg-blue-100 dark:bg-blue-900 px-1 rounded">GET_POSITION</code> again and record toolhead X/Y</li>
        <li>Enter all four values below</li>
      </ol>
    </div>

    <!-- Input Form -->
    <form @submit.prevent="handleCalculate" class="space-y-4 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Toolhead X Probe -->
        <div>
          <label for="x-probe" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Toolhead X Probe *
          </label>
          <input
            id="x-probe"
            v-model.number="toolheadXProbe"
            type="number"
            step="0.1"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="e.g., 188.0"
          />
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
            X position when probe triggered (from GET_POSITION)
          </p>
        </div>

        <!-- Toolhead Y Probe -->
        <div>
          <label for="y-probe" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Toolhead Y Probe *
          </label>
          <input
            id="y-probe"
            v-model.number="toolheadYProbe"
            type="number"
            step="0.1"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="e.g., 185.0"
          />
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
            Y position when probe triggered (from GET_POSITION)
          </p>
        </div>

        <!-- Toolhead X Nozzle -->
        <div>
          <label for="x-nozzle" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Toolhead X Nozzle *
          </label>
          <input
            id="x-nozzle"
            v-model.number="toolheadXNozzle"
            type="number"
            step="0.1"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="e.g., 224.0"
          />
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
            X position when nozzle at marked spot
          </p>
        </div>

        <!-- Toolhead Y Nozzle -->
        <div>
          <label for="y-nozzle" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Toolhead Y Nozzle *
          </label>
          <input
            id="y-nozzle"
            v-model.number="toolheadYNozzle"
            type="number"
            step="0.1"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="e.g., 148.0"
          />
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
            Y position when nozzle at marked spot
          </p>
        </div>
      </div>

      <!-- Calculate Button -->
      <button
        type="submit"
        :disabled="loading || !allFieldsFilled"
        class="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-2 px-4 rounded-md transition-colors duration-200"
      >
        {{ loading ? 'Calculating...' : 'Calculate Offsets' }}
      </button>
    </form>

    <!-- Error Display -->
    <div v-if="error" class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-md p-4 mb-6">
      <p class="text-red-800 dark:text-red-200 text-sm">{{ error }}</p>
    </div>

    <!-- Results Display -->
    <transition name="fade">
      <div v-if="result" class="space-y-6">
        <!-- Main Result -->
        <div class="bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20 rounded-lg p-6 border border-green-200 dark:border-green-800">
          <h3 class="text-lg font-semibold mb-4 text-gray-900 dark:text-white">
            Calculated Offsets
          </h3>
          <div class="grid grid-cols-2 gap-6">
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">X Offset</p>
              <p class="text-4xl font-bold text-green-600 dark:text-green-400">{{ result.x_offset }}mm</p>
              <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
                {{ result.x_offset < 0 ? '← Probe is left of nozzle' : '→ Probe is right of nozzle' }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">Y Offset</p>
              <p class="text-4xl font-bold text-blue-600 dark:text-blue-400">{{ result.y_offset }}mm</p>
              <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
                {{ result.y_offset < 0 ? '↓ Probe is front of nozzle' : '↑ Probe is back of nozzle' }}
              </p>
            </div>
          </div>
          <div class="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
            <div class="grid grid-cols-2 gap-4 text-sm">
              <div>
                <p class="text-gray-600 dark:text-gray-400">Probe Position</p>
                <p class="font-medium text-gray-900 dark:text-white">
                  X: {{ result.toolhead_x_probe }}, Y: {{ result.toolhead_y_probe }}
                </p>
              </div>
              <div>
                <p class="text-gray-600 dark:text-gray-400">Nozzle Position</p>
                <p class="font-medium text-gray-900 dark:text-white">
                  X: {{ result.toolhead_x_nozzle }}, Y: {{ result.toolhead_y_nozzle }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Klipper Config -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex justify-between items-center mb-2">
            <h4 class="text-md font-semibold text-gray-900 dark:text-white">Klipper Configuration</h4>
            <button
              @click="copyToClipboard(result.klipper_config)"
              class="text-sm bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-md transition-colors duration-200"
            >
              {{ copied ? '✓ Copied!' : 'Copy' }}
            </button>
          </div>
          <pre class="bg-gray-900 dark:bg-black text-green-400 p-4 rounded-md overflow-x-auto text-sm">{{ result.klipper_config }}</pre>
        </div>

        <!-- Usage Guide -->
        <div class="bg-yellow-50 dark:bg-yellow-900/20 rounded-lg p-4 border border-yellow-200 dark:border-yellow-800">
          <h4 class="text-md font-semibold text-yellow-900 dark:text-yellow-100 mb-2">
            📝 Next Steps
          </h4>
          <pre class="text-sm text-yellow-800 dark:text-yellow-200 whitespace-pre-line">{{ result.usage_guide }}</pre>
        </div>

        <!-- Understanding Offsets -->
        <div class="bg-purple-50 dark:bg-purple-900/20 rounded-lg p-4 border border-purple-200 dark:border-purple-800">
          <h4 class="text-md font-semibold text-purple-900 dark:text-purple-100 mb-2">
            💡 Understanding the Values
          </h4>
          <div class="text-sm text-purple-800 dark:text-purple-200 space-y-2">
            <p><strong>Negative X offset:</strong> Probe is to the left of the nozzle (most common)</p>
            <p><strong>Positive X offset:</strong> Probe is to the right of the nozzle</p>
            <p><strong>Negative Y offset:</strong> Probe is in front of the nozzle (most common)</p>
            <p><strong>Positive Y offset:</strong> Probe is behind the nozzle</p>
            <p class="pt-2 border-t border-purple-200 dark:border-purple-700">
              <strong>Why it matters:</strong> Accurate offsets ensure the bed mesh is measured correctly and the nozzle is positioned exactly where Klipper expects it to be. This is critical for first layer adhesion.
            </p>
          </div>
        </div>

        <!-- Reference Link -->
        <div class="text-center">
          <a
            :href="result.reference"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
          >
            📚 Read More: Klipper Probe Calibration Documentation
          </a>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useCalculatorStore } from '~/stores/calculator'
import type { XAndYOffsetsRequest } from '~/types/calculators'

const calculatorStore = useCalculatorStore()

// Form inputs
const toolheadXProbe = ref<number | null>(null)
const toolheadYProbe = ref<number | null>(null)
const toolheadXNozzle = ref<number | null>(null)
const toolheadYNozzle = ref<number | null>(null)

// UI state
const loading = ref(false)
const error = ref<string | null>(null)
const copied = ref(false)

// Results
const result = computed(() => calculatorStore.xAndYOffsets.result)

const allFieldsFilled = computed(() => {
  return toolheadXProbe.value !== null &&
         toolheadYProbe.value !== null &&
         toolheadXNozzle.value !== null &&
         toolheadYNozzle.value !== null
})

const handleCalculate = async () => {
  if (!allFieldsFilled.value) {
    error.value = 'Please fill in all four toolhead positions'
    return
  }

  loading.value = true
  error.value = null

  try {
    const request: XAndYOffsetsRequest = {
      toolhead_x_probe: toolheadXProbe.value!,
      toolhead_y_probe: toolheadYProbe.value!,
      toolhead_x_nozzle: toolheadXNozzle.value!,
      toolhead_y_nozzle: toolheadYNozzle.value!,
    }

    await calculatorStore.calculateXAndYOffsets(request)
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || 'Calculation failed'
  } finally {
    loading.value = false
  }
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

code {
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}
</style>
