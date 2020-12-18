from tl.tl_application import TlApplication
from random import randrange


class TestTl(TlApplication):

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

    def start_methods_tl(self):
        methods_def = []

        for method in dir(self):
            if 'test' in method:
                methods_def.append(method)
        random_index = randrange(len(methods_def))
        method_name = methods_def[random_index]
        getattr(self, method_name)()

    def login(self):
        self.setup_login(log='sam', passwd='sam')
