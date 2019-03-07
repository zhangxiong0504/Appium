import os
from appium import webdriver
from framework.logger import Logger
import yaml
import os


logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    apk_path = os.path.dirname(os.path.abspath('.'))
    def appium_desired(self):
        with open(os.path.dirname(os.path.abspath('.'))+'/config/config.yaml','r',encoding='utf-8')as file:
            data=yaml.load(file)
        desired_caps = {}
        desired_caps['platformName']=data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = ['127.0.0.1:62001']
        desired_caps['sessionOverride'] =True
        desired_caps['app'] = self.apk_path + '/app/'+data['app']
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] =data['appActivity']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
        self.driver.implicitly_wait(5)
        return self.driver
    def quit(self):
        self.driver.quit()

# Browser=BrowserEngine()
# Browser.appium_desired()


# class BrowserEngine(object):
#     dir=os.path.dirname(os.path.abspath('.'))
#     todolist_driver_path=dir+'/app/todolist.apk'
#     znbwl_driver_path=dir+'/app/znbwl.apk'
#     apk_path = os.path.dirname(os.path.abspath('.'))
#     desired_cap={}
#
#     def open_browser(self):
#         config=ConfigParser()
#         file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.yaml'
#         config.read(file_path)
#
#         brower=config.get("browserType","browerName")
#         print(brower)
#         logger.info("You has select %s browser"%brower)
#         name=config.get("testServer","apkname")
#         print(name)
#         logger.info("The test server url is:%s"%name)
#
#         self.desired_cap['platformName'] =brower  # 设备系统
#         self.desired_cap['platformVersion'] = '4.4.2'  # 设备系统版本
#         self.desired_cap['deviceName'] = '127.0.0.1:62001'  # 设备名称
#
#         if name=="todolist":
#             self.desired_cap['sessionOverride'] = True  # 有没有创建链接，每次覆盖
#             # 测试apk包的路径
#             self.desired_cap['app'] = self.apk_path + '/app/todolist.apk'
#             logger.info("Starting todolist brower")
#             self.desired_cap['appPackage'] = 'com.example.todolist'
#             self.desired_cap['appActivity'] = 'com.example.todolist.LoginActivity'
#         elif name=="znbwl":
#             self.desired_cap['sessionOverride'] = True  # 有没有创建链接，每次覆盖
#             # 测试apk包的路径
#             self.desired_cap['app'] = self.apk_path + '/app/todolist.apk'
#             logger.info("Starting znbwl brower")
#             self.desired_cap['appPackage'] = 'com.pdswp.su.smartcalendar'
#             self.desired_cap['appActivity'] = 'com.pdsw.su.smartcalendar.WelcomeNote'
#
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desired_cap)  # 启动app
#         logger.info("Open appname:%s"%name)
#     def quit_browser(self):
#         logger.info("Now,Close and quit the browser")
#         self.driver.quit()
#

