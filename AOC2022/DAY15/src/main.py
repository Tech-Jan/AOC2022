import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
response = requests.get('https://panel.op-net.com/login', headers=headers)
print(response.text)
print(response)