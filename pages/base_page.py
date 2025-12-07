from core.config_loader import load_settings

class BasePage:

    def __init__(self, page):
        self.page = page
        self.settings = load_settings()
        self.base_url = self.settings["base_url"]
        "test"

    def open(self):
        self.page.goto(f"{self.base_url}")
