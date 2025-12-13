import pytest
from core.driver_factory.driver_manager import DriverManager
from core.config_loader import load_settings
import random

@pytest.fixture(scope="function")
def page(request):
    cli_browser = request.config.getoption("--browser", default=None)
    browser_name=""
    settings = load_settings()
    if cli_browser:
        browser_name = cli_browser
    else:

        browser_list = settings["browsers"].get("supported")
        if not browser_list:
            raise RuntimeError(
                "Browser not specified. Use --browser=<name> or set 'browser' in settings.yaml."
            )
        browser_name = random.choice(browser_list)
    headless = settings["browsers"].get("headless")
    browser_obj = DriverManager.get_browser(browser_name,headless=headless)
    page = browser_obj.get_browser()

    yield page

    browser_obj.stop()
