from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME = (By.XPATH, '//input[@placeholder="Full Name"]')
    EMAIL = (By.XPATH, '//input[@placeholder="name@example.com"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@placeholder="Current Address"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')