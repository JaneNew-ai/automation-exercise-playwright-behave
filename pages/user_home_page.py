from playwright.sync_api import expect
from .base_page import BasePage
from features.helpers.test_data import valid_user_name


class UserHomePage(BasePage):

    def assert_user_logged_in(self) -> None:
        # Verify that "Logged in as <name>" is visible
        expect(self.page.get_by_text(
            f' Logged in as {valid_user_name}',
            exact=False)
        ).to_be_visible()