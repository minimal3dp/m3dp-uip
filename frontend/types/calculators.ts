// Calculator types matching backend Pydantic models

export interface RotationDistanceRequest {
  current_rotation_distance: number
  requested_extrusion: number
  actual_extrusion: number
}

export interface RotationDistanceResponse {
  new_rotation_distance: number
  change_percent: number
  within_tolerance: boolean
  klipper_config: string
  recommendation: string
}

export interface OrcaSlicerFlowRequest {
  old_flow_rate: number
  pass_1_slide_value: number
  pass_2_slide_value?: number
}

export interface OrcaSlicerFlowResponse {
  pass_1_flow: number
  pass_2_flow: number | null
  change_from_original: number
  slicer_config: string
  recommendation: string
}

export interface OrcaSlicerFlowYoloRequest {
  old_flow_rate: number
  yolo_slide_value: number
}

export interface OrcaSlicerFlowYoloResponse {
  new_flow: number
  change_from_original: number
  slicer_config: string
  recommendation: string
}

export interface PressureAdvanceRequest {
  material_type: string
  current_pa?: number
  print_speed: number
  nozzle_diameter: number
}

export interface PressureAdvanceResponse {
  recommended_range: [number, number]
  start_value: number
  increment: number
  test_parameters: {
    start_pa: number
    end_pa: number
    increment: number
    speed: number
    layer_height: number
    line_width: number
    nozzle_diameter: number
  }
  klipper_config: string
  calibration_method: string
}

export interface InputShapingRequest {
  test_type: string
  x_frequency: number
  y_frequency: number
}

export interface InputShapingResponse {
  shaper_x: string
  shaper_y: string
  max_accel: number
  square_corner_velocity: number
  klipper_config: string
  notes: string
}
