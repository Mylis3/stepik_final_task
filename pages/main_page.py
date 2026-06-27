from .base_page import BasePage
from .locators import MainPageLocators
# from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # 1-й способ перехода между страницами: возвращать нужный Page Object.
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)

    #  далее в тесте:
    # def test_guest_can_go_to_login_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(browser, link)
    #     page.open()
    #     login_page = page.go_to_login_page()
    #     login_page.should_be_login_page()

    # 2-й способ перехода между страницами:
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    # закомментировать:
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)

    # далее Инициализируем LoginPage в теле теста и import LoginPage
    # def test_guest_can_go_to_login_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(browser, link)
    #     page.open()
    #     page.go_to_login_page()
    #     login_page = LoginPage(browser, browser.current_url)
    #     login_page.should_be_login_page()
