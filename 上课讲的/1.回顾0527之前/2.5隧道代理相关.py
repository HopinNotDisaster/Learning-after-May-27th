# 隧道代理的使用
import requests

# 隧道域名:端口号
tunnel = "f543.kdltps.com:15818"

# 用户名密码方式
username = "t11679376003566"
password = "suu5g3sg"
proxies = {
    "http": "http://t11679376003566:suu5g3sg@f543.kdltps.com:15818/",
    "https": f"http://{username}:{password}@{tunnel}/"
}

url = "https://www.httpbin.org/get"
response = requests.get(url,proxies=proxies)
print(response.content.decode())