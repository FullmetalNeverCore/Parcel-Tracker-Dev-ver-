import requests
from bs4 import BeautifulSoup as bs 

courier = input('input courier')
trck_num = input("input track number")

URL = 'https://gdeposylka.ru/courier/'+courier+'/tracking/'+trck_num
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r  

def get_content(html):
    soup = bs(html, 'html.parser')
    itms = soup.findAll('div', class_='col-md-8')
    prc = []
    for itm in itms:
        prc.append(
            itm.find('span', class_='td info status-iconed').text
        )
    print(prc)
    print(len(prc))
    jeez = str(prc)
    j = jeez.replace("\\n", "")
    print(j)


def parse():
    print("Parcel-Tracker")
    print("Ver inf-dev 0.1")
    html = get_html(URL)
    if html.status_code == 200:
        print(html.status_code)
        get_content(html.text)
    else:
        print('Err: ' + html.status_code)

parse()
