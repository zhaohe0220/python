# -*- coding: UTF-8 -*-

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
# for data in ['micheal','tracy','sarah']:
text = raw_input("输入内容：")
s.send(text)
data = s.recv(1024)
print data
if data == 'exit':
    s.close()
    print 'Connection close'