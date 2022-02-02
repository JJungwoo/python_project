import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
datas = []

for tr in trs:
    name = tr.select_one('th > a').get_text()
    current_price = tr.select_one('td').get_text() 
    change_direction = tr['class'][0]
    change_price = tr.select_one('td > span').get_text()
    datas.append([name, current_price, change_direction, change_price])

for data in datas:
    print(data)

# 참고: https://wikidocs.net/91464
