import { test, expect } from '@playwright/test'

test.describe('Input Shaping Calculator', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/calculators')
    await page.waitForLoadState('networkidle')
  })

  test('should display input shaping calculator', async ({ page }) => {
    await expect(page.getByRole('heading', { name: /input shaping calculator/i })).toBeVisible()
    await expect(page.locator('[data-testid="x-frequency"]')).toBeVisible()
    await expect(page.locator('[data-testid="y-frequency"]')).toBeVisible()
  })

  test('should calculate shaper recommendations', async ({ page }) => {
    await page.locator('[data-testid="x-frequency"]').fill('45.2')
    await page.locator('[data-testid="y-frequency"]').fill('37.8')
    await page.locator('[data-testid="calculate-input-shaping-button"]').click()
    await expect(page.getByTestId('input-shaping-result')).toBeVisible({ timeout: 5000 })
    const resultText = await page.getByTestId('input-shaping-result').textContent()
    expect(resultText).toMatch(/X Shaper/i)
    expect(resultText).toMatch(/Y Shaper/i)
    expect(resultText).toMatch(/Max Accel/i)
    expect(resultText).toMatch(/Klipper Configuration/i)
  })

  test('should reset fields', async ({ page }) => {
    await page.locator('[data-testid="x-frequency"]').fill('50')
    await page.locator('[data-testid="y-frequency"]').fill('55')
    await page.locator('[data-testid="calculate-input-shaping-button"]').click()
    await expect(page.getByTestId('input-shaping-result')).toBeVisible({ timeout: 5000 })
    await page.locator('[data-testid="reset-input-shaping-button"]').click()
    await expect(page.locator('[data-testid="x-frequency"]').inputValue()).resolves.toBe('')
    await expect(page.locator('[data-testid="y-frequency"]').inputValue()).resolves.toBe('')
    await expect(page.getByTestId('input-shaping-result')).not.toBeVisible()
  })
})
