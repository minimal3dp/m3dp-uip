import { test, expect } from '@playwright/test';

/**
 * E2E Tests for OrcaSlicer Flow Calculators
 *
 * Tests both two-pass and YOLO flow calibration methods
 */

test.describe('OrcaSlicer Flow Calibration - Two Pass', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/calculators');
    await page.waitForLoadState('networkidle');
  });

  test('should calculate pass 1 flow ratio', async ({ page }) => {
    // Find OrcaSlicer Flow calculator section
    await expect(page.getByRole('heading', { name: /orcaslicer.*flow.*two.*pass/i })).toBeVisible();

    // Fill pass 1 inputs (using actual field names from component)
    // Current flow = 1.0, Pass 1 slide = -10 (meaning 90% flow)
    await page.locator('[data-testid="current-flow-pass1"]').fill('1.0');
    await page.locator('[data-testid="pass1-slide-value"]').fill('-10');

    await page.locator('[data-testid="calculate-flow-button"]').click();

    // Verify pass 1 result appears
    await expect(page.getByTestId('pass1-flow-result')).toBeVisible({ timeout: 5000 });
  });

  test('should calculate final flow with two passes', async ({ page }) => {
    // Pass 1
    await page.locator('[data-testid="current-flow-pass1"]').fill('1.0');
    await page.locator('[data-testid="pass1-slide-value"]').fill('-10');
    await page.locator('[data-testid="calculate-flow-button"]').click();

    // Wait for pass 1 result
    await expect(page.getByTestId('pass1-flow-result')).toBeVisible({ timeout: 5000 });

    // Fill pass 2 inputs (using pass 1 result)
    await page.locator('[data-testid="pass2-slide-value"]').fill('-2');
    await page.locator('[data-testid="calculate-flow-button"]').click();

    // Verify final result container still visible
    await expect(page.getByTestId('orcaslicer-flow-result')).toBeVisible({ timeout: 5000 });
  });
});

test.describe('OrcaSlicer Flow Calibration - YOLO', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/calculators');
    await page.waitForLoadState('networkidle');
  });

  test('should calculate direct flow adjustment', async ({ page }) => {
    // Find YOLO calculator section
    await expect(page.getByRole('heading', { name: /orcaslicer.*yolo/i })).toBeVisible();

    // Current flow = 1.0, YOLO slide = -0.035 (3.5% reduction)
    await page.locator('[data-testid="current-flow-yolo"]').fill('1.0');
    await page.locator('[data-testid="yolo-slide-value"]').fill('-0.035');

    await page.locator('[data-testid="calculate-yolo-button"]').click();

    // Verify result appears
    await expect(page.getByTestId('yolo-flow-result')).toBeVisible({ timeout: 5000 });
  });

  test('should handle negative slide value', async ({ page }) => {
    // Negative slide value means reduce flow
    await page.locator('[data-testid="current-flow-yolo"]').fill('1.0');
    await page.locator('[data-testid="yolo-slide-value"]').fill('-0.05');

    await page.locator('[data-testid="calculate-yolo-button"]').click();

    // Result should appear
    await expect(page.getByTestId('yolo-flow-result')).toBeVisible({ timeout: 5000 });
  });
});
