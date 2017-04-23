#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

class pythonThread(threading.Thread):
    def __init__(self,name,age):
        threading.Thread.__init__(self)
        self.name=name
        self.age=age

    def run(self):
        print 'this is thread start'
        print_mes(self.name,self.age)
        print 'this is thread end'

def print_mes(name,age):
    time.sleep(5)
    print 'my name is %s and age is %s'%(name,age)


thread = pythonThread('fengzi',23)
thread.start()
