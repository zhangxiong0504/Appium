from framework.base_testcase import BaseTestCase
from app_objects.znbwl_alter import Alter
import unittest

class ApkSearch3(BaseTestCase):

    def test_apk_search(self):

        alter = Alter(self.driver)
        alter.alter("805135162@qq.com","zx980504","zxc")
if __name__=="__main__":
    unittest.main()
