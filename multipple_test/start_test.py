import os
from random import randrange
import logging
import datetime as dt
from ms.test_mnemoscheme import TestMnemoscheme
from tl.test_tl import TestTl
from pmm.test_pmm import TestPmm
from driver.wd import SelDrv


class Start:

    def __init__(self):
        self.drv = SelDrv()
        self.tm = TestMnemoscheme(self.drv)
        self.pmm = TestPmm(self.drv)
        self.tl = TestTl(self.drv)
        self.path = './logs/'
        os.makedirs(self.path, exist_ok=True)
        self.time = dt.datetime.now().strftime("%d.%m.%Y")
        logging.basicConfig(filename=f'./logs/{self.time}.log', format='%(asctime)s;%(message)s', datefmt='%d-%m-%Y %H:%M:%S')

    def run(self):
        dicts = {
            #0: ['start_methods_pmm', self.pmm],
            #1: ['start_methods_tm', self.tm],
            0: ['start_methods_tl', self.tl]
        }

        while True:
            random_method = randrange(len(dicts))
            getattr(dicts[random_method][1], dicts[random_method][0])()


st = Start()
st.pmm.login()
#st.tm.test_pmm_vidjet()
st.tl.test_change_date()

# st.run()





#st.pmm.test_setup_kvit_events()
#st.pmm.start_methods_pmm()

"""st.tm.login()
st.tm.start_methods_mn()
"""


