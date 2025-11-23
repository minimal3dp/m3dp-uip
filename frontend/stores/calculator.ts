// Pinia store for calculator state
import { defineStore } from 'pinia'
import { useCalculatorApi } from '~/composables/useCalculatorApi'
import type { XAndYOffsetsRequest, XAndYOffsetsResponse, SkewCorrectionRequest, LineWidthsRequest, LineWidthsResponse } from '~/types/calculators'

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
  maxVolumetricSpeed: {
    startValue: number | null
    stepValue: number | null
    heightMeasured: number | null
    temperature: number | null
    hotendType: string | null
    result: any | null
  }
  runCurrent: {
    peakCurrent: number | null
    motorModel: string | null
    driverType: string
    result: any | null
  }
  leadScrewRotationDistance: {
    pitch: number
    numberOfThreads: number
    screwType: string | null
    result: any | null
  }
  xAndYOffsets: {
    toolheadXProbe: number | null
    toolheadYProbe: number | null
    toolheadXNozzle: number | null
    toolheadYNozzle: number | null
    result: XAndYOffsetsResponse | null
  }
  skewCorrection: {
    xyAc: number | null
    xyBd: number | null
    xyAd: number | null
    xzAc: number | null
    xzBd: number | null
    xzAd: number | null
    yzAc: number | null
    yzBd: number | null
    yzAd: number | null
    result: any | null
  }
  lineWidths: {
    nozzleDiameter: number | null
    featureType: string
    layerHeight: number | null
    result: LineWidthsResponse | null
  }
  paOrcaSlicer: {
    measuredHeight: number | null
    extruderType: string
    result: any | null
  }
  extrusionRateSmoothing: {
    acceleration: number
    lineWidth: number
    layerHeight: number
    result: any | null
  }
  adaptivePressureAdvance: {
    paValues: string
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
    maxVolumetricSpeed: {
      startValue: null,
      stepValue: null,
      heightMeasured: null,
      temperature: null,
      hotendType: null,
      result: null,
    },
    runCurrent: {
      peakCurrent: null,
      motorModel: null,
      driverType: 'TMC2209',
      result: null,
    },
    leadScrewRotationDistance: {
      pitch: 2.0,
      numberOfThreads: 1,
      screwType: null,
      result: null,
    },
    xAndYOffsets: {
      toolheadXProbe: null,
      toolheadYProbe: null,
      toolheadXNozzle: null,
      toolheadYNozzle: null,
      result: null,
    },
    skewCorrection: {
      xyAc: null,
      xyBd: null,
      xyAd: null,
      xzAc: null,
      xzBd: null,
      xzAd: null,
      yzAc: null,
      yzBd: null,
      yzAd: null,
      result: null,
    },
    lineWidths: {
      nozzleDiameter: 0.4,
      featureType: 'perimeter',
      layerHeight: null,
      result: null,
    },
    paOrcaSlicer: {
      measuredHeight: null,
      extruderType: 'direct_drive',
      result: null,
    },
    extrusionRateSmoothing: {
      acceleration: 12000,
      lineWidth: 0.6,
      layerHeight: 0.2,
      result: null,
    },
    adaptivePressureAdvance: {
      paValues: '',
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

    async calculateMaxVolumetricSpeed() {
      if (!this.maxVolumetricSpeed.startValue || !this.maxVolumetricSpeed.stepValue || !this.maxVolumetricSpeed.heightMeasured) {
        this.error = 'Please fill in all required fields'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateMaxVolumetricSpeed({
          start_value: this.maxVolumetricSpeed.startValue,
          step_value: this.maxVolumetricSpeed.stepValue,
          height_measured: this.maxVolumetricSpeed.heightMeasured,
          temperature: this.maxVolumetricSpeed.temperature || undefined,
          hotend_type: this.maxVolumetricSpeed.hotendType || undefined,
        })
        this.maxVolumetricSpeed.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetMaxVolumetricSpeed() {
      this.maxVolumetricSpeed.startValue = null
      this.maxVolumetricSpeed.stepValue = null
      this.maxVolumetricSpeed.heightMeasured = null
      this.maxVolumetricSpeed.temperature = null
      this.maxVolumetricSpeed.hotendType = null
      this.maxVolumetricSpeed.result = null
      this.error = null
    },

    async calculateRunCurrent(request: any) {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateRunCurrent(request)
        this.runCurrent.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
        throw err
      } finally {
        this.loading = false
      }
    },

    resetRunCurrent() {
      this.runCurrent.peakCurrent = null
      this.runCurrent.motorModel = null
      this.runCurrent.driverType = 'TMC2209'
      this.runCurrent.result = null
      this.error = null
    },

    async calculateLeadScrewRotationDistance(request: any) {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateLeadScrewRotationDistance(request)
        this.leadScrewRotationDistance.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
        throw err
      } finally {
        this.loading = false
      }
    },

    resetLeadScrewRotationDistance() {
      this.leadScrewRotationDistance.pitch = 2.0
      this.leadScrewRotationDistance.numberOfThreads = 1
      this.leadScrewRotationDistance.screwType = null
      this.leadScrewRotationDistance.result = null
      this.error = null
    },

    async calculateXAndYOffsets(request: XAndYOffsetsRequest) {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateXAndYOffsets(request)
        this.xAndYOffsets.result = result
      }
      catch (err: any) {
        this.error = err.data?.detail || err.message || 'Failed to calculate X and Y offsets'
        throw err
      }
      finally {
        this.loading = false
      }
    },

    resetXAndYOffsets() {
      this.xAndYOffsets.toolheadXProbe = null
      this.xAndYOffsets.toolheadYProbe = null
      this.xAndYOffsets.toolheadXNozzle = null
      this.xAndYOffsets.toolheadYNozzle = null
      this.xAndYOffsets.result = null
      this.error = null
    },

    async calculateSkewCorrection(request: SkewCorrectionRequest) {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateSkewCorrection(request)
        this.skewCorrection.result = result
      }
      catch (err: any) {
        this.error = err.data?.detail || err.message || 'Failed to calculate skew correction'
        throw err
      }
      finally {
        this.loading = false
      }
    },

    resetSkewCorrection() {
      this.skewCorrection.xyAc = null
      this.skewCorrection.xyBd = null
      this.skewCorrection.xyAd = null
      this.skewCorrection.xzAc = null
      this.skewCorrection.xzBd = null
      this.skewCorrection.xzAd = null
      this.skewCorrection.yzAc = null
      this.skewCorrection.yzBd = null
      this.skewCorrection.yzAd = null
      this.skewCorrection.result = null
      this.error = null
    },

    async calculateLineWidths(request: LineWidthsRequest) {
      this.loading = true
      this.error = null
      try {
        const api = useCalculatorApi()
        const result = await api.calculateLineWidths(request)
        this.lineWidths.result = result
      } catch (err: any) {
        this.error = err.data?.detail || err.message || 'Failed to calculate line widths'
        throw err
      } finally {
        this.loading = false
      }
    },

    resetLineWidths() {
      this.lineWidths.nozzleDiameter = 0.4
      this.lineWidths.featureType = 'perimeter'
      this.lineWidths.layerHeight = null
      this.lineWidths.result = null
      this.error = null
    },

    async calculatePAOrcaSlicer() {
      if (!this.paOrcaSlicer.measuredHeight) {
        this.error = 'Please enter measured height'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculatePAOrcaSlicer({
          measured_height: this.paOrcaSlicer.measuredHeight,
          extruder_type: this.paOrcaSlicer.extruderType,
        })
        this.paOrcaSlicer.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetPAOrcaSlicer() {
      this.paOrcaSlicer.measuredHeight = null
      this.paOrcaSlicer.extruderType = 'direct_drive'
      this.paOrcaSlicer.result = null
      this.error = null
    },

    async calculateExtrusionRateSmoothing() {
      this.loading = true
      this.error = null

      try {
        const api = useCalculatorApi()
        const result = await api.calculateExtrusionRateSmoothing({
          acceleration: this.extrusionRateSmoothing.acceleration,
          line_width: this.extrusionRateSmoothing.lineWidth,
          layer_height: this.extrusionRateSmoothing.layerHeight,
        })
        this.extrusionRateSmoothing.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetExtrusionRateSmoothing() {
      this.extrusionRateSmoothing.acceleration = 12000
      this.extrusionRateSmoothing.lineWidth = 0.6
      this.extrusionRateSmoothing.layerHeight = 0.2
      this.extrusionRateSmoothing.result = null
      this.error = null
    },

    async calculateAdaptivePressureAdvance() {
      if (!this.adaptivePressureAdvance.paValues) {
        this.error = 'Please enter PA values'
        return
      }

      this.loading = true
      this.error = null

      try {
        // Parse comma-separated PA values
        const paArray = this.adaptivePressureAdvance.paValues
          .split(',')
          .map(v => parseFloat(v.trim()))
          .filter(v => !isNaN(v))

        if (paArray.length < 2) {
          this.error = 'Please enter at least 2 PA values'
          return
        }

        const api = useCalculatorApi()
        const result = await api.calculateAdaptivePressureAdvance({
          pa_values: paArray,
        })
        this.adaptivePressureAdvance.result = result
      } catch (err: any) {
        this.error = err.data?.detail || 'Calculation failed'
      } finally {
        this.loading = false
      }
    },

    resetAdaptivePressureAdvance() {
      this.adaptivePressureAdvance.paValues = ''
      this.adaptivePressureAdvance.result = null
      this.error = null
    },
  },
})
