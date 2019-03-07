from framework.base import BasePage
from appium.webdriver.common.mobileby import By
from appium import webdriver

class Search(BasePage):
    search_button=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    search_content=(By.ID,"android:id/search_src_text")
    def search(self,text):
        self.click(*self.search_button)
        self.click(*self.search_content)
        self.sendkeys(text,*self.search_content)
        self.driver.keyevent(66)