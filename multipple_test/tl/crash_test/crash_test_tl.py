from tl.crash_test.tl_crash_test_application import CrashTlApplication
from random import randrange


class TestTl(CrashTlApplication):

    def __init__(self, driver):
        super().__init__(driver)

    def __str__(self):
        return 'TestTl'

    def test_tl_enter(self):
        self.setup_tl_enter()
        self.setup_indusoft_button()

    def test_get_table(self):
        self.setup_tl_enter()
        self.setup_get_table()
        self.setup_indusoft_button()

    def test_add_event(self):
        self.setup_tl_enter()
        self.setup_add_event()
        self.setup_indusoft_button()

    def test_open_event_card(self):
        self.setup_tl_enter()
        self.setup_get_table()
        self.setup_open_event_card()
        self.setup_indusoft_button()

    def test_change_date(self):
        self.setup_tl_enter()
        self.setup_change_date()
        self.setup_get_table()
        self.setup_indusoft_button()

    def test_filter_by_group(self):
        self.setup_tl_enter()
        self.setup_filter_by_group()
        self.setup_get_table()
        self.setup_indusoft_button()

    def login(self):
        self.setup_login(log='sam', passwd='sam')