from framework.base_testcase import BaseTestCase
from app_objects.znbwl_search import Search
import unittest

class ApkSearch5(BaseTestCase):

    def test_apk_search(self):

        search = Search(self.driver)
        search. search("111")
if __name__=="__main__":
    unittest.main()
