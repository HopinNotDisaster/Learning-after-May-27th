# 进程池
import time
from multiprocessing import Process


def func(name):
    print('hello', name)
    time.sleep(3)
    print('end')


if __name__ == '__main__':

    start_time = time.time()
    pl = []
    for i in range(5):
        pl.append(Process(target=func, args=('bob',)))

    for p in pl:
        p.start()

    for p1 in pl:
        p1.join()
    print(time.time() - start_time)
