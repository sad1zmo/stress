import logging
import datetime as dt
from ms.crash_test.crash_test_mnemoscheme import CrashTestMnemoscheme
from driver.wd import SelDrv


class Start:

    def __init__(self):
        self.drv = SelDrv()
        self.tm = CrashTestMnemoscheme(self.drv)
        self.time = dt.datetime.now().strftime("%d.%m.%Y")
        logging.basicConfig(filename=f'./logs/crash/mn/{self.time}.log', format='%(asctime)s;%(message)s', datefmt='%d-%m-%Y %H:%M:%S')


st = Start()
st.tm.login()
st.tm.test_150af()
st.tm.test_150pi()
st.tm.test_button()
st.tm.test_30Smarttrand()
st.tm.test_150Smarttrand()
st.tm.test_zonemaker()
st.tm.test_pmm_grid_control()
st.tm.test_pmm_vidjet()







#st.pmm.test_setup_kvit_events()
#st.pmm.start_methods_pmm()

"""st.tm.login()
st.tm.start_methods_mn()
"""


