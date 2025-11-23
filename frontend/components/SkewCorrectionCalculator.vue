<template>
  <div class="skew-correction-calculator bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
      Skew Correction Calculator
    </h2>
    <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">
      Calculate printer frame skew from calibration print measurements. Corrects dimensional inaccuracy caused by frame misalignment.
      <a
        href="https://www.klipper3d.org/Skew_Correction.html"
        target="_blank"
        rel="noopener noreferrer"
        class="text-blue-600 dark:text-blue-400 hover:underline"
      >
        Reference: Klipper Docs
      </a>
    </p>

    <!-- Instructions -->
    <div class="bg-purple-50 dark:bg-purple-900/20 rounded-lg p-4 mb-6 border border-purple-200 dark:border-purple-800">
      <h3 class="text-md font-semibold text-purple-900 dark:text-purple-100 mb-2">
        📐 Calibration Steps
      </h3>
      <ol class="text-sm text-purple-800 dark:text-purple-200 space-y-1 list-decimal list-inside">
        <li>Print calibration model: <a href="https://www.thingiverse.com/thing:2972743/" target="_blank" class="underline">Thingiverse #2972743</a></li>
        <li>Measure with calipers (±0.01mm precision recommended)</li>
        <li>For each plane, measure: AC diagonal, BD diagonal, AD orthogonal</li>
        <li>XY plane is always required; XZ and YZ are optional but recommended</li>
      </ol>
    </div>

    <!-- Input Form -->
    <form @submit.prevent="handleCalculate" class="space-y-6 mb-6">
      <!-- XY Plane (Required) -->
      <div class="border border-blue-300 dark:border-blue-700 rounded-lg p-4 bg-blue-50 dark:bg-blue-900/10">
        <h3 class="text-lg font-semibold text-blue-900 dark:text-blue-100 mb-3">
          XY Plane (Bed) - Required
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label for="xy-ac" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AC Diagonal (mm) *
            </label>
            <input
              id="xy-ac"
              v-model.number="xyAc"
              type="number"
              step="0.01"
              required
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 141.21"
            />
          </div>
          <div>
            <label for="xy-bd" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              BD Diagonal (mm) *
            </label>
            <input
              id="xy-bd"
              v-model.number="xyBd"
              type="number"
              step="0.01"
              required
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 140.97"
            />
          </div>
          <div>
            <label for="xy-ad" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AD Orthogonal (mm) *
            </label>
            <input
              id="xy-ad"
              v-model.number="xyAd"
              type="number"
              step="0.01"
              required
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 104.77"
            />
          </div>
        </div>
      </div>

      <!-- XZ Plane (Optional) -->
      <div class="border border-green-300 dark:border-green-700 rounded-lg p-4 bg-green-50 dark:bg-green-900/10">
        <h3 class="text-lg font-semibold text-green-900 dark:text-green-100 mb-3">
          XZ Plane (Left Side) - Optional
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label for="xz-ac" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AC Diagonal (mm)
            </label>
            <input
              id="xz-ac"
              v-model.number="xzAc"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-green-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 141.98"
            />
          </div>
          <div>
            <label for="xz-bd" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              BD Diagonal (mm)
            </label>
            <input
              id="xz-bd"
              v-model.number="xzBd"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-green-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 141.63"
            />
          </div>
          <div>
            <label for="xz-ad" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AD Orthogonal (mm)
            </label>
            <input
              id="xz-ad"
              v-model.number="xzAd"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-green-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 104.90"
            />
          </div>
        </div>
      </div>

      <!-- YZ Plane (Optional) -->
      <div class="border border-orange-300 dark:border-orange-700 rounded-lg p-4 bg-orange-50 dark:bg-orange-900/10">
        <h3 class="text-lg font-semibold text-orange-900 dark:text-orange-100 mb-3">
          YZ Plane (Right Side) - Optional
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label for="yz-ac" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AC Diagonal (mm)
            </label>
            <input
              id="yz-ac"
              v-model.number="yzAc"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-orange-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 141.54"
            />
          </div>
          <div>
            <label for="yz-bd" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              BD Diagonal (mm)
            </label>
            <input
              id="yz-bd"
              v-model.number="yzBd"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-orange-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 141.33"
            />
          </div>
          <div>
            <label for="yz-ad" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              AD Orthogonal (mm)
            </label>
            <input
              id="yz-ad"
              v-model.number="yzAd"
              type="number"
              step="0.01"
              class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-orange-500 dark:bg-gray-700 dark:text-white"
              placeholder="e.g., 104.83"
            />
          </div>
        </div>
      </div>

      <!-- Calculate Button -->
      <button
        type="submit"
        :disabled="loading || !xyFieldsFilled"
        class="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-3 px-4 rounded-md transition-colors duration-200"
      >
        {{ loading ? 'Calculating...' : 'Calculate Skew Correction' }}
      </button>
    </form>

    <!-- Error Display -->
    <div v-if="error" class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-md p-4 mb-6">
      <p class="text-red-800 dark:text-red-200 text-sm">{{ error }}</p>
    </div>

    <!-- Results Display -->
    <transition name="fade">
      <div v-if="result" class="space-y-6">
        <!-- Interpretation -->
        <div class="bg-gradient-to-r from-purple-50 to-blue-50 dark:from-purple-900/20 dark:to-blue-900/20 rounded-lg p-6 border border-purple-200 dark:border-purple-800">
          <h3 class="text-lg font-semibold mb-3 text-gray-900 dark:text-white">
            📊 Skew Analysis
          </h3>
          <p class="text-gray-800 dark:text-gray-200 mb-4">{{ result.interpretation }}</p>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
            <div v-for="(plane, key) in result.skew_profile" :key="key" class="bg-white dark:bg-gray-800 rounded-lg p-4">
              <p class="text-sm font-medium text-gray-600 dark:text-gray-400">{{ key }} Plane</p>
              <p class="text-2xl font-bold text-purple-600 dark:text-purple-400">{{ plane.degrees }}°</p>
              <p class="text-xs text-gray-500 dark:text-gray-500">{{ plane.radians }} radians</p>
            </div>
          </div>
        </div>

        <!-- SET_SKEW Command -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex justify-between items-center mb-2">
            <h4 class="text-md font-semibold text-gray-900 dark:text-white">SET_SKEW Command</h4>
            <button
              @click="copyToClipboard(result.set_skew_command)"
              class="text-sm bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-md transition-colors duration-200"
            >
              {{ copiedSetSkew ? '✓ Copied!' : 'Copy' }}
            </button>
          </div>
          <pre class="bg-gray-900 dark:bg-black text-green-400 p-4 rounded-md overflow-x-auto text-sm">{{ result.set_skew_command }}</pre>
        </div>

        <!-- CALC_MEASURED_SKEW Commands -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
          <h4 class="text-md font-semibold text-gray-900 dark:text-white mb-3">CALC_MEASURED_SKEW Commands (for testing)</h4>
          <div class="space-y-2">
            <div v-for="(cmd, plane) in result.calc_measured_skew_commands" :key="plane">
              <div class="flex justify-between items-center mb-1">
                <p class="text-sm font-medium text-gray-700 dark:text-gray-300">{{ plane }} Plane:</p>
                <button
                  @click="copyToClipboard(cmd, String(plane))"
                  class="text-xs bg-gray-600 hover:bg-gray-700 text-white px-2 py-1 rounded transition-colors duration-200"
                >
                  {{ copiedCalc === String(plane) ? '✓' : 'Copy' }}
                </button>
              </div>
              <pre class="bg-gray-900 dark:bg-black text-yellow-400 p-2 rounded text-xs overflow-x-auto">{{ cmd }}</pre>
            </div>
          </div>
        </div>

        <!-- Usage Guide -->
        <div class="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 border border-blue-200 dark:border-blue-800">
          <h4 class="text-md font-semibold text-blue-900 dark:text-blue-100 mb-2">
            📝 Implementation Steps
          </h4>
          <pre class="text-sm text-blue-800 dark:text-blue-200 whitespace-pre-line">{{ result.usage_guide }}</pre>
        </div>

        <!-- Reference Links -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-center">
          <a
            :href="result.calibration_model"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
          >
            🖨️ Download Calibration Model (Thingiverse)
          </a>
          <a
            :href="result.reference"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
          >
            📚 Read More: Klipper Skew Correction Documentation
          </a>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useCalculatorStore } from '~/stores/calculator'
import type { SkewCorrectionRequest } from '~/types/calculators'

const calculatorStore = useCalculatorStore()

// Form inputs - XY Plane (required)
const xyAc = ref<number | null>(null)
const xyBd = ref<number | null>(null)
const xyAd = ref<number | null>(null)

// XZ Plane (optional)
const xzAc = ref<number | null>(null)
const xzBd = ref<number | null>(null)
const xzAd = ref<number | null>(null)

// YZ Plane (optional)
const yzAc = ref<number | null>(null)
const yzBd = ref<number | null>(null)
const yzAd = ref<number | null>(null)

// UI state
const loading = ref(false)
const error = ref<string | null>(null)
const copiedSetSkew = ref(false)
const copiedCalc = ref<string | null>(null)

// Results
const result = computed(() => calculatorStore.skewCorrection.result)

const xyFieldsFilled = computed(() => {
  return xyAc.value !== null && xyBd.value !== null && xyAd.value !== null
})

const handleCalculate = async () => {
  if (!xyFieldsFilled.value) {
    error.value = 'Please fill in all XY plane measurements (required)'
    return
  }

  loading.value = true
  error.value = null

  try {
    const request: SkewCorrectionRequest = {
      xy_ac: xyAc.value!,
      xy_bd: xyBd.value!,
      xy_ad: xyAd.value!,
    }

    // Add XZ plane if all three values are present
    if (xzAc.value !== null && xzBd.value !== null && xzAd.value !== null) {
      request.xz_ac = xzAc.value
      request.xz_bd = xzBd.value
      request.xz_ad = xzAd.value
    }

    // Add YZ plane if all three values are present
    if (yzAc.value !== null && yzBd.value !== null && yzAd.value !== null) {
      request.yz_ac = yzAc.value
      request.yz_bd = yzBd.value
      request.yz_ad = yzAd.value
    }

    await calculatorStore.calculateSkewCorrection(request)
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || 'Calculation failed'
  } finally {
    loading.value = false
  }
}

const copyToClipboard = async (text: string, plane?: string) => {
  try {
    await navigator.clipboard.writeText(text)

    if (text.startsWith('SET_SKEW')) {
      copiedSetSkew.value = true
      setTimeout(() => {
        copiedSetSkew.value = false
      }, 2000)
    } else if (plane) {
      copiedCalc.value = plane
      setTimeout(() => {
        copiedCalc.value = null
      }, 2000)
    }
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
