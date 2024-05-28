import json
import time
import requests

for page in range(1, 499):

    # 请求
    url = f'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123044986676596757946_1716800069025' \
          f'&sortColumns=NOTICE_DATE%2CSUM%2CRECEIVE_START_DATE%2CSECURITY_CODE&sortTypes=-1%2C-1%2C-1%2C1&pageSize=50' \
          f'&pageNumber={page}&reportName=RPT_ORG_SURVEYNEW&columns=SECUCODE%2CSECURITY_CODE%2CSECURITY_NAME_ABBR%2CNOTICE_DATE' \
          f'%2CRECEIVE_START_DATE%2CRECEIVE_PLACE%2CRECEIVE_WAY_EXPLAIN%2CRECEPTIONIST%2CSUM&quoteColumns=f2~01' \
          f'~SECURITY_CODE~CLOSE_PRICE%2Cf3~01~SECURITY_CODE~CHANGE_RATE&quoteType=0&source=WEB&client=WEB&filter=(' \
          f'NUMBERNEW%3D%221%22)(IS_SOURCE%3D%221%22)(RECEIVE_START_DATE%3E%272021-05-27%27) '

    # params = {
    #     'callback': 'jQuery11230482143316415262_1716801743142',
    #     'sortColumns': 'NOTICE_DATE%2CSUM%2CRECEIVE_START_DATE%2CSECURITY_CODE',
    #     'sortTypes': '-1%2C-1%2C-1%2C1',
    #     'pageSize': 50,
    #     'pageNumber': 2,
    #     'reportName': 'RPT_ORG_SURVEYNEW',
    #     'columns': 'SECUCODE%2CSECURITY_CODE%2CSECURITY_NAME_ABBR%2CNOTICE_DATE%2CRECEIVE_START_DATE%2CRECEIVE_PLACE%2CRECEIVE_WAY_EXPLAIN%2CRECEPTIONIST%2CSUM',
    #     'quoteColumns': 'f2~01~SECURITY_CODE~CLOSE_PRICE%2Cf3~01~SECURITY_CODE~CHANGE_RATE',
    #     'quoteType': 0,
    #     'source': 'WEB',
    #     'client': 'WEB',
    #     'filter': '(NUMBERNEW%3D%221%22)(IS_SOURCE%3D%221%22)(RECEIVE_START_DATE%3E%272021-05-27%27)',
    # }

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    #     'Cookie': 'qgqp_b_id=5613353f33410681a61bc11e242cb60a; st_si=02776285827110; st_asi=delete; JSESSIONID=AC2E166CD40E61AB45520AAC548B7EB3; st_pvi=22031946122739; st_sp=2024-05-27%2016%3A53%3A58; st_inirUrl=; st_sn=3; st_psi=20240527172223718-113300301541-2361797804',
    # }

    res = requests.get(url=url)
    # print(res)
    # print(res.text[43:-2])
    res = res.text[43:-2]
    res = json.loads(res)
    # # print(res,type(res),len(res))
    datas = res["result"]["data"]
    print(f"正在输出第{page}页的数据！")
    for d in datas:
        code = d["SECURITY_CODE"]
        name = d["SECURITY_NAME_ABBR"]
        close_price = d["CLOSE_PRICE"]
        change_rate = f'{d["CHANGE_RATE"]}%'
        print(code, name, close_price, change_rate)
    time.sleep(1)
    # redundant = "jQuery1123044986676596757946_1716800069025("
    # 43
    # print(len(redundant))
