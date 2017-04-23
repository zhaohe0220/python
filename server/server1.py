# -*- coding: UTF-8 -*-
import threading
import time
import socket

def tcplink(sock,addr):
    print 'Accept new connection from %s：%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        print data
        time.sleep(1)
        if data == 'exit':
            sock.close()
            print 'Connection from %s:%s close' % addr
        text = raw_input("输入内容：")
        sock.send(text)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print 'waiting for connection...'
while True:
    sock,addr = s.accept()
    t = threading.Thread(target = tcplink,args = (sock,addr))
    t.start()