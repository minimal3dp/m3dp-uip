# Playwright E2E Testing

## Overview
End-to-end tests for M3DP-UIP calculator flows using Playwright. Tests verify:
- User input validation
- Calculation accuracy
- UI component rendering
- Error handling
- Klipper config output formatting

## Setup

### Install Dependencies
```bash
cd frontend
npm install
```

### Install Browsers
```bash
npx playwright install chromium
```

## Running Tests

### Run all tests (headless)
```bash
npm run test:e2e
```

### Interactive UI mode (recommended for development)
```bash
npm run test:e2e:ui
```

### Watch tests run in browser
```bash
npm run test:e2e:headed
```

### Debug mode (step through tests)
```bash
npm run test:e2e:debug
```

### Run specific test file
```bash
npx playwright test e2e/rotation-distance.spec.ts
```

## Test Structure

```
frontend/e2e/
├── rotation-distance.spec.ts    # Rotation distance calculator tests
└── orcaslicer-flow.spec.ts      # OrcaSlicer flow calibration tests
```

## Writing New Tests

### Test Naming Convention
```typescript
test.describe('Calculator Name', () => {
  test('should [action/outcome]', async ({ page }) => {
    // Test implementation
  });
});
```

### Use Data Test IDs
Components should include `data-testid` attributes for reliable selection:

```vue
<!-- Component template -->
<input data-testid="current-flow-pass1" v-model="currentFlow" />
<div data-testid="pass1-flow-result">{{ result }}</div>
```

```typescript
// Test file
await page.locator('[data-testid="current-flow-pass1"]').fill('0.98');
const result = await page.getByTestId('pass1-flow-result').textContent();
```

### Test Patterns

#### 1. Basic Calculation Test
```typescript
test('should calculate correctly', async ({ page }) => {
  await page.goto('/calculators');
  await page.getByLabel(/input field/i).fill('value');
  await page.getByRole('button', { name: /calculate/i }).click();
  await expect(page.getByTestId('result')).toContainText('expected');
});
```

#### 2. Validation Test
```typescript
test('should validate inputs', async ({ page }) => {
  await page.goto('/calculators');
  await page.getByRole('button', { name: /calculate/i }).click();
  await expect(page.getByLabel(/required field/i)).toHaveAttribute('required');
});
```

#### 3. Multi-Step Flow Test
```typescript
test('should handle multi-step process', async ({ page }) => {
  // Step 1
  await page.fill('[data-testid="step1-input"]', 'value1');
  await page.click('[data-testid="next-button"]');

  // Step 2
  await expect(page.getByTestId('step2-section')).toBeVisible();
  await page.fill('[data-testid="step2-input"]', 'value2');
  await page.click('[data-testid="calculate-button"]');

  // Verify final result
  await expect(page.getByTestId('final-result')).toBeVisible();
});
```

## CI/CD Integration

Tests automatically run in CI with:
- 2 retries on failure
- Single worker for consistency
- HTML report generation

### GitHub Actions Example
```yaml
- name: Run E2E Tests
  run: |
    cd frontend
    npm ci
    npx playwright install --with-deps chromium
    npm run test:e2e
```

## Debugging

### View Test Report
After running tests:
```bash
npx playwright show-report
```

### Trace Viewer
For failed tests, traces are automatically captured:
```bash
npx playwright show-trace trace.zip
```

### Screenshots
Screenshots are saved on failure to `test-results/` directory.

## Best Practices

1. **Use semantic selectors** - Prefer `getByRole`, `getByLabel`, `getByText` over CSS selectors
2. **Wait for stability** - Use `waitForLoadState('networkidle')` before interactions
3. **Verify visibility** - Check elements are visible before asserting content
4. **Test user flows** - Focus on complete user journeys, not isolated functions
5. **Keep tests independent** - Each test should work in isolation
6. **Use test IDs** - Add `data-testid` for dynamic/generated content
7. **Test error states** - Include validation and error handling tests
8. **Mobile testing** - Add mobile device tests for responsive layouts (future)

## Coverage

Current test coverage:
- ✅ Rotation Distance Calculator
- ✅ OrcaSlicer Flow (Two-Pass)
- ✅ OrcaSlicer Flow (YOLO)
- ⏳ Pressure Advance (TODO)
- ⏳ Vision Analysis Flow (TODO)

## Performance

Typical test run times:
- Single calculator: ~5-10 seconds
- Full suite: ~30-60 seconds
- With UI mode: Interactive (no timeout)

## Troubleshooting

### Tests timing out
Increase timeout in `playwright.config.ts`:
```typescript
timeout: 60 * 1000, // 60 seconds
```

### Dev server not starting
Check if port 3000 is available:
```bash
lsof -i :3000
```

### Browser not found
Reinstall browsers:
```bash
npx playwright install --force chromium
```

## Resources
- [Playwright Documentation](https://playwright.dev/)
- [Nuxt Testing Guide](https://nuxt.com/docs/getting-started/testing)
- [Best Practices](https://playwright.dev/docs/best-practices)
