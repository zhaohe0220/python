import urllib
import urllib2
# from lxml import etree



if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    headers = {'User-Agent':user_agent}
    url = 'http://www.qiushibaike.com/hot/'
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    pageCode = response.read()

    selector = etree.HTML(pageCode)

    content = selector.xpath('//*/div[1]/a[2]/h2/text()')
    for each in content:
        print each