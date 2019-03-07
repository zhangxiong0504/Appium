import sys
import os
curpath=os.path.abspath(os.path.dirname(__file__))
rootpath=os.path.split(curpath)[0]
sys.path.append(rootpath)
import unittest
import HTMLTestRunner
from testsuites.register_test import ApkSearch1
from testsuites.login_test import ApkSearch2
from testsuites.alter_test import ApkSearch3
from testsuites.add_text_test import ApkSearch4
from testsuites.search_test import ApkSearch5
from testsuites.sort_test import ApkSearch6
from testsuites.archive_test import ApkSearch7
from testsuites.delete_test import ApkSearch8


report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(ApkSearch1))
suite.addTest(unittest.makeSuite(ApkSearch2))
suite.addTest(unittest.makeSuite(ApkSearch3))
suite.addTest(unittest.makeSuite(ApkSearch4))
suite.addTest(unittest.makeSuite(ApkSearch5))
suite.addTest(unittest.makeSuite(ApkSearch6))
suite.addTest(unittest.makeSuite(ApkSearch7))
suite.addTest(unittest.makeSuite(ApkSearch8))
# cur_path=os.path.dirname(os.path.realpath(__file__))
# report_path=os.path.join(cur_path,"test_report")
# if not os.path.exists(report_path):os.mkdir(report_path)
# test_dir="./"
# suit=unittest.TestLoader().discover(test_dir,pattern="*test.py")

if __name__=="__main__":
    html_report = report_path + r"\result.html"  # r定义存放报告的路径
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)