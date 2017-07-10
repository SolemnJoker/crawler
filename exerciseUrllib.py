# coding:UTF-8
import urllib
import urllib2

url = 'http://www.zhihu.com/#signin'
userAgent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER"
headers = {'User-Agent':userAgent}
data = {'username':'test','password':'test2'}
dataencode = urllib.urlencode(data)
request = urllib2.Request(url,None,headers)
response = urllib2.urlopen(request)

