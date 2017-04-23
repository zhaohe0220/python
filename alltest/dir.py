# -*- coding: UTF-8 -*-

import os

# print os.name系统名称
# print os.environ环境变量
# print os.path.abspath('.')当前所在路径
# print os.path.join('E:/python','testdir')拼接文件
# os.mkdir('E:/python/testdir')
# os.mkdir('E:/python/dir')创建目录
# os.rmdir('E:/python/dir')删除目录
# print os.path.splitext('E:/python/test.txt')分割文件格式
# os.rename('E:/python/test.txt','E:/python/renametest.py')重命名
# os.remove('E:/python/renametest.py')删除文件

# print [x for x in os.listdir('.') if os.path.isdir(x)]#列出当前目录下的所有目录

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#筛选文件格式为py

