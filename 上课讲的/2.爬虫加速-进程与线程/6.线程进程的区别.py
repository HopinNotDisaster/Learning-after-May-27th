﻿# 进程是系统分配资源的基本单位
# 线程是CPU调度和代码执行的基本单位

# 一个应用程序由一个或多个进程组成
# 一个进程又可以包含一个或多个线程

# 线程可以共享全局变量，进程不能

# 进程线程使用的队列也不一样  线程使用python内置  进程使用多进程模块封装后的队列

# 进程的创建和切换开销会比线程高

# 多线程适合IO操作比较多的场景
# （IO reqeusts=网络IO  open=文件IO mysql,mongodb=DB IO）
# 多进程适合计算操作比较多的场景
# （AI模型训练  大数据计算）