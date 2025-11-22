import { test, expect } from '@playwright/test';

/**
 * E2E Tests for Rotation Distance Calculator
 *
 * Tests the complete user flow:
 * 1. Navigate to calculators page
 * 2. Fill in rotation distance form
 * 3. Submit calculation
 * 4. Verify results display correctly
 */

test.describe('Rotation Distance Calculator', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to calculators page
    await page.goto('/calculators');

    // Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');
  });

  test('should display rotation distance calculator', async ({ page }) => {
    // Verify calculator heading exists
    await expect(page.getByRole('heading', { name: /rotation distance/i })).toBeVisible();

    // Verify input fields exist
    await expect(page.locator('[data-testid="current-rotation-distance"]')).toBeVisible();
    await expect(page.locator('[data-testid="requested-extrusion"]')).toBeVisible();
    await expect(page.locator('[data-testid="actual-extrusion"]')).toBeVisible();
  });

  test('should calculate new rotation distance correctly', async ({ page }) => {
    // Fill in form with test values
    // Formula: new = (current × actual) / requested
    // Test: (22.67 × 95) / 100 = 21.5365
    await page.locator('[data-testid="current-rotation-distance"]').fill('22.67');
    await page.locator('[data-testid="requested-extrusion"]').fill('100');
    await page.locator('[data-testid="actual-extrusion"]').fill('95');

    // Submit form
    await page.locator('[data-testid="calculate-button"]').click();

    // Wait for results to appear
    await page.waitForSelector('[data-testid="rotation-distance-result"]', {
      state: 'visible',
      timeout: 5000
    });

    // Verify result contains the calculated value (allowing for 3 decimal precision)
    const result = await page.getByTestId('rotation-distance-result').textContent();
    expect(result).toMatch(/21\.53[0-9]/); // Match 21.53X (handles rounding variations)
  });

  test('should show validation error for empty fields', async ({ page }) => {
    // Try to submit without filling fields
    await page.locator('[data-testid="calculate-button"]').click();

    // Expect validation message or disabled state
    // This will depend on your actual validation implementation
    const currentInput = page.locator('[data-testid="current-rotation-distance"]');
    await expect(currentInput).toHaveAttribute('required');
  });

  test('should handle decimal inputs correctly', async ({ page }) => {
    // Test with realistic decimal precision (3 decimals - typical for Klipper)
    // Use a meaningful calibration scenario: 3% under-extrusion
    await page.locator('[data-testid="current-rotation-distance"]').fill('22.679');
    await page.locator('[data-testid="requested-extrusion"]').fill('100');
    await page.locator('[data-testid="actual-extrusion"]').fill('97');

    await page.locator('[data-testid="calculate-button"]').click();

    // Should complete without errors and display result
    await expect(page.getByTestId('rotation-distance-result')).toBeVisible({ timeout: 5000 });

    // Verify the result contains a calculated value
    const result = await page.getByTestId('rotation-distance-result').textContent();
    expect(result).toMatch(/21\.99[0-9]/); // Should show ~21.99X (22.679 * 0.97)
  });

  test('should reset form after calculation', async ({ page }) => {
    // Fill and calculate
    await page.locator('[data-testid="current-rotation-distance"]').fill('22.67');
    await page.locator('[data-testid="requested-extrusion"]').fill('100');
    await page.locator('[data-testid="actual-extrusion"]').fill('95');
    await page.locator('[data-testid="calculate-button"]').click();

    // Wait for result
    await expect(page.getByTestId('rotation-distance-result')).toBeVisible({ timeout: 5000 });

    // Find reset button specifically within rotation distance calculator section
    const calculatorSection = page.locator('[data-testid="rotation-distance-result"]').locator('..');
    const resetButton = calculatorSection.getByRole('button', { name: /reset/i });

    // Click reset and verify fields are cleared
    await resetButton.click();
    await expect(page.locator('[data-testid="current-rotation-distance"]')).toHaveValue('');
  });

  test('should display Klipper config format', async ({ page }) => {
    // Calculate
    await page.locator('[data-testid="current-rotation-distance"]').fill('22.67');
    await page.locator('[data-testid="requested-extrusion"]').fill('100');
    await page.locator('[data-testid="actual-extrusion"]').fill('95');
    await page.locator('[data-testid="calculate-button"]').click();

    // Wait for result
    await expect(page.getByTestId('rotation-distance-result')).toBeVisible({ timeout: 5000 });

    // Check if config snippet is shown
    const configSnippet = page.locator('code, pre').filter({ hasText: /rotation_distance/i });
    await expect(configSnippet).toBeVisible();
  });
});
