# -*- coding: UTF-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = raw_input('Email:')
password = raw_input('password:')
pop3_server = raw_input('POP3 server:')

server = poplib.POP3(pop3_server)
print(server.getwelcome())

server.user(email)
server.pass_(password)

print ('Message:%s.Size:%s' % server.stat())

resp,mails,octets = server.list()
print(mails)

index = len(mails)
resp,lines,octets = server.retr(index)

msg_content = '\r\n'.join(lines)

msg = Parser().parsestr(msg_content)

server.quit()

def print_info(msg,indent = 0):
    if indent == 0:
        for header in ['Form','To','Subject']:
            value = msg.get(header,'')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr,addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s<%s>' % (name,addr)
            print('%s%s:%s' % (' ' * indent,header,value))
    if(msg.ismultipart()):
        parts = msg.get_payload()
        
