from framework.base import BasePage
from appium.webdriver.common.mobileby import By
from appium import webdriver
import time
import unittest

class Delete(BasePage):
    unit=unittest.TestCase()
    note_title = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")
    menu_delete=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    recycle_click = (By.NAME, "回收站")
    clean_recycle=(By.ID,"com.pdswp.su.smartcalendar:id/button")
    submit_delete=(By.NAME,"确定")
    title = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")
    def delete(self):
        self.long_press(*self.note_title)
        self.click(*self.menu_delete)
        self.click(*self.login_button)
        self.click(*self.recycle_click)
        a=self.text(self.find_element(*self.clean_recycle))
        print(a)
        self.unit.assertEqual(a,'清空回收站',msg=a)
        self.click(*self.clean_recycle)
        self.click(*self.submit_delete)
