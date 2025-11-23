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

export interface InputShapingRequest {
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

export interface MaxVolumetricSpeedRequest {
  start_value: number
  step_value: number
  height_measured: number
  temperature?: number
  hotend_type?: string
}

export interface MaxVolumetricSpeedResponse {
  max_flow: number
  safe_flow_95: number
  safe_flow_90: number
  comparison: {
    your_max_flow: number
    closest_hotend: string
    closest_flow: number
    common_hotends: Record<string, number>
  }
  slicer_config: string
  recommendation: string
  test_details: {
    start_value: number
    step_value: number
    height_measured: number
    temperature?: number
    hotend_type?: string
  }
}

export interface RunCurrentRequest {
  peak_current: number
  motor_model?: string
  driver_type: string
}

export interface RunCurrentResponse {
  run_current: number
  peak_current: number
  rms_factor: number
  driver_max: number
  within_limits: boolean
  klipper_config: string
  recommendation: string
  reference: string
}

export interface LeadScrewRotationDistanceRequest {
  pitch: number
  number_of_threads: number
  screw_type?: string
}

export interface LeadScrewRotationDistanceResponse {
  rotation_distance: number
  pitch: number
  number_of_threads: number
  common_examples: Record<string, number>
  klipper_config: string
  recommendation: string
  reference: string
}
