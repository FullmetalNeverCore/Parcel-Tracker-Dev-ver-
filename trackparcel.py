import requests
from bs4 import BeautifulSoup as bs 

courier = ['russian-post','cainiao','latvijas-pasts','dpd-russia','dhl-global-mail']
trck_num = input("input track number")

num = 0
URL = 'https://gdeposylka.ru/courier/'+courier[num]+'/tracking/'+trck_num
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r  

def get_content(html):
    global num
    soup = bs(html, 'html.parser')
    itms = soup.findAll('div', class_='col-md-8')
    prc = []
    for itm in itms:
        prc.append(
            itm.find('span', class_='td info status-iconed').text
        )
    print(prc)
    print(len(prc))
    if len(prc) == 0:
        num += 1
        print(num)
        parse_again()
    jeez = str(prc)
    j = jeez.replace("\\n", "")
    print(j)


def parse():
    print("Parcel-Tracker")
    print("Ver inf-dev 0.2")
    html = get_html(URL)
    if html.status_code == 200:
        print(html.status_code)
        get_content(html.text)
    else:
        print('Err: ' + html.status_code)

def parse_again():
    print("Parcel-Tracker")
    print("Ver inf-dev 0.1")
    URL1 = 'https://gdeposylka.ru/courier/'+courier[num]+'/tracking/'+trck_num
    print(URL1)
    html = get_html(URL1)
    if html.status_code == 200:
        print(html.status_code)
        get_content(html.text)
    else:
        print('Err: ' + html.status_code)


parse()
