from behave import *
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.user_home_page import UserHomePage
from pages.account_created_page import AccountCreatedPage
from features.helpers.test_data import valid_signup_user_data

# ---------------------------
# Scenario 1: Home title
# ---------------------------

@given('I open the home page')
def step_open_home_page(context):
    context.home_page = HomePage(context.page)
    context.home_page.open()

@then('the page title should contain "{text}"')
def step_title_contains(context, text):
    # text = "Automation Exercise"
    context.home_page.assert_title_contains(text)


# ---------------------------
# Scenario 2: Register new user
# ---------------------------

@when('I register a new user')
def step_register_user(context):
    context.home_page.go_to_login_page()
    
    context.login_page = LoginPage(context.page)
    context.login_page.signup_new_user()

    context.signup_page = SignupPage(context.page)
    context.signup_page.complete_registration()

@then('the account should be created and I should see "{text}"')
def step_account_created(context, text):
    account_page = AccountCreatedPage(context.page)
    account_page.assert_account_created(text)
    account_page.continue_to_home()


# ---------------------------
# Scenario 3: Registered user can login
# ---------------------------

@given('I have a registered user')
def step_have_registered_user(context):
    context.test_user = valid_signup_user_data

@when('I open the login page')
def  step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()

@when('I login with the registered user')
def step_login_with_registered_user(context):
    context.login_page.login()

@then('I should be logged in and see the username')
def step_logged_in_username(context):
    home = UserHomePage(context.page)
    home.assert_user_logged_in()


    

    
    





