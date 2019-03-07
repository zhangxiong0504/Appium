from framework.base_testcase import BaseTestCase
from app_objects.znbwl_delete import Delete
import unittest

class ApkSearch8(BaseTestCase):

    def test_apk_search(self):

        delete = Delete(self.driver)
        delete.delete()
if __name__=="__main__":
    unittest.main()
