// API composable for calculator endpoints
import type {
  RotationDistanceRequest,
  RotationDistanceResponse,
  OrcaSlicerFlowRequest,
  OrcaSlicerFlowResponse,
  OrcaSlicerFlowYoloRequest,
  OrcaSlicerFlowYoloResponse,
  PressureAdvanceRequest,
  PressureAdvanceResponse,
  InputShapingRequest,
  InputShapingResponse
} from '~/types/calculators'

export const useCalculatorApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const calculateRotationDistance = async (data: RotationDistanceRequest): Promise<RotationDistanceResponse> => {
    return await $fetch<RotationDistanceResponse>(`${apiBase}/api/v1/calculators/rotation-distance`, {
      method: 'POST',
      body: data,
    })
  }

  const calculateOrcaSlicerFlow = async (data: OrcaSlicerFlowRequest): Promise<OrcaSlicerFlowResponse> => {
    return await $fetch<OrcaSlicerFlowResponse>(`${apiBase}/api/v1/calculators/orcaslicer-flow`, {
      method: 'POST',
      body: data,
    })
  }

  const calculateOrcaSlicerFlowYolo = async (data: OrcaSlicerFlowYoloRequest): Promise<OrcaSlicerFlowYoloResponse> => {
    return await $fetch<OrcaSlicerFlowYoloResponse>(`${apiBase}/api/v1/calculators/orcaslicer-flow-yolo`, {
      method: 'POST',
      body: data,
    })
  }

  const calculatePressureAdvance = async (data: PressureAdvanceRequest): Promise<PressureAdvanceResponse> => {
    return await $fetch<PressureAdvanceResponse>(`${apiBase}/api/v1/calculators/pressure-advance`, {
      method: 'POST',
      body: data,
    })
  }

  const calculateInputShaping = async (data: InputShapingRequest): Promise<InputShapingResponse> => {
    return await $fetch<InputShapingResponse>(`${apiBase}/api/v1/calculators/input-shaping`, {
      method: 'POST',
      body: data,
    })
  }

  const listCalculators = async () => {
    return await $fetch<any>(`${apiBase}/api/v1/calculators`)
  }

  return {
    calculateRotationDistance,
    calculateOrcaSlicerFlow,
    calculateOrcaSlicerFlowYolo,
    calculatePressureAdvance,
    calculateInputShaping,
    listCalculators,
  }
}
