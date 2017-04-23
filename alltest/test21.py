# -*- coding: UTF-8 -*-
# x = int(raw_input("请输入一个数字：\n"))
x = 14354
a = x / 10000
# print x
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print "5位数",e,d,b,c,a
elif b != 0:
    print "4位数",e,d,b,c
elif c != 0:
    print "3位数",e,d,b
elif d != 0:
    print "2位数",e,d
else:
    print "1位数",e