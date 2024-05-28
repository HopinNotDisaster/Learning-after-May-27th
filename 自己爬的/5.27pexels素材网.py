import requests

next = '2024-05-28T09%3A03%3A43.117Z'
while 1:
    url = f'https://www.pexels.com/zh-cn/api/v2/feed?seed={next}&per_page=12&seo_tags=true'

    headers = {
        'Referer': 'https://www.pexels.com/zh-cn/',
        'Cookie': '_ga=GA1.1.39825888.1716802803; OptanonAlertBoxClosed=2024-05-27T09:40:05.154Z; active_experiment={"id":"paginatedMediumAds","name":"Paginate ads in medium suggestions","variant":{"id":"1","name":"test","weight":50}}; __cf_bm=XRBi1MxdfUkwlBBbK8ZrbtypAXXulknZpkh9k9FyIRU-1716895441-1.0.1.1-G690qlW.DQTjzFZupgZOI.Y0HkFkHble5Y6uh_gUiAkx0THaLbZlHcd4m10HN44NtgD4tHn3gyjySTJS7nA..w; _sp_ses.9ec1=*; _sp_id.9ec1=04c6af4e-4f90-4602-a54b-74ee6903c69f.1716802808.2.1716895443.1716803508.a91bf5bd-cec5-46c4-aa98-264fe1c08f80.e4a80aa7-ee7b-4135-a9fb-b81a33ef1e6c.fd1cb453-d57b-4043-9b16-9c8abdb1b2fc.1716895443168.2; _ga_8JE65Q40S6=GS1.1.1716895443.2.0.1716895443.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+28+2024+19%3A24%3A04+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BHA&AwaitingReconsent=false',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Secret-Key': 'H2jk9uKnhRmL6WPwh89zBezWvr'
    }

    res = requests.get(url=url, headers=headers)
    print(res.json())
    next = res.json()['pagination']["cursor"]
    print(next)
