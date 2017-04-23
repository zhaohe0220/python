# -*- coding: UTF-8 -*-

import xlrd
from pyExcelerator import *

w = Workbook()
ws = w.add_sheet('Sheet1')

fname = "mini.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname

nrows = sh.nrows
ncols = sh.ncols
print "nrows %d,ncols %d" % (nrows,ncols)

for i in range(0,nrows):
    j = 0
    row_datas = sh.row_values(i)
    for row_data in row_datas:
        pkgdata = str(row_data).split(',')
        for data in pkgdata:
            ws.write(i,j,data)
            j += 1
w.save('reflect.xls')