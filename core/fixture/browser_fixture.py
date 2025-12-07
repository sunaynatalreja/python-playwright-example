import pytest
from core.driver_factory.driver_manager import DriverManager
from core.config_loader import load_settings
import random

@pytest.fixture(scope="function")
def page(request):
    cli_browser = request.config.getoption("--browser", default=None)
    browser_name=""
    if cli_browser:
        browser_name = cli_browser
    else:
        settings = load_settings()
        browser_list = settings["browsers"].get("supported")
        if not browser_list:
            raise RuntimeError(
                "Browser not specified. Use --browser=<name> or set 'browser' in settings.yaml."
            )
        browser_name = random.choice(browser_list)

    browser_obj = DriverManager.get_browser(browser_name)
    browser = browser_obj.get_browser()

    context = browser.new_context(viewport=None)
    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()
    browser_obj.stop()
