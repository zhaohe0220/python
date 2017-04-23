# -*- coding:UTF-8 -*-
# 冒泡排序
def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
        pass_num = pass_num - 1


if __name__ == '__main__':
    a_list = [20,40,30,90,50,80,70,60,1110,100]
    short_bubble_sort(a_list)
    print(a_list)