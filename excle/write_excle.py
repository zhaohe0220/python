from pyExcelerator import *

w = Workbook()
ws = w.add_sheet('Hey,Hades')
ws.write(0,0,'bit')
ws.write(0,1,'huang')
ws.write(1,0,'xuan')
w.save('mini.xls')