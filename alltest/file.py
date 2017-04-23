# -*- conding: UTF-8 -*-

# try:
#     f=open('E:/python/test.txt','r')
#     print f.read()
# finally:
#     if f:
#         f.close()


# with open('E:/python/test.txt','r') as f:
#     # print f.read()
#     for line in f.readlines():
#         print(line.strip())

with open('E:/python/test.txt','w') as f:
    f.write('hello world---')