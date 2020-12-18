from pmm.pmm_application import PmmApplication
from random import randrange
from time import sleep

class TestPmm(PmmApplication):

    def __init__(self, driver):
        super().__init__(driver)

    def __str__(self):
        return 'TestPmm'

    def test_open_pmm(self):
        self.setup_open_pmm()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_event_card(self):
        self.setup_open_pmm()
        self.setup_event_card()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_change_date(self):
        self.setup_open_pmm()
        self.setup_change_date()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_filter_by_group(self):
        self.setup_open_pmm()
        self.setup_filter_by_group()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_kvit_events(self):
        self.setup_open_pmm()
        self.setup_kvit_events()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_ended_events(self):
        self.setup_open_pmm()
        self.setup_ended_events()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def test_filtered_and_kvit(self):
        self.setup_open_pmm()
        self.setup_filter_by_group()
        self.setup_kvit_events()
        self.setup_indusoft_button()
        self.setup_alert_apply()

    def login(self):
        self.setup_login(log='sam', passwd='sam')

    def start_methods_pmm(self):
        methods_def = []

        for method in dir(self):
            if 'test' in method:
                methods_def.append(method)
        random_index = randrange(len(methods_def))
        method_name = methods_def[random_index]
        getattr(self, method_name)()
