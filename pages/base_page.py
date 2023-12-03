from selenium.webdriver.support.ui import WebDriverWait as wait
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, loctor, timeout = 5):
        return


