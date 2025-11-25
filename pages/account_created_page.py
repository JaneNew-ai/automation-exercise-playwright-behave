from playwright.sync_api import expect
from .base_page import BasePage


class AccountCreatedPage(BasePage):
    def assert_account_created(self, text: str) -> None:
        # Adjust the text according to the real page title
        expect(self.page.get_by_text(text, exact=False)).to_be_visible()

    def continue_to_home(self) -> None:
        self.page.get_by_role('link', name='Continue').click()