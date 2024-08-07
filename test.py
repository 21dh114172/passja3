from cytls import cytls

headers = {
    "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": '"Windows"',
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    "Sec-GPC": '1',
    "Accept-Language": 'en-US,en;q=0.6',
    "Sec-Fetch-Site": 'none',
    "Sec-Fetch-Mode": 'navigate',
    "Sec-Fetch-User": '?1',
    "Sec-Fetch-Dest": 'document',
    "Accept-Encoding": 'gzip, deflate, br, zstd'

}

proxies =  {"http": "http://13.83.94.137:3128"}

url ="https://passport.yandex.ru/passport?isFromQr=1&mode=restore"
req = cytls.get(url, headers=headers, proxies=proxies)


dt = req.text
print(req.status_code)
print(req.headers["Set-Cookie"])
#print("Response:" + dt)
