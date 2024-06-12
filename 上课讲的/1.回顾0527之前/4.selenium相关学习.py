# from selenium import webdriver
#
# # 创建一个Chrome浏览器实例
# driver = webdriver.Chrome()
# # driver = webdriver.PhantomJS()
# driver.get('https://www.baidu.com')
# print(driver.page_source)

from selenium import webdriver
import time
import requests

# 1.添加代理
# api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oiuu4bftgx6l3irk6m98&signature=ef1gr5yikjr4kzclmyqe3tf0uq33kb24&num=1&pt=1&format=text&sep=2"
# proxy_ip = requests.get(api_url).text
# print("获取新代理：", proxy_ip)
# options = webdriver.ChromeOptions()  # 创建一个配置对象
# options.add_argument(f'--proxy-server=http://{proxy_ip}')  # 使用代理ip
# driver = webdriver.Chrome(chrome_options=options)  # 实例化带有配置的driver对象
# driver.get('http://www.httpbin.org/get')
# input()
# driver.quit()


# 2.携带插件的方式启动浏览器（条件：开启前需要关闭所有其他浏览器）
# 携带cookie启动 免登录
option = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/")
option.add_argument("--user-data-dir=C:/Users/QK/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=option)
driver.get("https://www.jd.com/")
while True:
    time.sleep(31)
    driver.refresh()

# 3.以开发者模式启动浏览器 绕过部分网站的检测
# options = webdriver.ChromeOptions()
# # # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# # # 就是这一行告诉chrome去掉了webdriver痕迹，令navigator.webdriver=false，极其关键
# options.add_argument("--disable-blink-features=AutomationControlled")
# # # 还有其他options配置，此处和问题无关，略去
# driver = webdriver.Chrome(options=options)
# # driver = webdriver.Chrome()
# driver.get("https://www.zhihu.com/question/503999321/answer/2827022034")
# time.sleep(10)
# try:
#     driver.find_element_by_xpath("//button[@aria-label='关闭']").click()
# except:
#     pass
# driver.find_element_by_xpath("//input[@id='Popover1-toggle']").send_keys("996")
# driver.find_element_by_xpath("//button[@aria-label='搜索']").click()

# 4.修改谷歌浏览器为无界面模式
# # 创建chrome参数对象
# opt = webdriver.ChromeOptions()
# # 把chrome设置成无头模式，不论windows还是linux都可以，自动适配对应参数
# opt.set_headless()
# # 不制定options选项则是普通有头浏览器
# driver = webdriver.Chrome(options=opt)
# driver.get("https://www.taobao.com/")
# # 后台运行 隐藏浏览器页面
# print(driver.page_source)


# 5.禁用图片优化浏览器执行速度
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("https://www.bilibili.com/")
# input()


# 6.等待优化
# driver = webdriver.Chrome()
#
# # 自己实现：
# # 等待优化
# def find_element(driver, xpath):
#     for i in range(30):
#         try:
#             time.sleep(0.5)
#             result = driver.find_elements_by_xpath(xpath)
#             return result
#         except:
#             print("节点还没有加载完成...")
#     return None

# # selenium自带的：  显式等待
# expected_conditions 类，负责条件触发
# from selenium.webdriver.support import expected_conditions as EC
# # WebDriverWait 库，负责循环等待
# from selenium.webdriver.support.ui import WebDriverWait
# # 查找方式的库
# from selenium.webdriver.common.by import By
#
# # 用户名的输入框
# keyword = WebDriverWait(driver,30).until(
#     EC.presence_of_element_located((By.XPATH, '//div[@class="subWp Ldn"]/div[1]//input'))
# )
