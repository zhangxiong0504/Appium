import os
from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
'''自动安装apk包到手机'''
apk_path=os.path.dirname(os.path.abspath('.'))

desired_cap={}
desired_cap['platformName']='Android'#设备系统
desired_cap['platformVersion']='4.4.2'#设备系统版本
desired_cap['deviceName']='127.0.0.1:62001'#设备名称
desired_cap['sessionOverride']=True#有没有创建链接，每次覆盖
#测试apk包的路径
desired_cap['app']=apk_path+'/app/todolist.apk'
#不需要每次都安装apk
desired_cap['noReset']=True
#应用程序的包名
desired_cap['appPackage']='com.example.todolist'
desired_cap['appActivity']='com.example.todolist.LoginActivity'
#如果设置是apk包的路径，则不需要配appPackage和appActivity，同理反之

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)#启动app


driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()
driver.find_element_by_id("com.example.todolist:id/action_new").click()
driver.find_element_by_id("com.example.todolist:id/toDoItemDetailET").send_keys("1111")
driver.find_element_by_id("com.example.todolist:id/saveBtn").click()
driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.find_element_by_id("android:id/title").click()
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()
action=TouchActions(driver)
delte=driver.find_element_by_id("com.example.todolist:id/toDoItemDetailTv")
action.long_press(delte).perform()
driver.find_element_by_id("android:id/title").click()
driver.find_element_by_id("android:id/button1").click()
driver.quit()

# driver.find_elements_by_android_uiautomator("new UiSelector().")
