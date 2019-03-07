from framework.base_testcase import BaseTestCase
from app_objects.znbwl_add_text import Add_text
import unittest

class ApkSearch4(BaseTestCase):

    def test_apk_search(self):
        add=Add_text(self.driver)
        add.add1("dsadsa")
        add.add2("sdfadasadas")

if __name__=="__main__":
    unittest.main()
