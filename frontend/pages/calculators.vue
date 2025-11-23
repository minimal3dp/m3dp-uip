<template>
  <NuxtLayout>
    <div class="max-w-4xl mx-auto p-6">
      <div class="mb-12 text-center">
        <h1 class="text-4xl font-bold mb-4">Klipper Calibration Tools</h1>
        <p class="text-zinc-400 max-w-xl mx-auto">
          CSV-driven calculators for precise Klipper calibrations. All formulas are directly translated from the Minimal 3DP knowledge base.
        </p>
      </div>

      <div class="space-y-8">
        <!-- Extrusion Calibration -->
        <RotationDistanceCalculator />

        <!-- Flow Rate (Two-Pass Recommended) -->
        <OrcaSlicerFlowCalculator />

        <!-- Flow Rate (YOLO Quick Method) -->
        <OrcaSlicerFlowYoloCalculator />

        <!-- Pressure Advance -->
        <PressureAdvanceCalculator />

        <!-- Input Shaping -->
        <InputShapingCalculator />

        <!-- Max Volumetric Speed -->
        <MaxVolumetricSpeedCalculator />

        <!-- Run Current (TMC Drivers) -->
        <RunCurrentCalculator />

        <!-- Lead Screw Rotation Distance -->
        <LeadScrewRotationDistanceCalculator />

        <!-- X and Y Offsets -->
        <XAndYOffsetsCalculator />
      </div>

      <div class="mt-12 text-center text-zinc-500 text-sm">
        <p>Formulas validated against <a href="https://www.klipper3d.org" target="_blank" class="text-brand-orange hover:underline">Klipper documentation</a> & OrcaSlicer calibration workflow.</p>
        <p class="mt-2">All calculations are deterministic spreadsheet translations — zero LLM hallucinations.</p>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
// Calculators page
</script>
