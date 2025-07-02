from playwright.sync_api import Page

def test_example_local_site(page: Page):
    page.goto("http://localhost:8000/example.html")
    page.locator("button.btn-primary").click()
    page.locator("button.btn-success").click()