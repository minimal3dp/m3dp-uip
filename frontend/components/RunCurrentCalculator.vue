<template>
  <div class="run-current-calculator bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
      Run Current Calculator
    </h2>
    <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">
      Calculate proper run_current for TMC stepper drivers (TMC2209/2208/5160) from motor peak current.
      <a
        href="https://docs.vorondesign.com/community/howto/120decibell/calculating_driver_current.html"
        target="_blank"
        rel="noopener noreferrer"
        class="text-blue-600 dark:text-blue-400 hover:underline"
      >
        Reference: Voron Docs
      </a>
    </p>

    <!-- Input Form -->
    <form @submit.prevent="handleCalculate" class="space-y-4 mb-6">
      <!-- Peak Current -->
      <div>
        <label for="peak-current" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Peak Current (A) *
        </label>
        <input
          id="peak-current"
          v-model.number="peakCurrent"
          type="number"
          step="0.1"
          min="0.5"
          max="3.0"
          required
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="e.g., 1.5, 2.0"
        />
        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
          Find this value in your stepper motor's datasheet (typically 1.5A - 2.5A for NEMA17)
        </p>
      </div>

      <!-- Driver Type -->
      <div>
        <label for="driver-type" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          TMC Driver Type
        </label>
        <select
          id="driver-type"
          v-model="driverType"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
        >
          <option value="TMC2209">TMC2209 (Max 1.2A)</option>
          <option value="TMC2208">TMC2208 (Max 1.4A)</option>
          <option value="TMC5160">TMC5160 (Max 3.0A)</option>
        </select>
      </div>

      <!-- Motor Model (Optional) -->
      <div>
        <label for="motor-model" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Motor Model (Optional)
        </label>
        <input
          id="motor-model"
          v-model="motorModel"
          type="text"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="e.g., NEMA17 17HS19-2004S1"
        />
      </div>

      <!-- Calculate Button -->
      <button
        type="submit"
        :disabled="loading || !peakCurrent"
        class="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-2 px-4 rounded-md transition-colors duration-200"
      >
        {{ loading ? 'Calculating...' : 'Calculate Run Current' }}
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
            Calculated Run Current
          </h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">Peak Current</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ result.peak_current.toFixed(2) }}A</p>
            </div>
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">RMS Factor</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ result.rms_factor }}</p>
            </div>
            <div class="col-span-2 mt-2">
              <p class="text-sm text-gray-600 dark:text-gray-400">Run Current (Result)</p>
              <p class="text-4xl font-bold text-green-600 dark:text-green-400">{{ result.run_current.toFixed(1) }}A</p>
            </div>
          </div>

          <!-- Driver Limit Warning -->
          <div v-if="!result.within_limits" class="mt-4 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-md p-3">
            <p class="text-yellow-800 dark:text-yellow-200 text-sm font-medium">
              ⚠️ Warning: Calculated value exceeds {{ driverType }} maximum ({{ result.driver_max }}A)
            </p>
          </div>
          <div v-else class="mt-4 bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800 rounded-md p-3">
            <p class="text-green-800 dark:text-green-200 text-sm font-medium">
              ✅ Within {{ driverType }} limits (Max: {{ result.driver_max }}A)
            </p>
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

        <!-- Recommendations -->
        <div class="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 border border-blue-200 dark:border-blue-800">
          <h4 class="text-md font-semibold text-blue-900 dark:text-blue-100 mb-2">
            💡 Tuning Recommendations
          </h4>
          <p class="text-sm text-blue-800 dark:text-blue-200">{{ result.recommendation }}</p>
        </div>

        <!-- Reference Link -->
        <div class="text-center">
          <a
            :href="result.reference"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
          >
            📚 Read More: Voron Documentation
          </a>
        </div>

        <!-- Common Motor Examples -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
          <h4 class="text-md font-semibold text-gray-900 dark:text-white mb-3">Common Motor Examples</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between">
              <span class="text-gray-600 dark:text-gray-400">NEMA17 17HS19-2004S1</span>
              <span class="font-medium text-gray-900 dark:text-white">2.0A peak → 1.4A run</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-600 dark:text-gray-400">LDO 42STH48-2504AH</span>
              <span class="font-medium text-gray-900 dark:text-white">2.5A peak → 1.7A run</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-600 dark:text-gray-400">Moons MS17HD6P4200</span>
              <span class="font-medium text-gray-900 dark:text-white">2.0A peak → 1.4A run</span>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useCalculatorStore } from '~/stores/calculator'
import type { RunCurrentRequest } from '~/types/calculators'

const calculatorStore = useCalculatorStore()

// Form inputs
const peakCurrent = ref<number | null>(null)
const driverType = ref<string>('TMC2209')
const motorModel = ref<string>('')

// UI state
const loading = ref(false)
const error = ref<string | null>(null)
const copied = ref(false)

// Results
const result = computed(() => calculatorStore.runCurrent.result)

const handleCalculate = async () => {
  if (!peakCurrent.value) {
    error.value = 'Please enter peak current'
    return
  }

  loading.value = true
  error.value = null

  try {
    const request: RunCurrentRequest = {
      peak_current: peakCurrent.value,
      driver_type: driverType.value,
      motor_model: motorModel.value || undefined,
    }

    await calculatorStore.calculateRunCurrent(request)
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
</style>
