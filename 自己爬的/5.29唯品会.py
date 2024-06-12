"""
出现的异常情况：
    1.进入新页面访问不出数据，进行刷新操作！
    2.访问十页左右会弹出登录iframe，点击×即可。
"""

import time
from selenium import webdriver

# start_time = time.time()


# 查询元素优化
# def find_elements(driver, xpath):
#     for i in range(60):
#         try:
#             time.sleep(0.5)
#             result = driver.find_elements_by_xpath(xpath)
#             if len(result) > 110:
#                 return result
#         except:
#             print("节点还没有加载完成...")
#     return None


# 环境配置
driver = webdriver.Chrome()
driver.get("https://category.vip.com/suggest.php?keyword=%E9%A6%99%E6%B0%B4&ff=235|12|1|1")
driver.maximize_window()
#
while True:

    try:
        # 进入新的页面有可能会显示登录弹窗 （iframe）
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='login_iframe']"))
        driver.find_element_by_xpath("//a[@class='ui-dialog-close  vipFont  J-login-frame-close']").click()
        driver.switch_to.default_content()
    except Exception as e:
        print(type(e), e)

    for i in range(2):
        # 模拟网页滑动
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    # 爬虫香水数据
    # item_list = find_elements(driver, "//section[@id='J_searchCatList']/div[contains(@class,'c-goods-item')]")
    # if item_list:
    #     print("商品数量：", len(item_list))
    #     for item in item_list:
    #         title = item.find_element_by_xpath(".//div[contains(@class,'c-goods-item__name')]").text
    #         price = item.find_element_by_xpath(".//div[@class='c-goods-item__sale-price J-goods-item__sale-price']").text
    #         print(title, price)
    try:
        driver.find_element_by_xpath("//a[@id='J_nextPage_link']").click()
        time.sleep(2)
    except Exception as e:
        print(type(e), e)
        print("点不了下一页了！")
        break
    # else:
    #     print(driver.current_url,"商品列表加载失败...")
    #     driver.refresh()
    #     time.sleep(2)

