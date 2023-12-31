from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(loctor))

    def elements_are_visible(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(loctor))

    def element_is_present(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(loctor))

    def elements_are_present(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(loctor))

    def element_is_not_visible(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(loctor))

    def element_is_clickable(self, loctor, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(loctor))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
