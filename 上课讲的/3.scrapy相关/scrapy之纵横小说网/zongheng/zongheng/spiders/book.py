import re
import scrapy
from lxml import etree
from zongheng.items import BookItem, ChapterItem

# 调度器三件事  入队出队，优先级排序，数据去重！

class BookSpider(scrapy.Spider):
    # 这个爬虫的名字，和启动相关！
    name = "book"

    # 指出允许的域名！如果去掉的话就是允许爬取全部的域名。
    # allowed_domains = ["xxx"]

    # 爬虫的起始url
    # 该链接的响应默认会由parse方法进行解析！
    start_urls = [f"https://book.zongheng.com/store/c0/c0/b0/u4/p{page}/v0/s9/t0/u0/i1/ALL.html" for page in
                  range(1, 1 + 1)]

    # 这个方法是用来解析起始url的！
    def parse(self, response):
        print(f"正在爬取{response.url}")
        # 下面这个是lxml的xpath写法！
        # html_str = response.body.decode()
        # root = etree.HTML(html_str)
        # book_list = root.xpath("//div[contains(@class,'bookbox')]")
        # print(len(book_list))
        # for book in book_list:
        #     book_name = "".join(book.xpath(".//div[@class='bookname']/a/text()"))
        #     book_url = "".join(book.xpath(".//div[@class='bookname']/a/@href"))
        #     book_id = re.search(r"\d+", book_url).group()
        #     print(f"书名是：{book_name} 书ID是：{book_id}")

        # 建议使用scrapy封装之后的xpath写法!
        book_list = response.xpath("//div[contains(@class,'bookbox')]")
        # print(len(book_list))
        for book in book_list:
            book_name = book.xpath(".//div[@class='bookname']/a/text()").get()
            book_url = book.xpath(".//div[@class='bookname']/a/@href").get()
            book_id = re.search(r"\d+", book_url).group()
            # 向管道传输的数据
            yield BookItem(book_name=book_name, book_url=book_url, book_id=book_id)
            print(f"书名是：{book_name} 书ID是：{book_id}")

            # 发送新的请求
            # 下面这个方法有点复杂！！！！！
            url = "https://bookapi.zongheng.com/api/chapter/getChapterList"
            # # callback 定义该请求的响应由哪个函数进行解析！
            # headers = {
            #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # }
            # yield scrapy.Request(url=url, callback=self.parse_chapter,method="POST",
            #                      headers=headers,body=f"bookId={book_id}",)

            # 使用封装好的方法来进行新表单类的请求！
            # 注意：这里需要将book_id传递给meta字典中！可以在回调函数之间传递参数！
            yield scrapy.FormRequest(url=url, callback=self.parse_chapter, formdata={"bookId": book_id},
                                     meta={"book_id": book_id})
            break
    # 自定义的回调函数！
    def parse_chapter(self, response):
        book_id = response.meta.get("book_id")
        # 这里的chapter_list实际上是卷的列表！
        for chapter_list in response.json()["result"]["chapterList"]:
            for chapter in chapter_list["chapterViewList"]:
                chapter_name = chapter["chapterName"]
                chapter_id = chapter["chapterId"]
                chapter_url = f"https://read.zongheng.com/chapter/{book_id}/{chapter_id}.html"
                # print(f"章节名是：{chapter_name} 章节链接是：{chapter_url}, 章节ID是：{chapter_id}")
                # # 向管道传输数据
                chapter_item = ChapterItem(chapter_name=chapter_name, chapter_url=chapter_url, chapter_id=chapter_id)
                yield scrapy.Request(url=chapter_url, callback=self.parse_content,meta={"chapter_item":chapter_item})

    def parse_content(self, response):
        chapter_item = response.meta.get("chapter_item")
        content = "\n".join(response.xpath("//div[@class='content']/p/text()").getall())
        chapter_item["content"] = content
        yield chapter_item

