
import unittest
from playwright.sync_api import sync_playwright, expect


class TestWikipedia(unittest.TestCase):

    def setUp(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()

    def tearDown(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def test_basic_assertions(self):
        self.page.goto("https://www.wikipedia.org/")
        self.page.screenshot(path="wikipedia_homepage.png")

        # Assert title
        expect(self.page).to_have_title("Wikipedia")

        # Assert visible elements
        expect(self.page.locator(".central-textlogo")).to_be_visible()
        expect(self.page.locator('input[name="search"]')).to_be_visible()
        expect(self.page.locator('button[type="submit"]')).to_be_visible()
        
   # def test_wikipedia_search_button_fails(self):
    #    self.page.goto("https://www.wikipedia.org/")
    #    expect(self.page.locator('button[type="submit1"]')).to_be_visible()
        

if __name__ == "__main__":
    unittest.main()