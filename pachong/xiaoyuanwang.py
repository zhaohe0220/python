# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SDU:
    def __init__(self):
        self.LoginUrl = 'http://218.57.111.210:81/default2.aspx'
        # self.LoginUrl = 'http://218.57.111.210:81/(b5s2k4ragnlktlelzyciom45)/xs_main.aspx'
        self.CaptchaUrl = 'http://218.57.111.210:81/CheckCode.aspx'
        self.cookies = cookielib.CookieJar()

        handle = urllib2.HTTPCookieProcessor(self.cookies)
        opener = urllib2.build_opener(handle)

        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent':self.user_agent}
        picture = opener.open(self.CaptchaUrl).read()
        local = open('e:/image.jpg','wb')
        local.write(picture)
        local.close()
        secretCode = raw_input('输入验证码：\n')

        self.postdata = urllib.urlencode({
            '__VIEWSTATE':'dDwtMTg3MTM5OTI5MTs7Pii3m+vkRfT6nfYKghkfGHRdW+aX',
            'TextBox1':'20120530127',
            'TextBox2':'',
            'RadioButtonList1':'学生',
            'TextBox3':secretCode
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.LoginUrl,
            data = self.postdata,
            headers = self.headers
        )
        result = self.opener.open(request)
        print result.read().decode('gbk')

sdu = SDU()
sdu.getPage()