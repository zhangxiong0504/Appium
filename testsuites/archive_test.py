from framework.base_testcase import BaseTestCase
from app_objects.znbwl_archive import Archive
import unittest

class ApkSearch7(BaseTestCase):

    def test_apk_search(self):

        archeive = Archive(self.driver)
        archeive.archive()
if __name__=="__main__":
    unittest.main()
