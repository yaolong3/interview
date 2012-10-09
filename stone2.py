'''
http://weibo.com/1915548291/yEeaUDS2L
#谷歌面试题# 两个玩家，一堆石头，假设多于100块，两人依次拿，最后拿光者赢，
规则是：1. 第一个人不能一次拿光所有的；
2. 第一次拿了之后， 每人每次最多只能拿对方前一次拿的数目的两倍。
求先拿者必胜策略, 如果有的话。怎么证明必胜。
有的面试，考察的是过程，比如，思考的方式，交流的畅通，等。
'''
'''
在石子数非斐波那契数时 第一步最多能取多少石子
a[i][j]表示剩i粒石头时该次拿j粒的 必胜状态，必胜为1，否则为0。
如果a[i-j][1 to 2*j]均为0，则a[i][j]为1，否则为0
'''
import os
import sys
import time
#import pprint

n = 1000

a = [[0]*n for i in xrange(0, n)]
a[1] = [0, 1]
a[2] = [0, 0, 1]
a[3] = [0, 0, 0, 1]

for i in xrange(4, n - 1):
    j = 1
    while j <= (i - 1) / 3:
        flag = 1
        for k in xrange(1, 2*j+1):
            if a[i-j][k] != 0:
                flag = 0
                break
        a[i][j] = flag
        j += 1
        
    while j < i:
        a[i][j] = 0
        j += 1
    a[i][i] = 1
    
#for i in xrange(1, 13):
#    print i, a[i][0:i+1]

for i in xrange(1, 110):
    flag = 0
    for j in xrange(1, (i - 1) / 3 + 1):
        if a[i][j] == 1:
            flag = j
    print (i, flag)
    

