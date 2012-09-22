# -*- coding: utf-8 -*-

'''
http://weibo.com/1915548291/yD0oyw4vb
#苹果面试题# 洗牌：你手上有一副313张的牌，做如下操作：
1. 拿出最上面一张，放到桌上；
2. 拿出最上面一张，放到手中这幅牌的最下面；
3. 重复1和2直到所有的牌都放到桌上，再从桌上拿起这副牌，
重复1，2和3，直到这副牌中每张牌的顺序和最初发牌时的一样。
你觉得需要多少轮操作？能写代码模拟吗？
'''
import os
import sys
import time


num = 313

def check(a):
    for i in xrange(0, num):
        if a[i] != i:
            return False
    return True

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

def run():
    '''
    d[i]用于记录i最早在第几轮复位
    当d[0~num-1]都求出后计算最小公倍数
    '''
    cnt = 0
    a = range(0, num)
    b = []

    d = [0] * num
    cntd = 0
    while(1):
        for i in xrange(0, num - 1):
            b.insert(0, a.pop(0))
            a.append(a.pop(0))
        b.insert(0, a.pop(0))
        cnt = cnt + 1
        for i in xrange(0, num):
            if b[i] == i and d[i] == 0:
                d[i] = cnt
                cntd = cntd + 1
        if cntd == num:
            None
            #不break就会让模拟一直进行下去直到一轮里全部复位
            break
        #print b
        if check(b):
            break
        a = b
        b = []

    result = d[0]
    for i in xrange(1, num):
        result = lcm(result, d[i])
    print 'd:', d
    print 'cnt:', cnt
    print 'result:', result

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isalnum() == True and int(sys.argv[1]) > 0:
        num = int(sys.argv[1])
    else:
        print 'ie.: python poker.py 313'
        exit(-1)
    run()

