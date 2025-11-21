// Pinia store for calculator state
import { defineStore } from 'pinia'
import { useCalculatorApi } from '~/composables/useCalculatorApi'

interface CalculatorState {
  rotationDistance: {
    currentRotationDistance: number | null
    requestedExtrusion: number
    actualExtrusion: number | null
    result: any | null
  }
  pressureAdvance: {
    materialType: string
    currentPa: number | null
    printSpeed: number
    nozzleDiameter: number
    result: any | null
  }
  loading: boolean
  error: string | null
}

export const useCalculatorStore = defineStore('calculator', {
  state: (): CalculatorState => ({
    rotationDistance: {
      currentRotationDistance: null,
      requestedExtrusion: 100,
      actualExtrusion: null,
      result: null,
    },
    pressureAdvance: {
      materialType: 'PLA',
      currentPa: null,
      printSpeed: 100,
      nozzleDiameter: 0.4,
      result: null,
    },
    loading: false,
    error: null,
  }),

  actions: {
    async calculateRotationDistance() {
      if (!this.rotationDistance.currentRotationDistance || !this.rotationDistance.actualExtrusion) {
        this.error = 'Please fill in all required fields'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateRotationDistance({
          current_rotation_distance: this.rotationDistance.currentRotationDistance,
          requested_extrusion: this.rotationDistance.requestedExtrusion,
          actual_extrusion: this.rotationDistance.actualExtrusion,
        })
        this.rotationDistance.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    async calculatePressureAdvance() {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculatePressureAdvance({
          material_type: this.pressureAdvance.materialType,
          current_pa: this.pressureAdvance.currentPa || undefined,
          print_speed: this.pressureAdvance.printSpeed,
          nozzle_diameter: this.pressureAdvance.nozzleDiameter,
        })
        this.pressureAdvance.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetRotationDistance() {
      this.rotationDistance.currentRotationDistance = null
      this.rotationDistance.actualExtrusion = null
      this.rotationDistance.result = null
      this.error = null
    },

    resetPressureAdvance() {
      this.pressureAdvance.currentPa = null
      this.pressureAdvance.result = null
      this.error = null
    },
  },
})
