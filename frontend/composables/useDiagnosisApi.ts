// API composable for diagnosis endpoints
export const useDiagnosisApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const analyzeImage = async (file: File, context?: {
    printer_model?: string
    filament_type?: string
    filament_color?: string
    slicer?: string
    nozzle_size?: number
  }) => {
    const formData = new FormData()
    formData.append('file', file)

    if (context) {
      Object.entries(context).forEach(([key, value]) => {
        if (value !== undefined) {
          formData.append(key, String(value))
        }
      })
    }

    return await $fetch<any>(`${apiBase}/api/v1/diagnosis/analyze/image`, {
      method: 'POST',
      body: formData,
    })
  }

  const analyzeText = async (query: string, context?: {
    printer_model?: string
    filament_type?: string
    filament_color?: string
    slicer?: string
    nozzle_size?: number
  }) => {
    return await $fetch<any>(`${apiBase}/api/v1/diagnosis/analyze/text`, {
      method: 'POST',
      body: {
        query,
        ...context,
      },
    })
  }

  return {
    analyzeImage,
    analyzeText,
  }
}
