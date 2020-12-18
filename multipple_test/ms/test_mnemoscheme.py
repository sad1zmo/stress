from ms.mnemoscheme_application import MnemoschemeApplication
from random import randrange


class TestMnemoscheme(MnemoschemeApplication):

    def __init__(self, driver):
        super().__init__(driver)

    def __str__(self):
        return 'TestMnemoscheme'

    def test_150af(self):
        self.setup_150af()
        self.setup_indusoft_button()

    def test_150pi(self):
        self.setup_150pi()
        self.setup_indusoft_button()

    def test_button(self):
        self.setup_button()
        self.setup_indusoft_button()

    def test_30Smarttrand(self):
        self.setup_30Smarttrand()
        self.setup_indusoft_button()

    def test_150Smarttrand(self):
        self.setup_150Smarttrand()
        self.setup_indusoft_button()

    def test_zonemaker(self):
        self.setup_zonemaker()
        self.setup_indusoft_button()

    def test_pmm_grid_control(self):
        self.setup_pmm_grid_control()
        self.setup_indusoft_button()

    def test_pmm_vidjet(self):
        self.setup_pmm_vidjet()
        self.setup_indusoft_button()

    def login(self):
        self.setup_login(log='sam', passwd='sam')

    def start_methods_tm(self):
        methods_def = []

        for method in dir(self):
            if 'test' in method:
                methods_def.append(method)
        random_index = randrange(len(methods_def))
        method_name = methods_def[random_index]
        getattr(self, method_name)()


