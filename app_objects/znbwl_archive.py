from framework.base import BasePage
from appium.webdriver.common.mobileby import By
from appium import webdriver
import time
import unittest

class Archive(BasePage):
    unit=unittest.TestCase()
    note_title=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    menu_archive=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    archive_click=(By.NAME,"归档")
    # archive_click=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    recover=(By.ID,"com.pdswp.su.smartcalendar:id/menu")
    title = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")
    def archive(self):
        self.long_press(*self.note_title)
        self.click(*self.menu_archive)
        self.click(*self.login_button)
        # self.click(self.find_elements(*self.archive_click)[2])
        self.click(*self.archive_click)

        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '归档', msg=a)
        time.sleep(3)
        self.swipe_move(400,157,200,157,600)
        time.sleep(5)
        self.click(*self.recover)
