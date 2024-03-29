from random import randrange
from selenium import webdriver


class SelDrv:

    def __init__(self):
        self.capabilities = {
            "browserName": "chrome",
            "browserVersion": "87.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "enableLog": False
            }
        }
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=self.capabilities)
        self.wait = 10
        self.big_wait = 120
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(self.wait)
        self.driver.get("http://portal-3.indusoft.ru:8093/")

    def random(self):
        return randrange(1, 2)
