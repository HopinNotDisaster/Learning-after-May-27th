import requests
from lxml import etree

# 目标网址
url = "https://book.zongheng.com/store/c0/c0/b0/u4/p1/v9/s9/t0/u0/i1/ALL.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

res = requests.get(url, headers=headers)

# print(res.text)
res = res.text
html_tree = etree.HTML(res)
# print(html_tree)
items = html_tree.xpath('//div[@class="store_collist"]')[0]
items = items.xpath('//div[contains(@class,"bookbox")]')
# print(items)
# print(len(items))
for item in items:
    # print(item)
    title = item.xpath(".//div[@class='bookname']/a/text()")[0]
    print(title)
    img_link = item.xpath(".//div[@class='bookimg']//img/@src")[0]
    print(img_link)
    detail_link = item.xpath(".//div[@class='bookname']/a/@href")[0]
    print(detail_link)