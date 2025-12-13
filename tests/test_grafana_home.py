import pytest

from pages.home_page import HomePage
import allure


class TestGrafanaHome:

    @allure.feature("Validate Grafana Homepage")
    @allure.description("""
    GIVEN the user wants to access the Grafana Play dashboard
    WHEN the homepage is opened
    THEN the dashboard should load successfully
    AND all links should be available for user interaction
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_grafana_home(self,home):
        home.verify_basic_links()

    @allure.feature("Validate PDF Export")
    @allure.description("""
    GIVEN the user opens the Export menu
    WHEN the user selects "Export as PDF"
    AND the user generates the PDF
    THEN a new browser tab should open
    AND the content type must be application/pdf
    """)
    @pytest.mark.regression
    def test_export_pdf(self,home):
        home.verify_pdf_export()

    @allure.feature("Validate Code Export")
    @allure.description("""
    GIVEN the user opens the Export menu
    WHEN the user selects "Export as Code"
    AND triggers the file download
    THEN a code file should be downloaded successfully
    """)
    @pytest.mark.regression
    def test_export_code(self,home):
        home.verify_code_export()

    @allure.feature("Validate Image Export")
    @allure.description("""
    GIVEN the user opens the Export menu
    WHEN the user selects "Export as Image"
    AND generates the image
    AND triggers the download
    THEN an image file should be downloaded successfully
    """)
    @pytest.mark.regression
    def test_export_image(self,home):
        home.verify_image_export()

    @allure.feature("Validate Share")
    @allure.description("""
    GIVEN the user clicks the Share button
    WHEN the Share action is performed
    THEN a confirmation/message should appear on the screen
    """)
    @pytest.mark.regression
    def test_share_link(self,home):
        home.verify_share()


    @allure.feature("Validate Login redirect")
    @allure.description("""
    GIVEN the user is on the homepage
    WHEN the user clicks the Sign In button
    THEN the user should be redirected to the /login page
    """)
    @pytest.mark.regression
    def test_login_redirect(self,home):
        home.verify_signin_redirect()

    @allure.feature("Validate links in updates panel")
    @allure.description("""
    GIVEN the user views the dashboard links panel
    WHEN the link container loads
    THEN at least one article or link entry should be present
    """)
    @pytest.mark.regression
    def test_links(self,home):
        home.verify_links_in_data_panel()


    @allure.feature("Validate Edit and Cancel")
    @allure.description("""
    GIVEN the user enters Edit mode
    WHEN the user cancels editing
    THEN the user should return to the regular dashboard view
    AND all basic links should remain visible
    """)
    @pytest.mark.regression
    def test_edit_cancel(self,home):
        home.verify_edit_and_cancel()


    @allure.feature("Validate Edit and Add")
    @allure.description("""
    GIVEN the user enters Edit mode
    WHEN the user adds a new row
    THEN the Add Row menu should appear
    AND the new row title should become visible
    AND the dashboard should save successfully
    """)
    @pytest.mark.regression
    def test_edit_add(self,home):
        home.verify_edit_and_add()


    @allure.feature("Validate search items")
    @allure.description("""
    GIVEN the user opens the Search panel
    WHEN the search list loads
    THEN at least one search result item should be visible
    """)
    @pytest.mark.regression
    def test_search(self,home):
        home.verify_search()

    @allure.feature("Validate page load time")
    @allure.description("""
    GIVEN the user navigates to the Grafana Play homepage
    WHEN the homepage loads completely
    THEN the total page load time should be under the defined SLA threshold
        """)
    @pytest.mark.regression
    def test_page_load_time(self, page):
        home = HomePage(page)
        load_time=home.open_home()
        home.verify_page_load_time(load_time)
