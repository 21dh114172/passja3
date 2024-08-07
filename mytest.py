from cytls import cytls

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

proxies = {"https": "http://13.83.94.137:3128"}

url ="https://example.com/"
req = cytls.get(url, headers=headers, proxies=proxies)

dt = req.text
print(req.status_code)
print(req.headers)
print(req.cookies)
print(dt)