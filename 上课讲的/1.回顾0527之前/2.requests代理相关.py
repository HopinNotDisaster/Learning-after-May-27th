#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

# import requests
#
# # # 提取代理API接口，获取1个代理IP
# # api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=osa1bjgdode03wo5c4ow&signature=zo8rzic43p72t2gb1j2gs75nvlnv6a50&num=1&pt=1&sep=1"
# #
# # # 获取API接口返回的代理IP
# # proxy_ip = requests.get(api_url).text
# # print(proxy_ip)
# # # 用户名密码认证(私密代理/独享代理)
# # username = "d1071485873"
# # password = "22hup5ft"
# # proxies = {
# #     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
# #     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# # }
#
# url = "https://httpbin.org/get"
# test_res = requests.get(url=url,)
# print(test_res.json())


import requests

# 隧道域名:端口号
tunnel = "j265.kdltps.com:15818"

# 用户名密码方式
username = "t11679490034549"
password = "tw1tw5uq"
# 代理的值都是一样的，键有是否有s之分
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}
url = "https://httpbin.org/get"
test_res = requests.get(url=url, proxies=proxies)
print(test_res.json())
