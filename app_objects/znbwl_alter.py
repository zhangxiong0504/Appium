from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import unittest

class Alter(BasePage):
    unit=unittest.TestCase()
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    login_button2 = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    login_name=(By.ID,"com.pdswp.su.smartcalendar:id/title")
    name_text=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    alter_butter=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    login_pwd=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    login_button1=(By.ID,"com.pdswp.su.smartcalendar:id/login")
    title=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    login_logout = (By.ID, "com.pdswp.su.smartcalendar:id/exit")
    back=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")
    def alter(self,name,pwd,alter_name):
        self.click(*self.login_button)
        self.click(*self.login_button2)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '云平台登录', msg=a)
        self.sendkeys(name, *self.login_name)
        self.sendkeys(pwd, *self.login_pwd)
        self.click(*self.login_button1)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '智能备忘录', msg=a)

        self.click(*self.login_button)
        self.click(*self.login_button2)

        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '用户中心', msg=a)

        self.click(*self.login_name)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '修改用户名', msg=a)

        self.clear()
        self.sendkeys(alter_name,*self.name_text)
        self.click(*self.alter_butter)
        self.click(*self.back)
        a = self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a, '智能备忘录', msg=a)
        self.click(*self.login_button)
        self.click(*self.login_button2)
        self.click(*self.login_logout)
