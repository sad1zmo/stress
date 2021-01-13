from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.css_selectors import *
import logging
import inspect


class CrashMnemoschemeApplication:
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_b = {button_b};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\naf150 = {af150};\n'
                f'shape_1_1_text_result = {shape_1_1_text_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_a = {button_a};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\npi150 = {pi150};\n'
                f'shape_1_1_text_result = {shape_1_1_text_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_d = {button_d};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\nsmart_trend30 = {smart_trend30};\n'
                f'smart30_result = {smart30_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_c = {button_c};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\npi_smart = {pi_smart};\n'
                f'shape_1_1_text_result = {shape_1_1_text_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_a = {button_a};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\nzone_maker_attach = {zone_maker_attach};\n'
                f'zone_and_button_result = {zone_and_button_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_button = {button_button};\nzone_and_button_result= {zone_and_button_result}')
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
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pmm_grid_control}").click()
            # Ожидаем элемент из мнемосхемы
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{pmm_grid_control_result}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_b = {button_b};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\npmm_grid_control = {pmm_grid_control};\n'
                f'pmm_grid_control_result = {pmm_grid_control_result}\n')
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
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_a = {button_a};\nlevel1 = {level1};\nlevel2 = {level2};\nlevel3 = {level3};\n'
                f'level4 = {level4};\nlevel5 = {level5};\npmm_vidjet = {pmm_vidjet};\n'
                f'pmm_vidjet_result = {pmm_vidjet_result}\n')
        finally:
            return

    def setup_login(self, log, passwd):
        try:
            # Проверяем находимся ли мы на странице логина
            if self.sel.driver.find_elements(By.CSS_SELECTOR, f"{login_block}"):
                sleep(self.sel.random())
                # Вводим логин
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{user_name}").send_keys(log)
                sleep(self.sel.random())
                # Вводим пароль
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{user_password}").send_keys(passwd)
                sleep(self.sel.random())
                # Жмем на кнопку войти
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_login}").click()
            else:
                return
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'login_block = {login_block};\nuser_name = {user_name};\nuser_password = {user_password};\n'
                f'button_login = {button_login}\n')
        finally:
            return

    def setup_indusoft_button(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_indusoft_button}").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};\n'
                f'button_indusoft_button = {button_indusoft_button}\n')
        finally:
            return