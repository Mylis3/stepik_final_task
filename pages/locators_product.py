from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    CART_BOOK_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    CART_PRICE = (By.CSS_SELECTOR, "div [class='alertinner '] p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
