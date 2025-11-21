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
