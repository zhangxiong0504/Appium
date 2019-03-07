from framework.base_testcase import BaseTestCase
from app_objects.znbwl_login import Login
import unittest
from ddt import data, ddt, unpack
from framework.until import Until
import os
import time

data_path = os.path.dirname(os.path.abspath('.')) + '/data/data.xlsx'
testdata = Until.read_excal(data_path, "Sheet1")

@ddt
class ApkSearch2(BaseTestCase):

    @data(*testdata)
    def test_apk_search(self,data):

        time.sleep(3)
        self.search_string = data["name"]
        self.search_string1 = data["pwd"]

        print("搜索内容->：%s", self.search_string)
        print("搜索内容->：%s", self.search_string1)

        login=Login(self.driver)
        time.sleep(3)
        login.login(self.search_string,self.search_string1)
if __name__=="__main__":
    unittest.main()
