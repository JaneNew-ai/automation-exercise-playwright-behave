from playwright.sync_api import expect
from .base_page import BasePage
from features.helpers.test_data import valid_signup_user_data


class SignupPage(BasePage):
    def complete_registration(self) -> None:
    # Title radio button if it has a label
        try:
            self.page.get_by_label("Mrs").check()
        except Exception:
            # If label text is different or there is no label you can skip this
            pass

        self.page.locator("[data-qa='password']").fill(valid_signup_user_data["password"])

        # DOB
        self.page.locator('div#uniform-days').click()
        self.page.select_option('#days', label='23')
        self.page.locator('div#uniform-months').click()
        self.page.select_option('#months', label='February')
        self.page.locator('div#uniform-years').click()
        self.page.select_option('#years', label='2000')

        self.page.get_by_label('Sign up for our newsletter!').click()
        self.page.get_by_label('Receive special offers from our partners!').click()

        # fill out address information
        self.page.locator("[data-qa='first_name']").fill(valid_signup_user_data['first_name'])
        self.page.locator("[data-qa='last_name']").fill(valid_signup_user_data["last_name"])
        self.page.locator("[data-qa='address']").fill(valid_signup_user_data['address'])
        self.page.locator("[data-qa='country']").click()
        self.page.select_option('#country', label='United States')

        self.page.locator("[data-qa='state']").fill(valid_signup_user_data["state"])
        self.page.locator("[data-qa='city']").fill(valid_signup_user_data['city'])

        self.page.locator("[data-qa='zipcode']").fill(valid_signup_user_data["zipcode"])
        self.page.locator("[data-qa='mobile_number']").fill(valid_signup_user_data["mobile_number"])
    
        self.page.get_by_role('button', name='Create Account').click()



    
        

