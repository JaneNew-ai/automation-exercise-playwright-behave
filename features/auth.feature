Feature: Home, Signup and Login flows

  Scenario: Home page title contains Automation Exercise
    Given I open the home page
    Then the page title should contain "Automation Exercise"

  Scenario: User can register a new account
    Given I open the home page
    When I register a new user
    Then the account should be created and I should see "ACCOUNT CREATED!"

  Scenario: Registered user can login
    Given I have a registered user
    When I open the login page
    And I login with the registered user
    Then I should be logged in and see the username

  