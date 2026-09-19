from selenium import webdriver


class Browser:
    """Browser Init class"""
    def __init__(self):
        self.driver = webdriver.Firefox()
