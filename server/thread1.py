#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import logging


exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name,self.counter,5)
        print "Exiting "+self.name

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threading.exit()
        time.sleep(delay)
        print "%s:%s"%(threadName,time.ctime(time.time()))
        counter -= 1
        
thread1=myThread(1,"Threaad-1",1)
thread2=myThread(2,"Threaad-2",2)

thread1.start()
thread2.start()


print "exiting main thread"