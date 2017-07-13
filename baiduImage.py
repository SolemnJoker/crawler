# coding:UTF-8
import time
import os
from bs4 import BeautifulSoup
import requests
url = "http://image.baidu.com/search/acjson"
path = 'E:/personal/jiepai'


def getUrl(url, curParams=None):
    try:
        r = requests.get(url, params=curParams)
        return r
    except:
        return ""


def download(url, filename):
    try:
        ir = requests.get(url)
        ir.raise_for_status()
        if ir.status_code == 200:
            filePathName = os.path.join(path, filename)
            open(filePathName, 'wb').write(ir.content)
    except BaseException,e:
        print 'download error :%s'%filename
        print e.message

def request(params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        json = response.json()['data']
        for i in range(0, len(json)):
            if json[i].has_key('replaceUrl') :
                objUrl = json[i]['replaceUrl'][-1]['ObjURL']
                filename = os.path.split(objUrl)[1].split('?')[0]
                if(len(filename) != 0):
                    fromHost = json[i]['fromURLHost']
                    print 'Downloading from %s' % objUrl
                    download(objUrl, filename)
    except:
        return "get url error"

def search(keyword, minpage, maxpage):
    params = {
        'tn': 'resultjson_com',
        'word': keyword,
        'queryWord':keyword,
        'ie': 'utf-8',
        'cg': '',
        'ct':'201326592',
        'fp':'result',
        'cl':'2',
        'lm':'-1',
        'rn': '30',
        'ipn':'rj'
    };
    for i in range(minpage, maxpage):
        print 'Download page %d:'%i 
        params['pn'] = '%d' % (i * 30)
        request(params)

def start():
    if os.path.exists(path) == False:
        os.mkdir(path)
    search('街拍', 1, 10)
