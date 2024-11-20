from behave import given, when, then
from selenium import webdriver
from pages.shop_page import ShopPage
from pages.cart_page import CartPage


@given("I open the shop page")
def step_open_shop_page(context):
    """Open the shop page."""
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.shop_page = ShopPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.shop_page.navigate_to("https://autoprojekt.simplytest.de/")


@then('I verify the shop title is "{expected_title}"')
def step_verify_shop_title(context, expected_title):
    """Verify the shop page title."""
    context.shop_page.verify_shop_title(expected_title)


@then("I verify the cart is empty")
def step_verify_cart_is_empty(context):
    """Verify the cart is initially empty."""
    context.shop_page.verify_cart_is_empty()


@when('I add "{item}" to the cart')
def step_add_item_to_cart(context, item):
    """Add an item to the cart."""
    context.shop_page.add_album_to_cart()


@when("I navigate to the cart page")
def step_navigate_to_cart(context):
    """Navigate to the cart page."""
    context.shop_page.click_view_cart()


@when('I set the item quantity to "{quantity}" and update the cart')
def step_set_item_quantity_and_update(context, quantity):
    """Set item quantity and update the cart."""
    context.cart_page.set_item_quantity_and_update(quantity)


@then('I verify the total price is "{expected_price}"')
def step_verify_total_price(context, expected_price):
    """Verify the total price in the cart."""
    context.cart_page.verify_total_price(expected_price)


def after_scenario(context, scenario):
    """Close the browser after each scenario."""
    context.driver.quit()