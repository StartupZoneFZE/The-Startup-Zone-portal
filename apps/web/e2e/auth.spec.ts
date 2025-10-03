import { test, expect } from '@playwright/test'

test.describe('Authentication', () => {
  test('should display login form', async ({ page }) => {
    await page.goto('/')
    
    // Check if the main layout is displayed (since we don't have auth yet, it should show)
    await expect(page.locator('h1:has-text("TSZ Portal")')).toBeVisible()
  })

  test('should have navigation sidebar', async ({ page }) => {
    await page.goto('/')
    
    // Check for sidebar navigation items
    await expect(page.locator('text=Dashboard')).toBeVisible()
    await expect(page.locator('text=Service Requests')).toBeVisible()
    await expect(page.locator('text=Clients')).toBeVisible()
    await expect(page.locator('text=Documents')).toBeVisible()
  })
})