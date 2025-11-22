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
  orcaSlicerFlow: {
    oldFlowRate: number
    pass1SlideValue: number | null
    pass2SlideValue: number | null
    result: any | null
  }
  orcaSlicerFlowYolo: {
    oldFlowRate: number
    yoloSlideValue: number | null
    result: any | null
  }
  inputShaping: {
    testType: string
    xFrequency: number | null
    yFrequency: number | null
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
    orcaSlicerFlow: {
      oldFlowRate: 1.0,
      pass1SlideValue: null,
      pass2SlideValue: null,
      result: null,
    },
    orcaSlicerFlowYolo: {
      oldFlowRate: 1.0,
      yoloSlideValue: null,
      result: null,
    },
    inputShaping: {
      testType: 'ADXL345',
      xFrequency: null,
      yFrequency: null,
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

    async calculateOrcaSlicerFlowYolo() {
      if (!this.orcaSlicerFlowYolo.yoloSlideValue) {
        this.error = 'Please enter the YOLO slide value'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateOrcaSlicerFlowYolo({
          old_flow_rate: this.orcaSlicerFlowYolo.oldFlowRate,
          yolo_slide_value: this.orcaSlicerFlowYolo.yoloSlideValue,
        })
        this.orcaSlicerFlowYolo.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetPressureAdvance() {
      this.pressureAdvance.currentPa = null
      this.pressureAdvance.result = null
      this.error = null
    },

    resetOrcaSlicerFlowYolo() {
      this.orcaSlicerFlowYolo.yoloSlideValue = null
      this.orcaSlicerFlowYolo.result = null
      this.error = null
    },

    async calculateOrcaSlicerFlow() {
      if (!this.orcaSlicerFlow.pass1SlideValue) {
        this.error = 'Please enter Pass 1 slide value'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateOrcaSlicerFlow({
          old_flow_rate: this.orcaSlicerFlow.oldFlowRate,
          pass_1_slide_value: this.orcaSlicerFlow.pass1SlideValue,
          pass_2_slide_value: this.orcaSlicerFlow.pass2SlideValue || undefined,
        })
        this.orcaSlicerFlow.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetOrcaSlicerFlow() {
      this.orcaSlicerFlow.pass1SlideValue = null
      this.orcaSlicerFlow.pass2SlideValue = null
      this.orcaSlicerFlow.result = null
      this.error = null
    },

    async calculateInputShaping() {
      if (!this.inputShaping.xFrequency || !this.inputShaping.yFrequency) {
        this.error = 'Please enter both X and Y frequencies'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateInputShaping({
          x_frequency: this.inputShaping.xFrequency,
          y_frequency: this.inputShaping.yFrequency,
        })
        this.inputShaping.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetInputShaping() {
      this.inputShaping.xFrequency = null
      this.inputShaping.yFrequency = null
      this.inputShaping.result = null
      this.error = null
    },
  },
})
