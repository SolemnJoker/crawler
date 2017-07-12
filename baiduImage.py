# coding:UTF-8
from bs4 import BeautifulSoup
import requests
import time
url = "http://image.baidu.com/search/acjson"
path = "./"


def getUrl(url, curParams=None):
    try:
        r = requests.get(url, params=curParams)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def download(url, filename):
    ir = requests.get(url)
    if ir.status_code == 200:
        filePathName = os.path.json(path, filename)
        open(filePathName, 'wb').write(ir.content)


def requests(params):
    response = requests.get(url, params=params)
    print response
    json = response.json()['imgs']

    for i in range(0, len(json)):
        filename = os.path.split(json[i]['objURL'])[1]
        print 'Downloading from %s' % json[i]['objURL']
        download(json[i]['objURL'], filename)


def search(keyword, minpage, maxpage):
    params = {
        'tn': 'resultjsonavatarnew',
        'ie': 'utf-8',
        'cg': '',
        'itg': '',
        'z': '0',
        'fr': '',
        'width': '',
        'height': '',
        'lm': '-1',
        'ic': '0',
        's': '0',
        'word': keyword,
        'st': '-1',
        'gsm': '1e',
        'rn': '30'
    };
    for i in range(minpage, maxpage):
        params['pn'] = '%d' % (i * 30)
        requests(params)

path = './jiepai'
search('街拍', 1, 10)
