#!/usr/bin/python
# -*- coding: UTF-8 -*-
# if __name__=='__main__':
#     import datetime
#     import time
    # print time.ctime(time.time())
    # print time.asctime(time.localtime(time.time()))
    # print time.asctime(time.gmtime(time.time()))
    
    # start = time.time()
    # time.sleep(6)
    # end = time.time()
    # print end - start
    
    # start = time.clock()
    # for i in range(10000):
    #     print i
    # end = time.clock()
    # print 'different is %6.3f' % (end - start)
    
    
   from dateutil import parser
   dt = parser.parse("Aug 28 2015 12:00PM")
   print dt