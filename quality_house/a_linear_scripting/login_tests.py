"""Simplest login liniear scripting test cases"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

QH_URL = "http://acme.qualityhouse.com/build3/index.php"

class LoginTests(unittest.TestCase):
    """Login test cases"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(QH_URL)

    def tearDown(self):
        self.driver.quit()

    def login(self, username: str, password: str) -> None:
        """Login the webpage"""
        self.driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=login']").click()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.NAME, "userpass").send_keys(password)
        self.driver.find_element(By.NAME, "ses_login").click()

    def logout(self):
        """Logout user"""
        self.driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=logout']").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "a.big-btn[href='index.php?ses_logout=1']"
                                 ).click()

    def test_login_student_1(self):
        self.login(username="student1", password="stpass1")
        self.logout()

    def test_login_student_2(self):
        self.login(username="student2", password="stpass2")
        self.logout()
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR, "a[href='index.php?page=login']")
                .is_displayed(), "User is not logged out.")

    def test_login_student_3(self):
        self.login(username="student3", password="stpass3")
        self.logout()
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR, "a[href='index.php?page=login']")
                .is_displayed(), "User is not logged out.")

    def test_login_all_students(self):
        student_accounts = [
            ("student1", "stpass1"),
            ("student2", "stpass2"),
            ("student3", "stpass3")
        ]
        for student, passwd in student_accounts:
            self.login(username=student, password=passwd)
            self.logout()
            self.assertTrue(
                self.driver.find_element(
                    By.CSS_SELECTOR, "a[href='index.php?page=login']"
                ).is_displayed(),
                f"User {student} is not logged out."
            )

if __name__ == "__main__":
    unittest.main()
