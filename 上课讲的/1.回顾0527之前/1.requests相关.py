import requests
import json

# 发送GET请求


url = 'https://www.httpbin.org/get'
params = {
    'key1': 'value1'
}
res = requests.get(url, params=params)

# 发送POST请求
# 看请求头来区分
# requests.post(url=url,data=) from表单的
# requests.post(url=url,json=) content/type json
# requests.post(url=url,files=) 文件相关
"""
# 常见请求的参数
    # headers 请求头
        # 1.User-Agent:浏览器信息
        # 2.Referer:请求的来源
        # 3.Cookie:请求的cookies
        # 4.Authorization:认证信息
        # 5.Content-Type:请求体类型       
    # proxies 代理
    # auth 认证
    # cookies 请求的cookies
    # timeout 超时
    # allow_redirects 是否允许重定向
    # params 查询参数
    # data 表单数据
    # json 请求体
    # version 协议版本
    # verify 是否验证SSL证书


:param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
"""

res = requests.get(url, params=params, headers={}, )

# 响应对象相关
"""
# response.status_code 状态码
    # 200 请求成功，仅仅是可以获取数据不一定是你想要的数据！
    # 301 永久重定向
    # 302 临时重定向
    # 304 资源未修改
    # 307 临时重定向
    # 400 请求错误
    # 401 未授权
    # 403 禁止访问
    # 404 请求资源不存在
    # 405 请求方法不支持
    # 408 请求超时
    # 409 请求资源冲突
    # 410 请求资源未找到
    # 411 请求实体过大
    # 429 请求过多
    # 500 服务器错误
    # 501 服务器不支持请求的功能
    
    
# response.ok 是否请求成功
# response.text 响应的文本内容
# response.content 响应的原始内容  ！建议使用content然后自己定义编码！
    # 以二进制的形式返回！
    # error参数可以设置为ignore来忽略应答中的错误编码。
    # response.content.decode('utf-8',errors="ignore") 转换为文本
# response.encoding 响应的编码
# response.apparent_encoding 响应的猜测编码
# response.json() 响应的json格式数据
    # response.json()
    # ==
    # json.loads(response.content.decode())  load    变简单！变好看，反序列化！
# response.cookies 响应的cookies
# response.headers 响应的头部信息！
# response.url 响应的url
response.history 重定向的响应历史

"""
res = requests.get("https://www.baidu.com", verify=False)
res.content.decode("gbk", errors="ignore")  # 'strict'默认编码都是严格模式！
