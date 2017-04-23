# -*- coding: UTF-8 -*-
# def pas_triangles():
#     a = [1]
#     while True:
#         yield a
#         a = [sum(i) for i in zip([0] + a, a + [0])]
 
# if __name__ == "__main__":
#     g = pas_triangles()
#     for n in range(10):
#         print(next(g))

if __name__=='__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j - 1]+a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print