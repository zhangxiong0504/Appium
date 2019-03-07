from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import unittest

class Add_text(BasePage):
    unit=unittest.TestCase()
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    add_text1=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    add_text_input=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    quick_add_text=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    menuAdd=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")
    title = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")
    def add1(self,text1):
        self.click(*self.login_button)
        self.click(*self.add_text1)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '添加备忘信息', msg=a)
        self.click(*self.add_text_input)
        self.sendkeys(text1,*self.add_text_input)
        self.click(*self.quick_add_text)
    def add2(self,text2):
        self.click(*self.menuAdd)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '添加备忘信息', msg=a)
        self.click(*self.add_text_input)
        self.sendkeys(text2, *self.add_text_input)
        self.click(*self.quick_add_text)
