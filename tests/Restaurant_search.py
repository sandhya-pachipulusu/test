import unittest
from playwright.sync_api import sync_playwright


class TestGoogleMaps(unittest.TestCase):

    def setUp(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()

    def tearDown(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def test_google_maps_search_restaurants(self):
        self.page.goto("https://www.google.com/maps")

        self.page.get_by_role("combobox", name="Search Google Maps").fill("restaurants")
        self.page.get_by_role("button", name="Search").click()

        self.page.wait_for_selector('[role="article"]', timeout=20000)
        results = self.page.locator('[role="article"]')
        print("Results found:", results.count())
        
        self.assertGreater(results.count(), 0)


if __name__ == "__main__":
    unittest.main()