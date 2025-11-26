Automation Exercise UI Test Suite (Playwright + Behave + Python)

This repository contains an automated UI test suite for the AutomationExercise.com website, implemented using:
   - Playwright (Python)
   - Behave (BDD)
   - Page Object Model (POM)
   - GitHub Actions CI
The project demonstrates modern QA automation engineering practices, including clean POM architecture, reusable step definitions, synchronization handling, and cross-browser/headless execution in CI.


Project Goals

The purpose of this test suite is to:
   - Showcase strong automation engineering skills
   - Provide a clean, scalable BDD + Playwright test framework
   - Demonstrate ability to build UI automation from scratch
   - Validate key user flows on AutomationExercise.com
   - Run tests automatically in GitHub Actions CI
This repository is structured as a real production-ready UI automation framework.

Test Scenarios

1. Home Page Title Verification
Ensures the home page loads correctly and the title matches expected content.

2. User Registration Flow
Validates that a new user can:
   - Navigate to the signup form
   - Provide name and email
   - Complete the full registration form
   - Successfully create an account

3. Registered User Login   
   - Ensures an existing user can:
   - Open the login page
   - Enter valid credentials
   - Log in and see the correct username displayed

All tests are written in Gherkin for readability and business-level clarity.


👩‍💻 Author

Evgeniia Novikova — Software QA Automation Engineer
Specialized in Playwright, Selenium, API automation, CI/CD integration, and scalable test architecture.

