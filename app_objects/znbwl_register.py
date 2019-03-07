from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import unittest

class Register(BasePage):
    unit=unittest.TestCase()
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    login_button2 = (By.ID, "com.pdswp.su.smartcalendar:id/email")

    register_click=(By.ID,"com.pdswp.su.smartcalendar:id/register")
    register_name=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    register_email=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    register_pwd = (By.ID, "com.pdswp.su.smartcalendar:id/password")
    register_submit=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")
    title=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    login_logout = (By.ID, "com.pdswp.su.smartcalendar:id/exit")
    def register(self,name,email,pwd):
        self.click(*self.login_button)
        self.click(*self.login_button2)

        self.click(*self.register_click)
        self.sendkeys(name,*self.register_name)
        self.sendkeys(email, *self.register_email)
        self.sendkeys(pwd, *self.register_pwd)
        self.click(*self.register_submit)
        a=self.text(self.find_element(*self.title))
        print(a)
        self.unit.assertEqual(a,'智能备忘录',msg=a)
        self.click(*self.login_button)
        self.click(*self.login_button2)
        self.click(*self.login_logout)
