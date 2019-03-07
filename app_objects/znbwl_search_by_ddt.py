from appium.webdriver.common.mobileby import By
from appium import webdriver
import unittest
from ddt import data, ddt, unpack
import time
from framework.until import Until
from framework.brower_engine import BrowserEngine
import os

data_path = os.path.dirname(os.path.abspath('.')) + '/data/data.xlsx'
testdata = Until.read_excal(data_path, "Sheet1")

@ddt
class Search_by_ddt(unittest.TestCase):
    browser=BrowserEngine()


    def setUp(self):
        self.browser.appium_desired()

    @data(*testdata)
    def test_search_by_ddt(self, data):
        search_string = data["name"]
        search_string1 = data["pwd"]

        print("搜索内容->：%s",search_string)
        print("搜索内容->：%s", search_string1)
        login_button = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
        search_input_name =(By.ID,"com.example.todolist:id/nameET")

        search_input_pwd=(By.ID,"com.example.todolist:id/passwordET")
        login_button2 = (By.ID,"com.pdswp.su.smartcalendar:id/email")
        # 找到后，键入 java 并提交搜索
        self.browserlogin_button.click()
        login_button2.click()
        search_input_name.send_keys(search_string)
        search_input_pwd.send_keys(search_string1)
        login_button1 = self.browser.driver.find_element_by_id( "com.example.todolist:id/loginBtn")
        time.sleep(3)
        login_button1.click()

    def tearDown(self):
        """测试结束后的操作，这里基本上都是关闭浏览器"""
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()