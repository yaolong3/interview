# -*- coding: utf-8 -*-
"""

@author: yaolong3
http://weibo.com/yaolong3

http://weibo.com/1269043140/z1WXNjTnd
刚才看到有人分享了这么一道#谷歌面试题#：
函数f(0)=f(1)=1, f(2)=2, f(n)=f(n-1)f(n-2)f(n-3)，
不考虑溢出，给定n编程求f(n)。这位同学给了个O(n)的解法就以为完事了。
其实一个简单并且很常用的优化就可以使算法复杂度大大降低，大家知道是什么优化吗？CC @陈利人

"""


import sys

A = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
###三阶矩阵快速幂乘
###A * [[x], [y], [z]] = [[y], [z], [x+y+z]]
###g(6) = A*A*A*A*[[x], [y], [z]] = (A*A)*(A*A)*[[x], [y], [z]]

def mul(a, b):
    assert(len(a[0]) == len(b))
    row = len(a)
    col = len(b[0])
    c = [[0]*col for i in xrange(row)]
    
    for i in xrange(row):
        for j in xrange(col):
            for k in xrange(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def solve(a, n):
    if n == 1:
        return a
    b = solve(a, n / 2)
    b = mul(b, b)
    if n % 2:
        b = mul(b, a)
    return b

n = 7
#g(i) = g(i-1) + g(i-2) + g(i-3)
g = solve(A, n - 2)
#f(i) = f(i-1) * f(i-2) * f(i-3)
f = 1 << g[-1][-1]
print g
print f

