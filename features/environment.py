from playwright.sync_api import sync_playwright


def before_all(context):
    # Start Playwright and launch browser once for all scenarios
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, slow_mo=500
    )

def before_scenario(context, scenario):
    # Create a fresh page for each scenario
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Close page after scenario
    context.page.close()

def after_all(context):
    # Close browser and Playwright after all tests
    context.browser.close()
    context.playwright.stop()
