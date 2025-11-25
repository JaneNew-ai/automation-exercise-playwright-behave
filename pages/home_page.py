from playwright.sync_api import expect
from .base_page import BasePage
from features.helpers.config import base_url


class HomePage(BasePage):
    def open(self) -> None:
        self.goto(base_url)

    def assert_title_contains(self, text: str) -> None:
        # Checks if the page title contains given text
        self.page.wait_for_load_state()
        title = self.page.title()
        assert text in title, f'Expected "{text}" to be in page title "{title}"'

    def go_to_login_page(self) -> None:
        # Click on Signup Login link in header
        self.page.get_by_role("link", name="Signup / Login").click()