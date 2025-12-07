import os
import allure

def take_screenshot(test_name,step_name,page):
    os.makedirs("screenshots/after_tests", exist_ok=True)
    file_path = f"screenshots/after_tests/{test_name}_{step_name}.png"
    page.screenshot(path=file_path, full_page=True)

    allure.attach.file(
        file_path,
        name=f"{test_name}_{step_name}",
        attachment_type=allure.attachment_type.PNG
        )