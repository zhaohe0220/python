#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
s=raw_input('inpiut a string:\n')
letters=0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print 'char =%d,space = %d,digit=%d,other=%d'%(letters,space,digit,other)