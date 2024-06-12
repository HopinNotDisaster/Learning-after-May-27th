# 使用Fiddler来抓取中国土地市场网的数据。
# 不使用右键检查了

# 异常情况！
# 加入隧道代理，全部解决
# 1.不管是页码多少 都会返回相同的数据！
#     1.1连接热点可以解决问题！
# 2.请求到差不多第七页就开始返回空了！
#     2.1降速！
# 3.返回的数据不是json格式。418访问被拦截

# 爬虫项目的维度
# 网站 中国土地市场网
# 取得的字段 土地供应相关
# 数据量 1300w~1400w
# 速度 80w/天 代理并发5次/秒
# 时间 2周*3=6周（爬取时间）
# 技术栈 python+requests+pymongo+Fiddler+代理ip
# 遇到的反爬
# 1.网站不允许f12       使用fidder抓包
# 2.页面访问过多，以及重复返回第一页的数据          使用代理ip
# 3.418，正常是json，疑似攻击的html          使用代理ip
# 4.状态码200，但接口状态码500
# 5.状态码200，但接口状态码301
# 6.网站会返回SSLError异常，需要使用代理
# 7.timeout



"""
数据的作用或者爬取网站的目的！
数据整理展示web    天眼查，企查查
数据统计分析可视化web 新抖 ，新站
AI 智能问答，AI绘图
咨询服务

"""












import time
from queue import Queue
from threading import Thread
import requests

from pymongo import MongoClient


class ResquestHelper:
    def __init__(self):
        self.max_retry_times = 10
        # 可能要手动规定每十秒换一次ip
        self.last_get_ip_time = time.time() - 10
        self.proxies = self.get_new_ip()

    def get_new_ip(self):
        print("更换了一次！！！！！！！！！！！！！！")
        # 隧道域名:端口号
        tunnel = "c852.kdltps.com:15818"
        # 用户名密码方式
        username = "t11741306088536"
        password = "n7ebkzyu"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
        }
        return proxies

    def post_with_proxy(self, url, json, headers, time_out=None):
        # print(f"现在使用的代理是{self.proxies}")
        """
        对于每一次的post请求，我们都进行十次重试
        在这十次重试中，每三次重试换一次ip
        :param url:
        :param json:
        :param headers:
        :param time_out:
        :return:
        """
        retry_times = 0
        while retry_times < self.max_retry_times:
            retry_times += 1
            # time.sleep(1)
            try:
                response = requests.post(url, json=json, headers=headers, proxies=self.get_new_ip(), timeout=time_out)
                if response.status_code == 200:
                    result = response.content.decode()
                    if "频繁" in result:
                        raise Exception("请求频繁")
                elif response.status_code == 418:
                    raise Exception(f"请求失败，状态码：{response.status_code}")
                return response
            except Exception as e:
                print(e, type(e))
                if retry_times % 3 == 0:
                    self.proxies = self.get_new_ip()
        return None


def task():
    client = MongoClient()
    rh = ResquestHelper()
    while not task_queue.empty():
        page = task_queue.get()
        print(f"正在抓取第{page}页的数据", "*******************")
        url = 'https://api.landchina.com/tGdxm/result/list'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        data = {"pageNum": page, "pageSize": 10, "startDate": "", "endDate": ""}
        response = rh.post_with_proxy(url=url, headers=headers, json=data)
        try:
            result = response.json()
            # print(result)
            data_obj = result["data"]["list"]
            for data in data_obj:
                print(page, data)
                client.land_china.data.insert_one(data)
        except Exception as e:
            print(e, type(e))
            print(f"{data},请求了十次仍没成功！")


if __name__ == '__main__':

    task_queue = Queue()
    for page in range(1, 181):
        task_queue.put(page)

    thread_list = []
    for i in range(42):
        t = Thread(target=task)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
