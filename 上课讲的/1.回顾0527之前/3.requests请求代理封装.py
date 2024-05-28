import requests

# 网络问题需要重试
# requests.exceptions.Timeout
# requests.exceptions.ReadTimeout
# requests.exceptions.ConnectTimeout
# requests.exceptions.ConnectionError

# 代理失效或者被封需要重试
# requests.exceptions.ProxyError

url = "http://www.httpbin.org/get"
for i in range(10):
    res = requests.get(url, )
    print(res.json())
