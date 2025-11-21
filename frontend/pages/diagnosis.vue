<template>
  <NuxtLayout>
    <div class="max-w-4xl mx-auto p-6">
      <!-- Header -->
      <div class="mb-12 text-center">
        <h1 class="text-4xl font-bold mb-4">AI Diagnostic Assistant</h1>
        <p class="text-zinc-400 max-w-xl mx-auto">
          Upload a photo of your failed print or describe the issue. Our AI will analyze it using the Minimal 3DP Knowledge Base.
        </p>
      </div>

      <!-- Mode Toggle -->
      <div class="flex justify-center mb-8">
        <div class="glass rounded-xl p-1 flex gap-1">
          <button
            @click="store.setMode('image')"
            :class="[
              'px-6 py-3 rounded-lg font-medium transition',
              store.mode === 'image'
                ? 'bg-brand-orange text-white'
                : 'text-zinc-400 hover:text-white'
            ]"
          >
            📸 Upload Photo
          </button>
          <button
            @click="store.setMode('text')"
            :class="[
              'px-6 py-3 rounded-lg font-medium transition',
              store.mode === 'text'
                ? 'bg-brand-orange text-white'
                : 'text-zinc-400 hover:text-white'
            ]"
          >
            💬 Describe Issue
          </button>
        </div>
      </div>

      <!-- Input Components -->
      <div class="mb-8">
        <ImageUpload v-if="store.mode === 'image'" />
        <TextInput v-else />
      </div>

      <!-- Results -->
      <ResultsDisplay />

      <!-- Info Box -->
      <div v-if="!store.result" class="mt-8 text-center text-zinc-500 text-sm glass-dark rounded-xl p-6">
        <p class="mb-2">💡 <strong>Pro Tip:</strong> Include printer model, filament type, and slicer settings for better results</p>
        <p>Powered by Gemini Vision AI + Semantic Router</p>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { useDiagnosisStore } from '~/stores/diagnosis'

const store = useDiagnosisStore()
</script>
