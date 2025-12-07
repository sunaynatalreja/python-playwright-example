from playwright.sync_api import sync_playwright
from core.driver_factory.base_browser import BrowserBase

class ChromeBrowser(BrowserBase):

    def __init__(self, headless=False, slow_mo=0):
        self.headless = headless
        self.slow_mo = slow_mo

    def get_browser(self):
        self.pw = sync_playwright().start()

        self.browser = self.pw.chromium.launch(
            channel="chrome",
            headless=self.headless,
            slow_mo=self.slow_mo
        )

        return self.browser

    def stop(self):
        if self.pw:
            self.pw.stop()
            self.pw = None