# -*- coding: UTF-8 -*-

name_list = []
for i in range(10):
    name = raw_input("input a name:")
    name_list.append(name)
sort_list = sorted(name_list)
for i in range(len(sort_list)):
    print sort_list[i]
