import requests
from bs4 import BeautifulSoup

def get_bs_obj(url, headers = None, params = None):
    result = requests.get(url, headers = headers, params = params)
    soup = BeautifulSoup(result.content.decode('euc-kr','replace'), 'html.parser')
    return soup

def get_company_info(company_code):
    url = 'https://finance.naver.com/item/main.naver'
    params = {
        'code': company_code
    }

    soup = get_bs_obj(url, params = params)

    try:
        company_info = soup.select_one('div.new_totalinfo > dl.blind').find_all('dd')
    except:
        return None

    return company_info

# 삼성전자 종목 증시 정보 가져오기
codes = ['005930']

for code in codes:
    results = get_company_info(code)

    if results == None:
        print('None')
        continue

    for result in results:
        print(str(result)[4:-5])

