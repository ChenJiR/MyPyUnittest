from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
sleep(3)

# 鼠标悬停在“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
# 保存设置
driver.find_element_by_id("perfpanelgo").click()
sleep(2)
# 接受警告
driver.switch_to().accept()
# 上传文件
driver.find_element_by_name("file").send_keys('D://upload_file.txt')
# 上传程序
os.system("D://upfile.exe")
# 下载文件
driver.quit()

fp = webdriver.firefoxProfile()
# 0下载到默认路径/2保存到指定目录
fp.set_preference("browser.download.folderList", 0 / 2)
# 是否显示开始
fp.set_preference("browser.download.manage.showWhenString", False)
# 指定所下载的文件目录， os.getcwd()不传参，用于返回当前目录
fp.set_preference("browser.download.dir", os.getcwd())
# 指定要下载的Content-type值，"application/octet-stream"为文件类型
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.python.org")
driver.find_element_by_partial_link_text("selenium-2").click()

# 获得cookie信息
cookie = driver.get_cookie()
print(cookie)

# 通过js设置浏览器窗口的滚动条位置
js = "window.scrollTo(400, 450);"
driver.execute_script(js)

# 播放视频
video = driver.find_element_by_xpath("body/.../video")
# 返回播放文件地址
url = driver.execute_script("return argument[0].currentSrc;", video)
# 播放视频
driver.execute_script("return argument[0].play() ", video)
# 播放15秒
sleep(15)
# 暂停视频
driver.execute_script("return argument[0].pause()", video)

# 截取当前窗口
driver.get_screenshot_as_file("D:\\pyse\\baidu_img.jpg")

driver.close()
# 设置万能验证码
from random import randint

verify = randint(1000, 9999)
number = input(u"生成的随机数：%d" % verify)

number = int(number)

if number == verify:
    print("登录成功")
elif number == 123456:
    print("登录成功")
else:
    print("验证码输入有误")

