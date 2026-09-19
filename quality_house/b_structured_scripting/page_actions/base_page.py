from abc import ABC

from selenium.webdriver.common.by import By



class BasePage(ABC):
    """Base Quality House landing page"""

    URL = "http://acme.qualityhouse.com/build3/index.php"
    login_button = (By.CSS_SELECTOR, "a[href='index.php?page=login']")
    username_field = (By.ID, "username")
    passw_field = (By.NAME, "userpass")
    confirm_login_button = (By.NAME, "ses_login")
    logout_button = (By.CSS_SELECTOR, "a[href='index.php?page=logout']")
    confirm_logout_button = (By.CSS_SELECTOR, "a.big-btn[href='index.php?ses_logout=1']")

    def __init__(self, browser):
        self.browser = browser

    def login(self, username: str, password: str) -> None:
        """Login the webpage"""
        self.browser.driver.find_element(*self.login_button).click()
        self.browser.driver.find_element(*self.username_field).send_keys(username)
        self.browser.driver.find_element(*self.passw_field).send_keys(password)
        self.browser.driver.find_element(*self.confirm_login_button).click()

    def logout(self):
        """Logout user"""
        self.browser.driver.find_element(*self.logout_button).click()
        self.browser.driver.find_element(*self.confirm_logout_button).click()
