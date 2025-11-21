// Pinia store for diagnosis state
import { defineStore } from 'pinia'
import { useDiagnosisApi } from '~/composables/useDiagnosisApi'

interface DiagnosisState {
  mode: 'image' | 'text'
  imageFile: File | null
  imagePreview: string | null
  textQuery: string
  context: {
    printerModel: string
    filamentType: string
    filamentColor: string
    slicer: string
    nozzleSize: number
  }
  result: any | null
  loading: boolean
  error: string | null
}

export const useDiagnosisStore = defineStore('diagnosis', {
  state: (): DiagnosisState => ({
    mode: 'image',
    imageFile: null,
    imagePreview: null,
    textQuery: '',
    context: {
      printerModel: '',
      filamentType: 'PLA',
      filamentColor: '',
      slicer: 'OrcaSlicer',
      nozzleSize: 0.4,
    },
    result: null,
    loading: false,
    error: null,
  }),

  actions: {
    setMode(mode: 'image' | 'text') {
      this.mode = mode
      this.result = null
      this.error = null
    },

    setImageFile(file: File) {
      this.imageFile = file
      this.imagePreview = URL.createObjectURL(file)
      this.error = null
    },

    clearImage() {
      if (this.imagePreview) {
        URL.revokeObjectURL(this.imagePreview)
      }
      this.imageFile = null
      this.imagePreview = null
    },

    async analyzeImage() {
      if (!this.imageFile) {
        this.error = 'Please upload an image'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useDiagnosisApi()
        const contextData = {
          printer_model: this.context.printerModel || undefined,
          filament_type: this.context.filamentType || undefined,
          filament_color: this.context.filamentColor || undefined,
          slicer: this.context.slicer || undefined,
          nozzle_size: this.context.nozzleSize || undefined,
        }

        this.result = await api.analyzeImage(this.imageFile, contextData)
      } catch (err: any) {
        this.error = err.data?.detail || 'Analysis failed'
        console.error('Image analysis error:', err)
      } finally {
        this.loading = false
      }
    },

    async analyzeText() {
      if (!this.textQuery.trim()) {
        this.error = 'Please describe your issue'
        return
      }

      this.loading = true
      this.error = null

      try {
        const api = useDiagnosisApi()
        const contextData = {
          printer_model: this.context.printerModel || undefined,
          filament_type: this.context.filamentType || undefined,
          filament_color: this.context.filamentColor || undefined,
          slicer: this.context.slicer || undefined,
          nozzle_size: this.context.nozzleSize || undefined,
        }

        this.result = await api.analyzeText(this.textQuery, contextData)
      } catch (err: any) {
        this.error = err.data?.detail || 'Analysis failed'
        console.error('Text analysis error:', err)
      } finally {
        this.loading = false
      }
    },

    reset() {
      this.clearImage()
      this.textQuery = ''
      this.result = null
      this.error = null
    },
  },
})
