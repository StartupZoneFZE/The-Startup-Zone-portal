import { test, expect } from '@playwright/test'

test.describe('Smoke', () => {
  test('dashboard renders', async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('h1:has-text("Dashboard")')).toBeVisible()
  })

  test('service requests page renders', async ({ page }) => {
    await page.goto('/service-requests')
    await expect(page.locator('h1:has-text("Service Requests")')).toBeVisible()
  })
})


