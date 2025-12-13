from playwright.sync_api import sync_playwright
from core.driver_factory.base_browser import BrowserBase

class EdgeBrowser(BrowserBase):

    def __init__(self, headless=False, slow_mo=0):
        self.headless = headless
        self.slow_mo = slow_mo

    def get_browser(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(
            channel="msedge",
            headless=self.headless,
            slow_mo=self.slow_mo
        )
        self.browser_context = self.browser.new_context(viewport=None)
        self.page = self.browser_context.new_page()

        return self.browser, self.browser_context, self.page


    def stop(self):
        if self.page:
            self.page.close()
            self.page = None

        if self.browser_context:
            self.browser_context.close()
            self.browser_context = None

        if self.browser:
            self.browser.close()
            self.browser = None

        if self.pw:
            self.pw.stop()
            self.pw = None