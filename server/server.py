#!//user/bin/python
# -*- coding: UTF-8 -*-
import socket

s=socket.socket()

host=socket.gethostname()
# host = '192.168.0.71'
port=12345
s.bind((host,port))

s.listen(5)
while True:
    text = raw_input("内容：\n")
    c,addr=s.accept()
    print '链接地址：',addr
    c.send(text)
    c.close()