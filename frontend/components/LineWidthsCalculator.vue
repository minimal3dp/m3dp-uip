<template>
  <div class="line-widths-calculator bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Line Width Recommendations</h2>
    <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">
      Suggests a safe and effective line width range for a given nozzle diameter and feature type.
    </p>

    <form @submit.prevent="handleCalculate" class="space-y-4 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label for="nozzle" class="block text-sm font-medium mb-1">Nozzle Diameter (mm)</label>
          <input id="nozzle" v-model.number="nozzleDiameter" type="number" step="0.01" min="0.1" max="2" class="w-full px-3 py-2 rounded border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white" />
        </div>
        <div>
          <label for="feature" class="block text-sm font-medium mb-1">Feature Type</label>
          <select id="feature" v-model="featureType" class="w-full px-3 py-2 rounded border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white">
            <option value="external_perimeter">External Perimeter</option>
            <option value="perimeter">Perimeter</option>
            <option value="solid_infill">Solid Infill</option>
            <option value="sparse_infill">Sparse Infill</option>
            <option value="first_layer">First Layer</option>
            <option value="support">Support</option>
          </select>
        </div>
      </div>
      <button type="submit" :disabled="loading" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 rounded transition-colors">
        {{ loading ? 'Calculating...' : 'Calculate Recommended Range' }}
      </button>
    </form>

    <div v-if="error" class="bg-red-50 dark:bg-red-900/30 border border-red-300 dark:border-red-700 text-red-700 dark:text-red-200 text-sm rounded p-3 mb-6">{{ error }}</div>

    <div v-if="result" class="space-y-4">
      <div class="bg-gradient-to-r from-indigo-50 to-blue-50 dark:from-indigo-900/20 dark:to-blue-900/20 border border-indigo-200 dark:border-indigo-800 rounded p-4">
        <h3 class="text-lg font-semibold mb-2 text-indigo-900 dark:text-indigo-100">Recommended Range</h3>
        <p class="text-sm text-gray-700 dark:text-gray-300 mb-2">Feature: <span class="font-medium">{{ featureLabel }}</span></p>
        <div class="flex flex-wrap gap-4 items-center">
          <div class="text-center">
            <p class="text-xs uppercase tracking-wide text-gray-500 dark:text-gray-400">Min</p>
            <p class="text-xl font-bold text-indigo-600 dark:text-indigo-300">{{ result.recommended_min.toFixed(3) }} mm</p>
          </div>
          <div class="text-center">
            <p class="text-xs uppercase tracking-wide text-gray-500 dark:text-gray-400">Target</p>
            <p class="text-xl font-bold text-blue-600 dark:text-blue-300">{{ result.default_target.toFixed(3) }} mm</p>
          </div>
          <div class="text-center">
            <p class="text-xs uppercase tracking-wide text-gray-500 dark:text-gray-400">Max</p>
            <p class="text-xl font-bold text-indigo-600 dark:text-indigo-300">{{ result.recommended_max.toFixed(3) }} mm</p>
          </div>
        </div>
      </div>

      <div class="bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded p-4">
        <h4 class="text-md font-semibold mb-2 text-gray-900 dark:text-white">Slicer Config Example</h4>
        <pre class="bg-black/90 text-green-400 text-xs p-3 rounded overflow-x-auto">{{ result.slicer_config }}</pre>
      </div>

      <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded p-4">
        <h4 class="text-md font-semibold mb-2 text-gray-900 dark:text-white">Notes</h4>
        <p class="text-sm text-gray-700 dark:text-gray-300 whitespace-pre-line">{{ result.notes }}</p>
        <p class="text-xs mt-2 text-gray-500 dark:text-gray-400">Flow hint: {{ result.extrusion_multiplier_hint }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useCalculatorStore } from '~/stores/calculator'
import type { LineWidthsRequest } from '~/types/calculators'

const store = useCalculatorStore()

const nozzleDiameter = ref<number>(store.lineWidths.nozzleDiameter || 0.4)
const featureType = ref<string>(store.lineWidths.featureType)
const loading = computed(() => store.loading)
const error = computed(() => store.error)
const result = computed(() => store.lineWidths.result)

const featureLabel = computed(() => {
  const map: Record<string,string> = {
    external_perimeter: 'External Perimeter',
    perimeter: 'Perimeter',
    solid_infill: 'Solid Infill',
    sparse_infill: 'Sparse Infill',
    first_layer: 'First Layer',
    support: 'Support'
  }
  return map[featureType.value] || featureType.value
})

async function handleCalculate() {
  const req: LineWidthsRequest = {
    nozzle_diameter: nozzleDiameter.value,
    feature_type: featureType.value,
  }
  try {
    await store.calculateLineWidths(req)
  } catch (_) {}
}
</script>

<style scoped>
.line-widths-calculator input:disabled {
  opacity: 0.6;
}
</style>
