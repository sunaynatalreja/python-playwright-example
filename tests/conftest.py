import pytest
from utils.step_context import StepContext
from utils.take_screenshot import take_screenshot
from core.fixture.browser_fixture import page,browser
from pages.home_page import HomePage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page", None)
        if page:
            take_screenshot(item.name,StepContext.get_step(),page)

@pytest.fixture
def home(page):
    home = HomePage(page)
    home.open_home()
    return home