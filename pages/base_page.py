from playwright.sync_api import Page

URL = 'https://www.saucedemo.com/'

class BasePage:

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url


    def open(self):
        self.page.goto(self.url)