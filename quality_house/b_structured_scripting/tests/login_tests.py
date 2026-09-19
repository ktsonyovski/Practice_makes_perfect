"""Simplest login liniear scripting test cases"""
import unittest
from quality_house.b_structured_scripting.page_actions.browser import Browser
from quality_house.b_structured_scripting.page_actions.base_page import BasePage


class LoginTests(unittest.TestCase):
    """Login test cases"""

    def setUp(self):
        self.browser = Browser()
        self.base_page = BasePage(browser=self.browser)
        self.browser.driver.get(BasePage.URL)

    def tearDown(self):
        self.browser.driver.quit()

    def test_login_student_1(self):
        self.base_page.login(username="student1", password="stpass1")
        self.base_page.logout()
        self.assertTrue(
            self.browser.driver.find_element(*self.base_page.login_button)
            .is_displayed(), "User is not logged out.")

    def test_login_student_2(self):
        self.base_page.login(username="student2", password="stpass2")
        self.base_page.logout()
        self.assertTrue(
            self.browser.driver.find_element(*self.base_page.login_button)
                .is_displayed(), "User is not logged out.")

    def test_login_student_3(self):
        self.base_page.login(username="student3", password="stpass3")
        self.base_page.logout()
        self.assertTrue(
            self.browser.driver.find_element(*self.base_page.login_button)
            .is_displayed(), "User is not logged out.")

    def test_login_all_students(self):
        student_accounts = [
            ("student1", "stpass1"),
            ("student2", "stpass2"),
            ("student3", "stpass3")
        ]

        for student, passwd in student_accounts:
            self.base_page.login(username=student, password=passwd)
            self.base_page.logout()
            self.assertTrue(
                self.browser.driver.find_element(*self.base_page.login_button)
                .is_displayed(), f"User {student} is not logged out.")

if __name__ == "__main__":
    unittest.main()
