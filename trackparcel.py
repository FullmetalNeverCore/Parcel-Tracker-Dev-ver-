import requests
import teletrack 
from teletrack import *
import asyncio 
from bs4 import BeautifulSoup as bs 

courier = ['russian-post','cainiao','latvijas-pasts','dpd-russia','dhl-global-mail', 'ups']


num = 0
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'accept': '*/*'}

async def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r  

async def url_creator(track, id):
    r = open("tnum.txt", "w", encoding='utf-8')
    u = id 
    r.write(track + ".")
    r.close()
    regi = {}
    try:
        with open("regi.txt", encoding='utf-8') as check_ab:
            for line in check_ab:
                for word in line.split('\n'):
                    (key, val) = word.split(",")
                    regi[str(val)] = key
    except Exception as e:
        print("err" )
        print(e)
        pass
    if track in regi:
        print(1)
        URL = 'https://gdeposylka.ru/courier/'+regi.get(track)+'/tracking/'+track
    else:
        print(2)
        URL = 'https://gdeposylka.ru/courier/'+courier[num]+'/tracking/'+track
    html = await get_html(URL)
    print(regi)
    if html.status_code == 200:
        print(html.status_code)
        await get_content(html.text, u, track)
    else:
        print('Err: ' + html.status_code)

async def get_content(html, id, track):
        global num
        soup = bs(html, 'html.parser')
        u2 = id
        itms = soup.findAll('div', class_='col-md-8')
        prc = []
        track = track
        for itm in itms:
            prc.append(
                itm.find('span', class_='td info status-iconed').text
            )
        if len(prc) == 0:
                num += 1
                await parse_again(u2, track)
        else:
                jeez = str(prc)
                j = jeez.replace("\\n", "")
                r = open("regi.txt", "a")
                form = str(courier[num]) + "," + str(track) + "\n"
                r.write(form)
                r.close()
                await async_get_content(j, u2)

async def async_get_content(data, id):
    d = data 
    i = id
    await teletrack.send_msg(d, i)

async def send_to_usr(data, id):
    d = data
    i = id 
    await trackparcel.send_msg(d, i)


async def parse_again(id,track):
    print("Parcel-Tracker")
    print("Ver inf-dev 0.1")
    i2 = id
    r1 = track
    URL1 = 'https://gdeposylka.ru/courier/'+courier[num]+'/tracking/'+r1
    html = await get_html(URL1)
    if html.status_code == 200:
        print(html.status_code)
        await get_content(html.text, i2, r1)
    else:
        print('Err: ' + html.status_code)

