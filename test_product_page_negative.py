import pytest
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)

    page.open()

    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message behavior is incorrect")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)

    page.open()

    page.add_product_to_cart()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message behavior is incorrect")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)

    page.open()

    page.add_product_to_cart()
    page.solve_quiz_and_get_code()

    page.should_disappear_success_message()
