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
    try:
        res = requests.get(url, )
        print(res.json())
    except Exception as e:
        print(e)
# 'origin': '123.160.225.220'
# 使用阿诚的小海豚之后变为'5.34.216.10'
