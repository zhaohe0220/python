# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

# page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
# headers = {'User-Agent':user_agent}
# try:
#     request = urllib2.Request(url,headers=headers)
#     response = urllib2.urlopen(request)
#     # print response.read()
#     content = response.read().decode('utf-8')
#     pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+'="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#     items = re.findall(pattern,content)
#     for item in items:
#         # haveImg = re.search("img",item[3])
#         # if not haveImg:
#         print item[0],item[1],item[2],item[3],item[4]
# except urllib2.URLError,e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []
        self.enable = False
        
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接失败，原因：",e.reason
                return None
                
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败......"
            return None
        pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+'="content".*?>(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search("img",item[1])
            if not haveImg:
                pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
        return pageStories
        
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1


    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t赞:%s\n%s" % (page,story[0],story[3],story[1])
            
    def start(self):
        print u"正在读取，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
                
spider = QSBK()
spider.start()