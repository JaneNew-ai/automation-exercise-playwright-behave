from .base_page import BasePage
from features.helpers.config import login_url
from features.helpers.test_data import valid_signup_user_data



class LoginPage(BasePage):
    def open(self) -> None:
        self.goto(login_url)

    def signup_new_user(self) -> None:
        # Work with the signup form on the right side
        signup_form = self.page.locator("form[action='/signup']")
        signup_form.get_by_placeholder("Name").fill(valid_signup_user_data['first_name'])
        signup_form.get_by_placeholder('Email Address').fill(valid_signup_user_data['email'])
        signup_form.get_by_role('button', name="Signup").click()

    def login(self) -> None:
        # Work with the login form on the left side
        login_form = self.page.locator("form[action='/login']")
        login_form.get_by_placeholder("Email Address").fill(valid_signup_user_data['email'])
        login_form.get_by_placeholder("Password").fill(valid_signup_user_data['password'])
        login_form.get_by_role("button", name="Login").click()


