from scrapy import cmdline

# cmdline.execute("scrapy crawl book".split())

# execute需要传入的是一个数组！所以需要使用split来进行切割！
cmdline.execute("scrapy crawl book --logfile zongheng.log".split())
"""
2024-06-11 15:54:00 [scrapy.utils.log] INFO: Scrapy 2.11.2 started (bot: zongheng) 显示我们使用的scrapy的版本信息
2024-06-11 15:54:00 [scrapy.utils.log] INFO: Versions: lxml 5.2.2.0, libxml2 2.11.7...... 相关内容的环境信息
2024-06-11 15:54:00 [scrapy.addons] INFO: Enabled addons:  显示出允许的域名！这里我给注掉了所有为空！
2024-06-11 15:54:00 [asyncio] DEBUG: Using selector: SelectSelector 异步相关！
2024-06-11 15:54:00 [scrapy.utils.log] DEBUG: Using reactor: twisted..... 异步相关！
2024-06-11 15:54:00 [scrapy.utils.log] DEBUG: Using asyncio event loo... 异步相关！
2024-06-11 15:54:00 [scrapy.extensions.telnet] INFO: Telnet Password: 52b0b67443805435  第三方扩展插件！
2024-06-11 15:54:00 [scrapy.middleware] INFO: Enabled extensions:  第三方扩展插件！
['scrapy.extensions.corestats.CoreStats',      第三方扩展插件！
 'scrapy.extensions.telnet.TelnetConsole',     第三方扩展插件！
 'scrapy.extensions.logstats.LogStats']          第三方扩展插件！
2024-06-11 15:54:00 [scrapy.crawler] INFO: Overridden settings:  设置相关！
{'BOT_NAME': 'zongheng', 
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'zongheng.spiders',  模块名
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',   什么请求指纹，与去重有关！
 'ROBOTSTXT_OBEY': True,  robots.txt就是那个协议了！
 'SPIDER_MODULES': ['zongheng.spiders'],  爬虫模块
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}  也是一个异步！
.
.
.
.
.
2024-06-11 15:54:00 [scrapy.middleware] INFO: Enabled item pipelines:    开启的管道！
2024-06-11 15:54:00 [scrapy.core.engine] INFO: Spider opened   才是咱的爬虫刚开始启动！
2024-06-11 15:54:00 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0...... 显示爬虫的速度！



2024-06-11 15:54:01 [scrapy.core.engine] INFO: Closing spider (finished)  爬虫结束！
{'downloader/request_bytes': 618,  共多少字节！
 'downloader/request_count': 2,  共多少个请求！
 'downloader/request_method_count/GET': 2,  共多少个GET请求！
 'downloader/response_bytes': 12200,  共多少个响应字节！
 'finish_reason': 'finished', 结束的原因！
 'finish_time': datetime.datetime(2024, 6, 11, 7, 54, 1, 20098),  结束的时间！
  'httpcompression/response_bytes': 131669,  压缩后的字节数量！
   'httpcompression/response_count': 1,       压缩之后的响应数量！
    'log_count/DEBUG': 5,       调试与正常的日志！
 'log_count/INFO': 10,
 'response_received_count': 2,   响应接受的数量！
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,     robot.txt的相关！
'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,  调度器的四个！
"""