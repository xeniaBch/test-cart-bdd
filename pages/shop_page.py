from selenium.webdriver.common.by import By
from .base_page import BasePage


class ShopPage(BasePage):
    SHOP_TITLE = (By.CSS_SELECTOR, ".woocommerce-products-header__title")
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    VIEW_CART_BUTTON = (By.LINK_TEXT, "View cart")
    CART_COUNT = (By.CSS_SELECTOR, "span.count")

    def verify_shop_title(self, expected_title):
        element = self.wait_for_element(*self.SHOP_TITLE)
        assert element.text == expected_title, f"Expected '{expected_title}', but got '{element.text}'"

    def verify_cart_is_empty(self):
        cart_count_icon = self.wait_for_element(*self.CART_COUNT)
        assert cart_count_icon.text.startswith("0"), f"Expected cart count to start with '0', but got '{cart_count_icon.text}'"

    def add_album_to_cart(self):
        self.wait_for_element(*self.ADD_TO_CART_BUTTON).click()

    def click_view_cart(self):
        self.wait_for_element(*self.VIEW_CART_BUTTON).click()