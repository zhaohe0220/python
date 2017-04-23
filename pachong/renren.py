# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import re

class SDU:
    def __init__(self):
        self.LoginUrl = 'http://www.renren.com/PLogin.do'
        self.cookies = cookielib.CookieJar()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent':self.user_agent}
        self.postdata = urllib.urlencode({
            # '__VIEWSTATE':'dDwtMTg3MTM5OTI5MTs7Pii3m+vkRfT6nfYKghkfGHRdW+aX',
            # 'TextBox1':'20120530127',
            # 'TextBox2':'',
            # 'RadioButtonList1_2':'checked'
            'email':'1259110433@qq.com',
            'password':''
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.LoginUrl,
            data = self.postdata,
            headers = self.headers
        )
        result = self.opener.open(request)
        print result.read().decode('utf-8')

sdu = SDU()
sdu.getPage()