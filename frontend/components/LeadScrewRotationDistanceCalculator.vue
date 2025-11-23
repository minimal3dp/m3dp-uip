<template>
  <div class="lead-screw-calculator bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
      Lead Screw Rotation Distance Calculator
    </h2>
    <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">
      Calculate rotation_distance for Z-axis lead screws. Formula: rotation_distance = pitch × number_of_threads.
      <a
        href="https://www.klipper3d.org/Rotation_Distance.html#axes-with-a-lead-screw"
        target="_blank"
        rel="noopener noreferrer"
        class="text-blue-600 dark:text-blue-400 hover:underline"
      >
        Reference: Klipper Docs
      </a>
    </p>

    <!-- Input Form -->
    <form @submit.prevent="handleCalculate" class="space-y-4 mb-6">
      <!-- Pitch -->
      <div>
        <label for="pitch" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Pitch (mm) *
        </label>
        <input
          id="pitch"
          v-model.number="pitch"
          type="number"
          step="0.5"
          min="0.5"
          max="10"
          required
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="e.g., 2, 8"
        />
        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
          Distance between threads (usually 2mm or 8mm for T8 lead screws)
        </p>
      </div>

      <!-- Number of Threads -->
      <div>
        <label for="threads" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Number of Threads (Starts) *
        </label>
        <select
          id="threads"
          v-model.number="numberOfThreads"
          required
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
        >
          <option :value="1">1 (Single start - most common)</option>
          <option :value="2">2 (Dual start)</option>
          <option :value="4">4 (Quad start)</option>
          <option :value="8">8 (Octo start)</option>
        </select>
        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
          Count the separate grooves at the end of the lead screw
        </p>
      </div>

      <!-- Screw Type (Optional) -->
      <div>
        <label for="screw-type" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Screw Type (Optional)
        </label>
        <input
          id="screw-type"
          v-model="screwType"
          type="text"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="e.g., T8x2, T8x4, T8x8"
        />
      </div>

      <!-- Calculate Button -->
      <button
        type="submit"
        :disabled="loading || !pitch || !numberOfThreads"
        class="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-2 px-4 rounded-md transition-colors duration-200"
      >
        {{ loading ? 'Calculating...' : 'Calculate Rotation Distance' }}
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
            Calculated Rotation Distance
          </h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">Pitch</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ result.pitch }}mm</p>
            </div>
            <div>
              <p class="text-sm text-gray-600 dark:text-gray-400">Number of Threads</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ result.number_of_threads }}</p>
            </div>
            <div class="col-span-2 mt-2">
              <p class="text-sm text-gray-600 dark:text-gray-400">Rotation Distance</p>
              <p class="text-4xl font-bold text-green-600 dark:text-green-400">{{ result.rotation_distance }}mm</p>
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

        <!-- Recommendations -->
        <div class="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 border border-blue-200 dark:border-blue-800">
          <h4 class="text-md font-semibold text-blue-900 dark:text-blue-100 mb-2">
            💡 Understanding Lead Screws
          </h4>
          <p class="text-sm text-blue-800 dark:text-blue-200">{{ result.recommendation }}</p>
        </div>

        <!-- Common Examples -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
          <h4 class="text-md font-semibold text-gray-900 dark:text-white mb-3">Common T8 Lead Screws</h4>
          <div class="space-y-2 text-sm">
            <div v-for="(value, key) in result.common_examples" :key="key" class="flex justify-between">
              <span class="text-gray-600 dark:text-gray-400">{{ key }}</span>
              <span class="font-medium text-gray-900 dark:text-white">{{ value }}mm</span>
            </div>
          </div>
          <div class="mt-4 p-3 bg-yellow-50 dark:bg-yellow-900/20 rounded-md border border-yellow-200 dark:border-yellow-800">
            <p class="text-xs text-yellow-800 dark:text-yellow-200">
              💡 <strong>How to identify:</strong> Look at the end of your lead screw. Count the number of separate grooves/threads you see. That's the number of starts.
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
            📚 Read More: Klipper Rotation Distance Documentation
          </a>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useCalculatorStore } from '~/stores/calculator'
import type { LeadScrewRotationDistanceRequest } from '~/types/calculators'

const calculatorStore = useCalculatorStore()

// Form inputs
const pitch = ref<number>(2.0)
const numberOfThreads = ref<number>(1)
const screwType = ref<string>('')

// UI state
const loading = ref(false)
const error = ref<string | null>(null)
const copied = ref(false)

// Results
const result = computed(() => calculatorStore.leadScrewRotationDistance.result)

const handleCalculate = async () => {
  if (!pitch.value || !numberOfThreads.value) {
    error.value = 'Please enter pitch and number of threads'
    return
  }

  loading.value = true
  error.value = null

  try {
    const request: LeadScrewRotationDistanceRequest = {
      pitch: pitch.value,
      number_of_threads: numberOfThreads.value,
      screw_type: screwType.value || undefined,
    }

    await calculatorStore.calculateLeadScrewRotationDistance(request)
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
