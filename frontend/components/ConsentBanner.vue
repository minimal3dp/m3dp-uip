<template>
  <div v-if="show" class="fixed bottom-4 left-0 right-0 flex justify-center px-4 z-50">
    <div class="glass-dark backdrop-blur-md border border-white/10 rounded-xl max-w-xl w-full p-4 flex flex-col md:flex-row md:items-center gap-4">
      <div class="text-sm text-zinc-300 flex-1">
        We use minimal analytics (GA4) to improve calibration tools. No personal data; events are calculator usage only.
      </div>
      <div class="flex gap-3">
        <button @click="deny" class="px-4 py-2 text-sm bg-zinc-800 hover:bg-zinc-700 rounded-lg">Decline</button>
        <button @click="accept" class="px-4 py-2 text-sm bg-brand-orange hover:bg-orange-600 text-white rounded-lg">Allow</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useConsent } from '~/composables/useConsent'

const { consent, setConsent } = useConsent()
const show = computed(() => consent.value === null)

const accept = () => setConsent(true)
const deny = () => setConsent(false)
</script>
