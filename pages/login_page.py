from playwright.sync_api import Page

from base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page, "https://www.saucedemo.com/")

        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")


    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
