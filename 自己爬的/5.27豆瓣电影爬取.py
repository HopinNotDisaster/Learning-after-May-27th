import requests

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Cookie': 'bid=8YpScs5_ieA; _pk_id.100001.4cf6=7883bde0cffa817d.1716810108.; _pk_ses.100001.4cf6=1; __utma=30149280.429059921.1716810108.1716810108.1716810108.1; __utmb=30149280.0.10.1716810108; __utmc=30149280; __utmz=30149280.1716810108.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1265963524.1716810108.1716810108.1716810108.1; __utmb=223695111.0.10.1716810108; __utmc=223695111; __utmz=223695111.1716810108.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
}
res = requests.get(url=url, headers=headers)
# print(res.json())
res = res.json()
print(res)
print(len(res))