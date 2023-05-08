#海豚后台，第一步：登录；第二步：切换产品；第三步：找个产品，进入分链；第四步：新增母链
#一个元素执行完，最好休眠三秒，不然报错的
#题目：登录进海豚互娱广告后台
from selenium import webdriver
#导入时间器
import  time
from time import sleep
import selenium.webdriver

#启动谷歌的webdriver
driver=webdriver.Chrome("D:\python\chromedriver.exe")
#打开这个网站，是海豚互娱广告后台的网站
driver.get("http://192.168.8.118:8899/admin/login.html")

#最大化浏览器
driver.maximize_window()
#元素定位：定位到用户名文本框，在文本框里面输入内容
username=driver.find_element_by_name("username")
username.clear()
username.send_keys('zhuwei')
#元素定位：定位到密码文本框，在文本框里面输入内容
password=driver.find_element_by_name("password")
password.send_keys('a123456')
#元素定位：定位到【立即登入】按钮
btn=driver.find_element_by_xpath("//*[@id='main-layout']/div/div[3]/form/ul/li[3]/input")
btn.click()
#隐式等待3秒，3秒后执行下一个定位
time.sleep(3)

#元素定位：切换到【测试项目】
xm=driver.find_element_by_xpath("//*[@class='layui-tab-title']/li[2]")
xm.click()
time.sleep(3)

#元素定位：点击第一个产品的【进入分链】
fl=driver.find_element_by_xpath("//*[@class='layui-col-md4'][1]/*[@data-id='515']/div[1]/span/span[3]")
fl.click()
time.sleep(3)
#元素定位：点击【+新增母链】按钮，进入新增母链页
addm=driver.find_element_by_xpath("//*[@id='addLink']")
addm.click()

time.sleep(3)
#新增一个母链
#[产品名称]是默认的，[所属类型]也是选好的，[母链名称]，[小游戏appid]，[备注]
# name=driver.find_element_by_name('//*[@id="app_form"]/div[3]/div/div/input')
# name.send_keys('角斗江湖站')

name=driver.find_element_by_name("name")
name.send_keys('暗斗江湖')

appid=driver.find_element_by_name('third_app_id')
appid.send_keys('4399')

beizhu=driver.find_element_by_name('backup')
beizhu.send_keys('这是一条测试母链')

submit=driver.find_element_by_xpath("//*[@id='app_submit']")
submit.click()

