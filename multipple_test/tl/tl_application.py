import datetime as dt
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import inspect

class TlApplication:
    def __init__(self, driver):
        self.sel = driver

    def setup_date_time(self):
        date_now = dt.datetime.now()
        six_month_ago = date_now - dt.timedelta(6 * 365 / 12)
        return six_month_ago.strftime("%d.%m.%Y %H:%M")

    def setup_tl_enter(self):
        try:
            sleep(self.sel.random())
            # Находим кнопку TL и нажимаем
            self.sel.driver.find_element(By.CSS_SELECTOR, ".custom-menu-submenu li[data-path$=TL]").click()
            # Проверяем появился ли чекбокс в верхней панели для дальнейших действий
            self.sel.driver.find_element(By.CSS_SELECTOR, "th.k-header>.checkbox-wrap.small")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_get_table(self):
        try:
            sleep(self.sel.random())
            # Ожидаем пока появится таблица в TL
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    ".k-virtual-scrollable-wrap table")))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_add_event(self):
        try:
            sleep(self.sel.random())
            # Нажимаем на кнопку Создать событие
            self.sel.driver.find_element(By.CSS_SELECTOR, "#addEventBtnId").click()
            sleep(self.sel.random())
            # Нажимаем на кнопку Простой оборудования
            self.sel.driver.find_element(By.CSS_SELECTOR, ".elem.ng-scope>a").click()
            sleep(self.sel.random())
            # Ожидаем экран загрузки
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                        ".big-loader")))
            # В открывшемся окне жмем ВЫБРАТЬ...
            self.sel.driver.find_element(By.CSS_SELECTOR, "#subdivivsion input[type=button]").click()
            sleep(self.sel.random())
            # Ставим галочку напротив НПП
            self.sel.driver.find_element(By.CSS_SELECTOR, ".k-top.k-top.ng-scope .k-in label>span").click()
            sleep(self.sel.random())
            # Нажимаем кнопку Выбрать
            self.sel.driver.find_element(By.CSS_SELECTOR, "span[ng-click='closeWindowSelect()']").click()
            sleep(self.sel.random())
            # Нажимаем кнопку Сохранить и закрыть
            self.sel.driver.find_element(By.CSS_SELECTOR, ".ui-button-text[ng-click*='saveAndCloseEvent()']").click()
            sleep(self.sel.random())
            # Ожидаем экран загрузки
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    ".big-loader")))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_open_event_card(self):
        try:
            sleep(self.sel.random())
            # Находим элемент в таблице
            element = self.sel.driver.find_element(By.CSS_SELECTOR, ".k-virtual-scrollable-wrap table> tbody > tr:nth-child(1) > td:nth-child(1)")
            # Нажимаем на элемент в таблице
            actions = ActionChains(self.sel.driver)
            actions.click(element).double_click(element).perform()
            # Ожидаем экран загрузки
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    ".big-loader")))
            sleep(self.sel.random())
            # Жмем на кнопку закрыть
            self.sel.driver.find_element(By.CSS_SELECTOR, ".ui-button-text[ng-click='closeWindow($event)']").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_change_date(self):
        try:
            actions = ActionChains(self.sel.driver)
            sleep(self.sel.random())
            # Нажимаем на кнопку Использование временного диапазона
            self.sel.driver.find_element(By.CSS_SELECTOR, "#isDateFilterAvaibleId").click()
            sleep(self.sel.random())
            element = self.sel.driver.find_element(By.CSS_SELECTOR, "#trend-settings-time-from")
            actions.click(element).send_keys(Keys.BACK_SPACE).send_keys('*-1Y')
            # Находим кнопку "Галочка"
            button = self.sel.driver.find_element(By.CSS_SELECTOR, "#applyDateTimeBtnId")
            # Нажимаем галочку применить
            actions.click(button).double_click(button).perform()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_filter_by_group(self):
        try:
            sleep(self.sel.random())
            # Нажимаем на НПП в меню слева
            self.sel.driver.find_element(By.CSS_SELECTOR,
                                             "#atp-treelist ul:nth-child(1) > li:nth-child(1)>div").click()
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
            if self.sel.driver.find_elements(By.CSS_SELECTOR, ".big-loader"):
                WebDriverWait(self.sel.driver, self.sel.big_wait).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                        ".big-loader")))
            self.sel.driver.find_element(By.CSS_SELECTOR, "h1.logo").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait + self.sel.big_wait} сек')
        finally:
            return
