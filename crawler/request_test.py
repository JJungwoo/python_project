import requests

url = 'https://finance.naver.com/item/main.naver'

params = {
    'code': '005930'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    html = response.text
    print(response.url + ' get success')
else :
    print(response.status_code)

