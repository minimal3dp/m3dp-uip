<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">💬</span>
      Describe Your Issue
    </h2>

    <p class="text-zinc-400 mb-8">
      Describe what's wrong with your print. Be specific about the defect type and when it occurs.
    </p>

    <textarea
      v-model="store.textQuery"
      rows="6"
      placeholder="Example: My prints have visible layer lines with gaps between them. The first layer looks good but issues start around layer 10. Using PLA at 200°C/60°C."
      class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 focus:outline-none focus:border-brand-orange transition resize-none"
    ></textarea>

    <!-- Context Inputs (Same as Image Upload) -->
    <div class="mt-6 glass-dark rounded-xl p-6">
      <h3 class="text-lg font-semibold mb-4">Additional Context (Optional)</h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium mb-2">Printer Model</label>
          <input
            v-model="store.context.printerModel"
            type="text"
            placeholder="e.g., Ender 3 V2"
            class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-brand-orange transition text-sm"
          />
        </div>

        <div>
          <label class="block text-sm font-medium mb-2">Filament Type</label>
          <select
            v-model="store.context.filamentType"
            class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-brand-orange transition text-sm"
          >
            <option value="PLA">PLA</option>
            <option value="PETG">PETG</option>
            <option value="ABS">ABS</option>
            <option value="TPU">TPU</option>
            <option value="ASA">ASA</option>
            <option value="NYLON">Nylon</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium mb-2">Slicer</label>
          <select
            v-model="store.context.slicer"
            class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-brand-orange transition text-sm"
          >
            <option value="OrcaSlicer">OrcaSlicer</option>
            <option value="PrusaSlicer">PrusaSlicer</option>
            <option value="Cura">Cura</option>
            <option value="SuperSlicer">SuperSlicer</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium mb-2">Nozzle Size (mm)</label>
          <input
            v-model.number="store.context.nozzleSize"
            type="number"
            step="0.1"
            min="0.1"
            max="2"
            class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-brand-orange transition text-sm"
          />
        </div>
      </div>
    </div>

    <!-- Error Message -->
    <div v-if="store.error" class="mt-6 bg-red-500/10 border border-red-500/50 rounded-lg p-4 text-red-400 text-sm">
      {{ store.error }}
    </div>

    <!-- Analyze Button -->
    <button
      @click="store.analyzeText()"
      :disabled="!store.textQuery.trim() || store.loading"
      class="w-full mt-6 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-4 rounded-lg font-medium transition text-lg"
    >
      {{ store.loading ? 'Analyzing...' : '✨ Analyze Issue' }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { useDiagnosisStore } from '~/stores/diagnosis'

const store = useDiagnosisStore()
</script>
