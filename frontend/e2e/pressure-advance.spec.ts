import { test, expect } from '@playwright/test';

/**
 * E2E Tests for Pressure Advance Calculator
 *
 * Tests the complete user flow:
 * 1. Navigate to calculators page
 * 2. Select material type
 * 3. Fill in print parameters
 * 4. Submit calculation
 * 5. Verify material-specific recommendations
 */

test.describe('Pressure Advance Calculator', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to calculators page
    await page.goto('/calculators');

    // Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');
  });

  test('should display pressure advance calculator', async ({ page }) => {
    // Verify calculator heading exists
    await expect(page.getByRole('heading', { name: /pressure advance/i })).toBeVisible();

    // Verify input fields exist
    await expect(page.locator('[data-testid="material-type"]')).toBeVisible();
    await expect(page.locator('[data-testid="current-pa"]')).toBeVisible();
    await expect(page.locator('[data-testid="print-speed"]')).toBeVisible();
    await expect(page.locator('[data-testid="nozzle-diameter"]')).toBeVisible();
  });

  test('should calculate PLA recommendations correctly', async ({ page }) => {
    // Select PLA material (should be default, but explicitly select)
    await page.locator('[data-testid="material-type"]').selectOption('PLA');

    // Fill in print parameters
    await page.locator('[data-testid="print-speed"]').fill('100');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');

    // Submit form
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results to appear
    await page.waitForSelector('[data-testid="pressure-advance-result"]', {
      state: 'visible',
      timeout: 5000
    });

    // Verify PLA-specific range is shown (0.03 - 0.06 from CSV)
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toMatch(/0\.03.*0\.06/); // Match PLA range
    expect(result).toContain('PLA'); // Material name should be shown
  });

  test('should calculate PETG recommendations correctly', async ({ page }) => {
    // Select PETG material
    await page.locator('[data-testid="material-type"]').selectOption('PETG');

    // Fill in print parameters
    await page.locator('[data-testid="print-speed"]').fill('80');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');

    // Submit form
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Verify PETG-specific range is shown (0.06 - 0.08 from CSV)
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toMatch(/0\.06.*0\.08/); // Match PETG range
    expect(result).toContain('PETG');
  });

  test('should calculate TPU recommendations correctly', async ({ page }) => {
    // Select TPU (flexible material with very low PA)
    await page.locator('[data-testid="material-type"]').selectOption('TPU');

    // Fill in print parameters (slower for flexible material)
    await page.locator('[data-testid="print-speed"]').fill('30');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');

    // Submit form
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Verify TPU-specific range is shown (0.0 - 0.02 from CSV - very low for flexible)
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toMatch(/0\.0.*0\.02/); // Match TPU range (flexible materials)
    expect(result).toContain('TPU');
  });

  test('should handle current PA value correctly', async ({ page }) => {
    // Select material
    await page.locator('[data-testid="material-type"]').selectOption('PLA');

    // Fill in current PA (user has already calibrated to 0.045)
    await page.locator('[data-testid="current-pa"]').fill('0.045');
    await page.locator('[data-testid="print-speed"]').fill('100');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');

    // Submit form
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Verify start value reflects current PA
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toContain('0.045'); // Should show current PA as start value
  });

  test('should display test parameters', async ({ page }) => {
    // Fill and calculate
    await page.locator('[data-testid="material-type"]').selectOption('ABS');
    await page.locator('[data-testid="print-speed"]').fill('90');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.6');
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Verify test parameters section is shown
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toContain('90'); // Print speed
    expect(result).toContain('0.6'); // Line width (should match nozzle diameter)
    expect(result).toContain('0.2'); // Layer height (standard from CSV)
  });

  test('should display Klipper config format', async ({ page }) => {
    // Calculate
    await page.locator('[data-testid="material-type"]').selectOption('PLA');
    await page.locator('[data-testid="print-speed"]').fill('100');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for result
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Check if config snippet is shown with pressure_advance keyword
    const configSnippet = page.locator('code, pre').filter({ hasText: /pressure_advance/i });
    await expect(configSnippet).toBeVisible();
  });

  test('should reset form after calculation', async ({ page }) => {
    // Fill and calculate
    await page.locator('[data-testid="material-type"]').selectOption('PETG');
    await page.locator('[data-testid="current-pa"]').fill('0.065');
    await page.locator('[data-testid="print-speed"]').fill('85');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for result
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Click reset button (scoped to pressure advance calculator)
    await page.locator('[data-testid="reset-pa-button"]').click();

    // Verify fields are cleared/reset
    await expect(page.locator('[data-testid="current-pa"]')).toHaveValue('');
    await expect(page.locator('[data-testid="print-speed"]')).toHaveValue('');

    // Verify result is hidden
    await expect(page.getByTestId('pressure-advance-result')).not.toBeVisible();
  });

  test('should require inputs again after reset', async ({ page }) => {
    // Perform initial calculation
    await page.locator('[data-testid="material-type"]').selectOption('PLA');
    await page.locator('[data-testid="print-speed"]').fill('100');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.4');
    await page.locator('[data-testid="calculate-pa-button"]').click();
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Reset
    await page.locator('[data-testid="reset-pa-button"]').click();
    await expect(page.getByTestId('pressure-advance-result')).not.toBeVisible();

    // Attempt to submit again without filling required fields
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Expect validation to prevent result and show required attribute
    const printSpeedInput = page.locator('[data-testid="print-speed"]');
    const nozzleDiameterInput = page.locator('[data-testid="nozzle-diameter"]');
    await expect(printSpeedInput).toHaveAttribute('required');
    await expect(nozzleDiameterInput).toHaveAttribute('required');
    await expect(page.getByTestId('pressure-advance-result')).not.toBeVisible();
  });

  test('should show validation error for empty required fields', async ({ page }) => {
    // Try to submit without filling required fields (print speed and nozzle diameter)
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Expect validation on required fields
    const printSpeedInput = page.locator('[data-testid="print-speed"]');
    const nozzleDiameterInput = page.locator('[data-testid="nozzle-diameter"]');
    
    await expect(printSpeedInput).toHaveAttribute('required');
    await expect(nozzleDiameterInput).toHaveAttribute('required');
  });

  test('should handle different nozzle sizes', async ({ page }) => {
    // Test with 0.6mm nozzle (affects line width in test parameters)
    await page.locator('[data-testid="material-type"]').selectOption('NYLON');
    await page.locator('[data-testid="print-speed"]').fill('60');
    await page.locator('[data-testid="nozzle-diameter"]').fill('0.6');
    await page.locator('[data-testid="calculate-pa-button"]').click();

    // Wait for results
    await expect(page.getByTestId('pressure-advance-result')).toBeVisible({ timeout: 5000 });

    // Verify nozzle diameter is reflected in test parameters
    const result = await page.getByTestId('pressure-advance-result').textContent();
    expect(result).toContain('0.6'); // Should show nozzle diameter in test parameters
  });
});
