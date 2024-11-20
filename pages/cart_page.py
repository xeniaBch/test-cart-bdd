from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CartPage(BasePage):
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.input-text.qty.text")
    UPDATE_CART_BUTTON = (By.NAME, "update_cart")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".order-total > td")

    def set_item_quantity_and_update(self, quantity):
        input_field = self.wait_for_element(*self.QUANTITY_INPUT)
        input_field.click()
        input_field.clear()
        input_field.send_keys(quantity)

        update_button = self.wait_for_element(*self.UPDATE_CART_BUTTON)
        old_total_price = self.wait_for_element(*self.TOTAL_PRICE).text.strip()
        update_button.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.TOTAL_PRICE).text.strip() != old_total_price,
            message="The total price did not update."
        )

    def verify_total_price(self, expected_price):
        total_price = self.wait_for_element(*self.TOTAL_PRICE).text.strip()
        assert total_price == expected_price, f"Expected total price to be '{expected_price}', but got '{total_price}'"