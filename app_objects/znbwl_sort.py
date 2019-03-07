from framework.base import BasePage
from appium.webdriver.common.mobileby import By
from appium import webdriver
import time

class Sort(BasePage):
    note_title=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    menu_sort=(By.ID,"com.pdswp.su.smartcalendar:id/menu_sort")
    sort_click=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")
    hold_el=(By.ID,"com.pdswp.su.smartcalendar:id/sortBtn")
    # note_time=(By.ID,"com.pdswp.su.smartcalendar:id/note_time")
    # space=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")
    def sort(self):
        self.long_press(*self.note_title)
        self.click(*self.menu_sort)
        # self.sort_move(683,353,683,200,1000)

        self.click_move(683,353,683,200,1000)
        # hold_el_list=self.find_elements(*self.hold_el)
        # print(hold_el_list)
        # self.huadong(hold_el_list[0],self.find_elements(*self.note_time)[1])
        # self.click(*self.space)
        time.sleep(3)
        self.click(*self.sort_click)
        # sort_click_list=self.find_elements(*self.sort_click)
        # self.click(sort_click_list[2])
