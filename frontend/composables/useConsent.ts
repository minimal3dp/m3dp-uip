import { ref } from 'vue'

const CONSENT_KEY = 'm3dp_analytics_consent'
const consent = ref<boolean | null>(null)

function readConsent(): boolean | null {
  if (typeof window === 'undefined') return null
  const raw = window.localStorage.getItem(CONSENT_KEY)
  if (raw === 'granted') return true
  if (raw === 'denied') return false
  return null
}

function writeConsent(value: boolean) {
  if (typeof window === 'undefined') return
  window.localStorage.setItem(CONSENT_KEY, value ? 'granted' : 'denied')
  consent.value = value
}

export const useConsent = () => {
  if (consent.value === null) {
    consent.value = readConsent()
  }
  return { consent, setConsent: writeConsent }
}
