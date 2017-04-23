# -*- coding:UTF-8 -*-
import urllib
import urllib2

values = {"LoginCode":"2333","LoginPwd":"123456"}
data = urllib.urlencode(values) 
url = "http://www.bingowang.com/Index/Login"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()