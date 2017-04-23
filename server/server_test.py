#!/user/bin/python
# -*- coding: UTF-8 -*-

import socket

s= socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))

s.listen(1)
while True:
    c,addr=s.accept()
    c.send('hahahaha')
    c.close()
