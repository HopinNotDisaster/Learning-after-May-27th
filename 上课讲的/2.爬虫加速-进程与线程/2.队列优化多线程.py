import time
from queue import Queue
from threading import Thread
import requests

def task():
    while not task_queue.empty():
        page = task_queue.get()
        url = f"https://api.bilibili.com/pgc/season/index/result?st=1&order=3&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page={page}&season_type=1&pagesize=20&type=1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        for item in response.json()["data"]["list"]:
            print(page, item["title"], item["order"])

# 1 ：49.19
# 2 ：19.38
# 3 ：12.94
# 4 ： 9.69
# 8 ： 5.0
# 16 ： 2.7
# 32 ： 1.57
# 50 ：1.25
# 64 ：1.25
# 100： 1.21
# 128：1.22
if __name__ == '__main__':

    start_time = time.time()

    task_queue = Queue()
    for page in range(1, 186 + 1):
        task_queue.put(page)

    thread_list = []
    for i in range(2):
        t = Thread(target=task)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print("多线程多进程爬虫完成，总耗时：", time.time() - start_time)
