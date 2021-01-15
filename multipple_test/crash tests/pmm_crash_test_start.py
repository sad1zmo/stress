import os
import logging
import datetime as dt
from pmm.crash_test.crash_test_pmm import CrashTestPmm
from driver.wd import SelDrv


class Start:

    def __init__(self):
        self.drv = SelDrv()
        self.pmm = CrashTestPmm(self.drv)
        self.time = dt.datetime.now().strftime("%d.%m.%Y")
        self.path = '../../logs/crash/pmm/'
        os.makedirs(self.path, exist_ok=True)
        logging.basicConfig(filename=f'../../logs/crash/pmm/{self.time}.log', format='%(asctime)s;%(message)s', datefmt='%d-%m-%Y %H:%M:%S')


st = Start()
st.pmm.login()
st.pmm.test_open_pmm()
st.pmm.test_event_card()
st.pmm.test_change_date()
st.pmm.test_filter_by_group()
st.pmm.test_kvit_events()
st.pmm.test_ended_events()
st.pmm.test_filtered_and_kvit()


