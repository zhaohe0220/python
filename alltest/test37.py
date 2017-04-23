# -*- coding: UTF-8 -*-
TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print 'if the num that you input below fifth，program will stoped'
again = 1
while again:
    num = int(raw_input('input number:'))
    print 'result is %d' %(SQ(num))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE