from framework.base_testcase import BaseTestCase
from app_objects.znbwl_sort import Sort
import unittest

class ApkSearch6(BaseTestCase):

    def test_apk_search(self):

        sort = Sort(self.driver)
        sort.sort()
if __name__=="__main__":
    unittest.main()
