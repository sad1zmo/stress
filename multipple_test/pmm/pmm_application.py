import datetime as dt
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import logging
import inspect
# Получить Имя класса который вызывает
#print(f'{self.__class__.__name__} 1')
# Получить имя метода который вызывает
#print(inspect.stack()[1].function)

class PmmApplication:
    def __init__(self, driver):
        self.sel = driver

    def setup_date_time(self):
        date_now = dt.datetime.now()
        six_month_ago = date_now - dt.timedelta(6 * 365 / 12)
        return six_month_ago.strftime("%d.%m.%Y %H:%M")

    def setup_open_pmm(self):
        try:
            sleep(self.sel.random())
            # Нажать кнопку PMM в верхнем меню
            self.sel.driver.find_element(By.CSS_SELECTOR, ".custom-swiper.main-menu-swiper li[data-path$=PMM]").click()
            # Проверяем нет ли экрана "Большой загрузки"
            if self.sel.driver.find_element(By.CSS_SELECTOR, ".big-loader").is_displayed():
                WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                        ".big-loader")))
            sleep(self.sel.random())
            # Проверяем открылось ли окно Выбора режимов
            if self.sel.driver.find_element(By.CSS_SELECTOR, "input[type=radio][value*='Диспетчерский журнал']").is_displayed():
                # В открывшейся менюшке нажать на кнопку диспетчерский журнал
                self.sel.driver.find_element(By.CSS_SELECTOR,
                                             "input[type=radio][value*='Диспетчерский журнал']").click()
                sleep(self.sel.random())
                # Нажать на кнопку выбрать
                self.sel.driver.find_element(By.CSS_SELECTOR,
                                             ".work-mode-form.ng-valid.ng-dirty.ng-valid-parse button").click()
            else:
                sleep(self.sel.random())
                # Ожидаем элемент из таблицы
                element = self.sel.driver.find_element(By.CSS_SELECTOR,
                                                        ".k-grid-content[style*=height] .k-master-row.ng-scope.additional-border:nth-child(1)")
                actions = ActionChains(self.sel.driver)
                actions.move_to_element(element)
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    ".big-loader")))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_event_card(self):
        sleep(self.sel.random())
        try:
            # Ожидаем элемент из таблицы
            element = self.sel.driver.find_element(By.CSS_SELECTOR,
                                               ".k-grid-content[style*=height] .k-master-row.ng-scope.additional-border:nth-child(1)")
            # Выполняем переход к элементу в таблице
            actions = ActionChains(self.sel.driver)
            actions.move_to_element(element).perform()
            sleep(self.sel.random())
            # Нажимаем кнопку "Показать детали" на элементе
            actions.double_click(element).perform()
            sleep(self.sel.random())
            # Находим и нажимаем кнопку закрыть
            close_button = self.sel.driver.find_element(By.CSS_SELECTOR, ".popup__body a[ng-click*='closeDetailPopup']")
            close_button.click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_change_date(self):
        try:
            sleep(self.sel.random())
            # Находим поле для ввода начальной даты и времени
            element = self.sel.driver.find_element(By.CSS_SELECTOR, "#startDatePicker")
            # Нажимаем в поле для ввода CTRL + A
            element.send_keys(Keys.CONTROL, 'a')
            sleep(self.sel.random())
            # Вводим дату и время
            element.send_keys(self.setup_date_time())
            sleep(self.sel.random())
            # Находим кнопку "Галочка"
            button = self.sel.driver.find_element(By.CSS_SELECTOR, ".time-button>button")
            # Нажимаем галочку применить
            actions = ActionChains(self.sel.driver)
            actions.click(button).double_click(button).perform()
            sleep(self.sel.random())
            # Ожидаем загрузку отфильтрованных элементов
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    "#circle-loader")))
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
            sleep(self.sel.random())
            # Находим стрелку правее фильтра НПП
            self.sel.driver.find_element(By.CSS_SELECTOR, "#atp-treelist ul:nth-child(1) > li:nth-child(1)>div>span[role=presentation]").click()
            sleep(self.sel.random())
            # Находим кнопку поиска(Лупу)
            button = self.sel.driver.find_element(By.CSS_SELECTOR, ".k-content.ng-scope button[icon*=search]")
            # Нажимаем на лупу
            actions = ActionChains(self.sel.driver)
            actions.click(button).double_click(button).perform()
            sleep(self.sel.random())
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    "#circle-loader")))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return



    def setup_kvit_events(self):
        try:
            sleep(self.sel.random())
            # Находим кнопку "Квитированные"
            button = self.sel.driver.find_element(By.CSS_SELECTOR,
                                                  ".swiper-wrapper > div:nth-child(3) > div")
            # Нажимаем кнопку "Квитированные"
            actions = ActionChains(self.sel.driver)
            actions.click(button).double_click(button).perform()
            # Ожидаем загрузку отфильтрованных элементов
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    "#circle-loader")))
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_ended_events(self):
        try:
            sleep(self.sel.random())
            # Находим кнопку "Завершенные"
            button = self.sel.driver.find_element(By.CSS_SELECTOR,
                                                  ".swiper-wrapper > div:nth-child(2) > div > span.summary-item-title.ng-binding")
            # Нажимаем кнопку "Завершенные"
            actions = ActionChains(self.sel.driver)
            actions.click(button).double_click(button).perform()
            # Ожидаем загрузку отфильтрованных элементов
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                    "#circle-loader")))
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
                WebDriverWait(self.sel.driver, self.sel.big_wait).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                                        ".big-loader")))
            self.sel.driver.find_element(By.CSS_SELECTOR, "h1.logo").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait + self.sel.big_wait} сек')
        finally:
            return

    # Закрываем предупреждение Хрома о том что данные не сохранятся
    def setup_alert_apply(self):
        sleep(self.sel.random())
        try:
            WebDriverWait(self.sel.driver, self.sel.wait).until(EC.alert_is_present())
            alert_obj = self.sel.driver.switch_to.alert
            alert_obj.accept()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

