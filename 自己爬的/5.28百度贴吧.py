﻿import requests
from lxml import etree

url = 'https://tieba.baidu.com/f?fr=search&ie=utf-8&kw=%E7%AC%94%E8%AE%B0%E6%9C%AC&red_tag=b3364292370'

headers = {
    'Cookie': 'BAIDUID=ADC17AC5E7E2A24F8ACB55BD8C88AA28:FG=1; BDUSS=ZsTXdyUkx6RmNMcmktay1RNDBpfkw0eEEyYVQ4WnJFeW9MTUFWVnROZm5hSHRtRVFBQUFBJCQAAAAAAAAAAAEAAABZedmgyP3UwsrHztLG3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOfbU2bn21NmMH; BDUSS_BFESS=ZsTXdyUkx6RmNMcmktay1RNDBpfkw0eEEyYVQ4WnJFeW9MTUFWVnROZm5hSHRtRVFBQUFBJCQAAAAAAAAAAAEAAABZedmgyP3UwsrHztLG3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOfbU2bn21NmMH; BIDUPSID=ADC17AC5E7E2A24F8ACB55BD8C88AA28; PSTM=1716795169; H_PS_PSSID=60237_60269_60287_60298; BAIDUID_BFESS=ADC17AC5E7E2A24F8ACB55BD8C88AA28:FG=1; ZFY=gRRhS7kndu37YpcJin9bIxs9gEoOzbV1r4xhBCV45C8:C; STOKEN=c6ec27bd597f13671cfe9817846f0b28c6631b6af4b594c54dcdbba81eeafa5c; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1714376729,1716897551; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1716897551; BAIDU_WISE_UID=wapp_1716897551868_310; USER_JUMP=-1; 2698606937_FRSVideoUploadTip=1; video_bubble2698606937=1; XFI=b2a61040-1ce9-11ef-ad3a-bd327ddca8ce; BA_HECTOR=akaka120aha0alah858l04al7pf21v1j5bhog1u; arialoadData=false; ab_sr=1.0.1_Y2NjMTUyZmNlYTE5MmQ3Nzc5ZWIzZjE4ZjIzNzc0MGNiOTI2MDM4MjIwNmM5MTIzNjQxNmU3MjQ5NjBhOTRiZDk2ZTEyMDY3YTc4MTFiYjIyZmFmZGExYTg0NmY1MDVjYTM4MTY3YTg4ODEyMTIzYTFjMDlkNjQzMzg1N2I4M2JiMzBhZDBlOGE5OGE3M2ExZDFiMmMxM2ZhM2UwODdlNmI2YzViYjRjZTljMGVjZWY0MGQ1ZmY4OWU5YmMxN2Yy; st_data=d536065e2228b5b4c1fd88d2052726d604a7fba5ef630a380120cb99bbb721c4cc441f8646a5a944e65eb1804a43505af9f17927a7019079a9416042119ae3817b3dc6de0a3c87bf455440f52bed56235f31bde348bbb561682f0d77f3ca15e7df2f767bf0e1c713645a4687f59cb670dbf736daa9b7fb6500809033ccc15720a6a59656d1f2f1d843de24560b162973; st_key_id=17; st_sign=5d65e418; XFCS=DA6AFB9C1C4C9031DE961D252654876C2472A28F74E4AA7DE05922F42EEFE47B; XFT=38veaAh+iSnCDb4lujsAFPYRCsn4RTeQ+bajYT66NT0=; RT="z=1&dm=baidu.com&si=eb19f97d-31ef-49f3-ac7e-c0feebc93fa8&ss=lwqch03b&sl=5&tt=6gr&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=10ji&ul=1amp"',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

res = requests.get(url=url, headers=headers)

print(res.content.decode('utf-8'))
res = res.content.decode('utf-8')
html_tree = etree.HTML(res)
# print(html_tree)
# items = html_tree.xpath("//ul[@id='thread_list']")
# print(items)

# items = items.xpath("./li")
# print(items)
# print(len(items))
