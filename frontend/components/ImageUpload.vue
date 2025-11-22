<template>
  <div class="glass rounded-2xl p-8 bg-zinc-900">
    <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
      <span class="text-3xl">📸</span>
      Image Upload
    </h2>

    <p class="text-zinc-400 mb-8">
      Upload a photo of your print failure. Our AI will analyze it and provide recommendations.
    </p>

    <!-- Drag and Drop Zone -->
    <div
      @drop.prevent="handleDrop"
      @dragover.prevent="dragover = true"
      @dragleave.prevent="dragover = false"
      :class="[
        'border-2 border-dashed rounded-xl p-8 text-center transition-all',
        dragover ? 'border-brand-orange bg-brand-orange/10' : 'border-zinc-700 hover:border-zinc-600'
      ]"
    >
      <template v-if="!store.imagePreview">
        <div class="mb-4 text-5xl">📷</div>
        <p class="text-lg mb-2">Drop your image here</p>
        <p class="text-sm text-zinc-500 mb-4">or</p>
        <label class="inline-block">
          <input
            type="file"
            accept="image/*"
            @change="handleFileSelect"
            class="hidden"
          />
          <span class="px-6 py-3 bg-brand-orange hover:bg-orange-600 text-white rounded-lg font-medium cursor-pointer transition inline-block">
            Choose File
          </span>
        </label>
        <p class="text-xs text-zinc-500 mt-4">
          Supports: JPG, PNG, WebP (Max 10MB)
        </p>
      </template>

      <template v-else>
        <img
          :src="store.imagePreview"
          alt="Preview"
          class="max-w-full max-h-64 mx-auto rounded-lg mb-4"
        />
        <button
          @click="store.clearImage()"
          class="px-4 py-2 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg text-sm transition"
        >
          Remove Image
        </button>
      </template>
    </div>

    <!-- Context Inputs (Optional) -->
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
      @click="store.analyzeImage()"
      :disabled="!store.imageFile || store.loading"
      class="w-full mt-6 bg-brand-orange hover:bg-orange-600 disabled:bg-zinc-700 disabled:cursor-not-allowed text-white px-6 py-4 rounded-lg font-medium transition text-lg"
    >
      {{ store.loading ? 'Analyzing...' : '✨ Analyze Defect' }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDiagnosisStore } from '~/stores/diagnosis'

const store = useDiagnosisStore()
const dragover = ref(false)

const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (file) {
    store.setImageFile(file)
  }
}

const handleDrop = (event: DragEvent) => {
  dragover.value = false
  const file = event.dataTransfer?.files[0]
  if (file && file.type.startsWith('image/')) {
    store.setImageFile(file)
  }
}
</script>
