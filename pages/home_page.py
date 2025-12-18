from pages.base_page import BasePage
from playwright.sync_api import expect
import allure
from utils.take_screenshot import take_screenshot
import time

GRAFANA_PLAY_HEADER=".grafana-play-header'"
NAVIGATION_DETAIL="span[data-testid='data-testid Grafana Play Home breadcrumb']"
SIGN_IN="//a[contains(text(),'Sign in')]"
EDIT="//span[contains(text(),'Edit')]"
EXPORT="//span[contains(text(),'Export')]"
SHARE="//span[contains(text(),'Share')]"
SEARCH="//button[contains(text(),'Search')]"
SIDE_MENU=".css-c8tdw9"
GRAFANA_PLAY="//h2[contains(text(),'What is Grafana Play?')]/parent::div"
DASHBOARD_OF_THE_MONTH="//h2[contains(text(),'Dashboard of the Month')]/parent::div"
FEATURED_CONTRIBUTOR="//h2[contains(text(),'Featured Grafana Contributor')]/parent::div"
YOUTUBE_FRAME="iframe[src*='youtube.com']"
YOUTUBE_LINK=".ytp-cued-thumbnail-overlay-image"
PLAY_LAUNCHPAD="//h2[contains(text(),'Play Launchpad')]/parent::div"
LINKS_PANEL=".css-l8ieyt"
EXPORT_MENU="div[aria-label='Export dashboard menu']"
EXPORT_AS_PDF="//span[contains(text(),'Export as PDF')]"
EXPORT_AS_PDF_DASHBOARD="div[aria-label='Drawer title Export dashboard PDF']"
GENERATE_PDF_BUTTON="//span[contains(text(),'Generate PDF')]"
CLOSE_BUTTON_SECONDARY="//button[@aria-label='Close' and @variant='secondary']"
EXPORT_AS_CODE="//span[contains(text(),'Export as code')]"
EXPORT_AS_CODE_DASHBOARD="div[aria-label='Drawer title Export dashboard']"
DOWNLOAD_FILE_BUTTON="//span[contains(text(),'Download file')]"
EXPORT_AS_IMAGE="//span[contains(text(),'Export as image')]"
EXPORT_AS_IMAGE_DASHBOARD="div[aria-label='Drawer title Export as image']"
GENERATE_IMAGE="//span[contains(text(),'Generate image')]"
DOWNLOAD_IMAGE="//span[contains(text(),'Download image')]"
MESSAGE="div[aria-label='Shortened link copied to clipboard']"
EXIT_EDIT="//span[contains(text(),'Exit edit')]"
ADD="//span[contains(text(),'Add')]"
ADD_MENU=".css-12jjova"
ADD_ROW="//span[contains(text(),'Row')]"
ROW_TITLE="//span[contains(text(),'Row title')]"
SAVE="//span[contains(text(),'SAVE')]"
SEARCH_LIST="#kbar-listbox"

class HomePage(BasePage):
    def open_home(self):
        with allure.step("Open homepage"):
            start = time.time()
            self.open()
            self.page.wait_for_load_state("load")
            end = time.time()
            return end - start

    def verify_basic_links(self):
        with allure.step("Validate basic navigation links"):
            links = [
                GRAFANA_PLAY_HEADER,
                NAVIGATION_DETAIL,
                SIGN_IN,
                EDIT,
                EXPORT,
                SHARE,
                SEARCH,
                SIDE_MENU,
                GRAFANA_PLAY,
                DASHBOARD_OF_THE_MONTH,
                FEATURED_CONTRIBUTOR,
                YOUTUBE_FRAME,
                LINKS_PANEL,
                PLAY_LAUNCHPAD
            ]

            for link in links:
                with allure.step("Element tested "+link):
                    element=self.page.locator(link)
                    element.scroll_into_view_if_needed()
                    expect(element).to_be_attached()

    def verify_pdf_export(self):
        with allure.step("Verify export as PDF"):
            self.page.click(EXPORT)
            self.page.wait_for_selector(EXPORT_MENU)
            self.page.click(EXPORT_AS_PDF)
            self.page.wait_for_selector(EXPORT_AS_PDF_DASHBOARD)
            with self.page.context.expect_page() as new_page_info:
                self.page.click(GENERATE_PDF_BUTTON)
            pdf_page = new_page_info.value
            pdf_page.wait_for_load_state("load")

            content_type = pdf_page.evaluate("() => document.contentType")
            assert content_type == "application/pdf", f"Expected content_type is application/pdf,but got {content_type}"
            take_screenshot("Verify exports","Verify export as PDF",self.page)
            self.page.click(CLOSE_BUTTON_SECONDARY)

    def verify_code_export(self):
        with allure.step("Verify export as CODE"):
            self.page.click(EXPORT)
            self.page.wait_for_selector(EXPORT_MENU)
            self.page.click(EXPORT_AS_CODE)
            self.page.wait_for_selector(EXPORT_AS_CODE_DASHBOARD)
            with self.page.expect_download() as download_info:
                self.page.click(DOWNLOAD_FILE_BUTTON)
            download = download_info.value
            path = download.path() 
            assert path is not None, "Code file did not download"
            take_screenshot("Verify exports", "Verify export as Code", self.page)
            self.page.click(CLOSE_BUTTON_SECONDARY)

    def verify_image_export(self):
        with allure.step("Verify export as IMAGE"):
            self.page.click(EXPORT)
            self.page.wait_for_selector(EXPORT_MENU)
            self.page.click(EXPORT_AS_IMAGE)
            self.page.wait_for_selector(EXPORT_AS_IMAGE_DASHBOARD)
            self.page.click(GENERATE_IMAGE)
            self.page.wait_for_selector(DOWNLOAD_IMAGE)
            with self.page.expect_download() as download_info:
                self.page.click(DOWNLOAD_IMAGE)
            download = download_info.value
            path = download.path()
            assert path is not None, "Image file did not download"
            take_screenshot("Verify exports", "Verify export as Image", self.page)
            self.page.click(CLOSE_BUTTON_SECONDARY)

    def verify_share(self):
        with allure.step("Verify Share"):
            self.page.click(SHARE)
            expect(self.page.locator(MESSAGE)).to_be_visible()

    def verify_signin_redirect(self):
        with allure.step("Verify Signin Redirect"):
            self.page.click(SIGN_IN)
            self.page.wait_for_load_state("load")
            assert "/login" in self.page.url


    def verify_links_in_data_panel(self):
        with allure.step("Verify Links In Panel"):
            for _ in range(10):
                self.page.mouse.wheel(0, 1000)
                self.page.wait_for_timeout(200)
                if self.page.locator(LINKS_PANEL).count() > 0:
                    break
            parent = self.page.locator(LINKS_PANEL)
            parent.wait_for(state="attached")
            child = parent.locator("xpath=.//article")
            assert child.count() > 0, "No matching child elements found"

    def verify_edit_and_cancel(self):
        with allure.step("Verify Edit and Cancel"):
            self.page.click(EDIT)
            take_screenshot("Verify Edit and Cancel", "Verify Edit and Cancel", self.page)
            self.page.click(EXIT_EDIT)
            self.verify_basic_links()

    def verify_edit_and_add(self):
        with allure.step("Verify Edit and Add"):
            self.page.click(EDIT)
            self.page.click(ADD)
            self.page.wait_for_selector(ADD_MENU)
            take_screenshot("Verify Edit and Add", "Verify Edit and Add", self.page)
            self.page.click(ADD_ROW)
            take_screenshot("Verify Add Row", "Verify Add Row", self.page)
            expect(self.page.locator(ROW_TITLE)).to_be_visible()
            self.page.keyboard.press("Meta+S")
            take_screenshot("Verify Save Panel", "Verify Save Panel", self.page)
            self.page.keyboard.press("Enter")

    def verify_search(self):
        with allure.step("Verify Search"):
            self.page.click(SEARCH)
            parent = self.page.locator(SEARCH_LIST)
            parent.wait_for(state="attached")
            child = parent.locator("xpath=.//*")
            assert child.count() > 0, "No matching child elements found"

    def verify_page_load_time(self,load_time,max_seconds=5):
        with allure.step("Verify Search"):
            allure.attach(
                str(round(load_time, 2)),
                name="Page Load Time (seconds)",
                attachment_type=allure.attachment_type.TEXT
            )
            assert load_time < max_seconds, f"Page load too slow: {load_time:.2f} seconds"
