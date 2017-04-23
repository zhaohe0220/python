#!/usr/bin/python
# -*- coding: UTF-8 -*-

def cutput(s,l):
    if l == 0:
        return
    print(s[l-1])
    cutput(s,l-1)

s = raw_input('Input a string:')
l = len(s)
cutput(s,l)



