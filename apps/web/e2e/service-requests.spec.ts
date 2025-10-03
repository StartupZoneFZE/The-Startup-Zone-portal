import { test, expect } from '@playwright/test'

test.describe('Service Requests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/service-requests')
  })

  test('should display service requests page', async ({ page }) => {
    // Check page title
    await expect(page.locator('h1:has-text("Service Requests")')).toBeVisible()
    
    // Check page description
    await expect(page.locator('text=Manage all client service requests')).toBeVisible()
  })

  test('should display service requests table', async ({ page }) => {
    // Check table headers
    await expect(page.locator('th:has-text("Title")')).toBeVisible()
    await expect(page.locator('th:has-text("Client")')).toBeVisible()
    await expect(page.locator('th:has-text("Category")')).toBeVisible()
    await expect(page.locator('th:has-text("Priority")')).toBeVisible()
    await expect(page.locator('th:has-text("Status")')).toBeVisible()
    
    // Check for at least one row of data (mock data)
    await expect(page.locator('text=New Trade License Application')).toBeVisible()
  })

  test('should open create service request modal', async ({ page }) => {
    // Click the New Request button
    await page.click('button:has-text("New Request")')
    
    // Check if modal is opened
    await expect(page.locator('h2:has-text("Create Service Request")')).toBeVisible()
    
    // Check form fields
    await expect(page.locator('label:has-text("Title")')).toBeVisible()
    await expect(page.locator('label:has-text("Description")')).toBeVisible()
    await expect(page.locator('label:has-text("Client")')).toBeVisible()
    await expect(page.locator('label:has-text("Category")')).toBeVisible()
    await expect(page.locator('label:has-text("Priority")')).toBeVisible()
    
    // Close modal
    await page.click('button:has-text("Cancel")')
    await expect(page.locator('h2:has-text("Create Service Request")')).not.toBeVisible()
  })

  test('should filter service requests', async ({ page }) => {
    // Type in search box
    await page.fill('input[placeholder="Search requests..."]', 'License')
    
    // Verify filter button exists
    await expect(page.locator('button:has-text("Filter")')).toBeVisible()
  })
})