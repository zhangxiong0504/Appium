from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import unittest

class Login(BasePage):
    unittest_testcase=unittest.TestCase()
    login_button=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")
    login_name=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    login_pwd=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    login_button1=(By.ID,"com.pdswp.su.smartcalendar:id/login")
    login_button2=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    title=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    login_logout = (By.ID, "com.pdswp.su.smartcalendar:id/exit")
    def login(self,name,pwd):
        self.click(*self.login_button)
        self.click(*self.login_button2)
        self.sendkeys(name,*self.login_name)
        self.sendkeys(pwd,*self.login_pwd)
        self.click(*self.login_button1)
        a=self.text(self.find_element(*self.title))
        print(a)
        self.unittest_testcase.assertEqual(a,'智能备忘录',msg=a)
        self.click(*self.login_button)
        self.click(*self.login_button2)
        self.click(*self.login_logout)


