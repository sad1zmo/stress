from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.css_selectors import *
import logging
import inspect


class MnemoschemeApplication:
    def __init__(self, driver):
        self.sel = driver

    def setup_150af(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_b}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{af150}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{shape_1_1_text_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_150pi(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_a}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pi150}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{shape_1_1_text_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_30Smarttrand(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_d}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{smart_trend30}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{smart30_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_150Smarttrand(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_c}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pi_smart}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{shape_1_1_text_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_zonemaker(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_a}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{zone_maker_attach}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{zone_and_button_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_button(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_button}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{zone_and_button_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_pmm_grid_control(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_b}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pmm_grid_control_result}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, ".pmmgridcontrol-body .pmmgc-row:nth-child(1) > g:nth-child(3) > text > tspan")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_pmm_vidjet(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_a}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level1}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level2}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level3}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level4}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{level5}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pmm_vidjet}").click()
            # Ожидаем элемент из мнемосхемы
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                                                        f"{pmm_vidjet_result}"), '0'))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_login(self, log, passwd):
        try:
            # Проверяем находимся ли мы на странице логина
            if self.sel.driver.find_elements(By.CSS_SELECTOR, '.login-block'):
                sleep(self.sel.random())
                # Вводим логин
                self.sel.driver.find_element(By.CSS_SELECTOR, "#txtUserName").send_keys(log)
                sleep(self.sel.random())
                # Вводим пароль
                self.sel.driver.find_element(By.CSS_SELECTOR, "#txtPassword").send_keys(passwd)
                sleep(self.sel.random())
                # Жмем на кнопку войти
                self.sel.driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
            else:
                return
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_logout(self):
        try:
            sleep(self.sel.random())
            # Ожидаем доступность кнопок после Экрана загрузки
            WebDriverWait(self.sel.driver, self.sel.big_wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                     ".big-loader")))
            # Нажимаем на кнопку "Список возможностей" в верхнем меню
            self.sel.driver.find_element(By.CSS_SELECTOR, ".profile").click()
            sleep(self.sel.random())
            # Жмем на кнопку завершить сеанс
            self.sel.driver.find_element(By.CSS_SELECTOR, "#logoutForm").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait + self.sel.big_wait} сек')
        finally:
            return

    def setup_indusoft_button(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_indusoft_button}").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait + self.sel.big_wait} сек')
        finally:
            return

