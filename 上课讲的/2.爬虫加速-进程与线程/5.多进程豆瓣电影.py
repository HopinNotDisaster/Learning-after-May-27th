# import requests
# 计算豆瓣排行榜总数量 64676
# type_dict = {'剧情': 11,
#              '喜剧': 24,
#              '动作': 5,
#              '爱情': 13,
#              '科幻': 17,
#              '动画': 25,
#              '悬疑': 10,
#              '惊悚': 19,
#              '恐怖': 20,
#              '纪录片': 1,
#              '短片': 23,
#              '情色': 6,
#              '音乐': 14,
#              '歌舞': 7,
#              '家庭': 28,
#              '儿童': 8,
#              '传记': 2,
#              '历史': 4,
#              '战争': 22,
#              '犯罪': 3,
#              '西部': 27,
#              '奇幻': 16,
#              '冒险': 15,
#              '灾难': 12,
#              '武侠': 29,
#              '古装': 30,
#              '运动': 18,
#              '黑色电影': 31}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# }
# sum = 0
# url = "https://movie.douban.com/j/chart/top_list_count"
# for type_name, type_id in type_dict.items():
#     for interval_id in range(100, 0, -10):
#         params = {
#             "type": type_id,
#             "interval_id": f"{interval_id}:{interval_id - 10}",
#             "action": ""
#         }
#         response = requests.get(url, headers=headers, params=params)
#         total = response.json()["total"]
#         sum += total
#         print(type_name, f"{interval_id}:{interval_id - 10}", total, sum)

# from queue import Queue
import requests
# from threading import Thread
from pymongo import MongoClient
from multiprocessing import Process, Queue


def task(task_queue):
    mongo_conn = MongoClient()
    while not task_queue.empty():
        task = task_queue.get()
        params = {
            "type": task[1],
            "interval_id": task[2],
            "action": "",
            "start": 0,
            "limit": 20000
        }
        url = "https://movie.douban.com/j/chart/top_list"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }
        response = requests.get(url, headers=headers, params=params)
        mongo_conn.douban.ranklist.insert_many(response.json())


if __name__ == '__main__':
    # 构建任务队列
    task_queue = Queue()
    type_dict = {'剧情': 11,
                 '喜剧': 24,
                 '动作': 5,
                 '爱情': 13,
                 '科幻': 17,
                 '动画': 25,
                 '悬疑': 10,
                 # '惊悚': 19,
                 # '恐怖': 20,
                 # '纪录片': 1,
                 # '短片': 23,
                 # '情色': 6,
                 # '音乐': 14,
                 # '歌舞': 7,
                 # '家庭': 28,
                 # '儿童': 8,
                 # '传记': 2,
                 # '历史': 4,
                 # '战争': 22,
                 # '犯罪': 3,
                 # '西部': 27,
                 # '奇幻': 16,
                 # '冒险': 15,
                 # '灾难': 12,
                 # '武侠': 29,
                 # '古装': 30,
                 # '运动': 18,
                 '黑色电影': 31}
    for type_name, type_id in type_dict.items():
        for interval_id in range(100, 0, -10):
            task_queue.put((type_name, type_id, f"{interval_id}:{interval_id - 10}"))

    thread_list = []
    for i in range(32):
        t = Process(target=task, args=(task_queue,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
