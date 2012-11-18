# -*- coding: utf-8 -*-
"""
#面试题# 左“{”，右”}"括号各N个，请打印出所有正确的组合，
比如当N=3，{}{}{}，{{{}}}，等为正确的组合。
如果写的代码是recursive，能否用iterative再写一个；反之亦然。
http://weibo.com/1915548291/z5J3dsL8M

@author: yaolong3
"""

import sys, os, time, random
import Queue

def _recursiveMatch(ans, cur, l, r):
    if 0 == r:
        ans.append(cur[:])
        return
    if l > 0:
        cur.append('{')
        _recursiveMatch(ans, cur, l - 1, r)
        cur.pop()
    if l < r:
        cur.append('}')
        _recursiveMatch(ans, cur, l, r - 1)
        cur.pop()

#递归方法
def recursiveMatch(n):
    ans = []
    cur = []
    _recursiveMatch(ans, cur, n, n)
    return ans

#标准队列 粗放型实现
def iterativeMatchV1(n):
    ans = []
    l, r = n, n
    q = Queue.Queue()
    q.put(([], l, r))
    while q.qsize() > 0:
        a, l, r = q.get()
        if 0 == r:
            ans.append(a)
            continue
        if l > 0:
            q.put((a + ['{'], l - 1, r))
        if l < r:
            q.put((a + ['}'], l, r - 1))
    return ans

#用栈 模拟回溯
def iterativeMatchV2(n):
    ans = []
    cs = ['{', '}']
    l, r = n, n
    #栈
    q = []
    q.append((0, l - 1, r, 0))
    while len(q) > 0:
        #k是左右括号的代号（用0、1表示），l r分别是左右括号剩的数量，f是回溯标记（1表示回溯）
        k, l, r, f = q[-1]
        if 0 == f:
            #非回溯状态
            if 0 == r:
                #获得一个解后修改该步为回溯状态
                ans.append([cs[i[0]] for i in q])
                q.pop()
                q.append((k, l, r, 1))
            elif l > 0:
                q.append((0, l - 1, r, 0))
            elif l < r:
                q.append((1, l, r - 1, 0))
        else:
            #回溯状态  若有 新的可达路径就前进 否则 继续回溯
            q.pop()
            if 0 == k:
                if l + 1 < r:
                    q.append((1, l + 1, r - 1, 0))
                else:
                    #走不下去， 修改上一步为回溯状态，继续回溯
                    if len(q) > 0:
                        k, l, r, f = q.pop()
                        q.append((k, l, r, 1))
            else:
                #修改上一步为回溯状态，继续回溯
                if len(q) > 0:
                    k, l, r, f = q.pop()
                    q.append((k, l, r, 1))
    return ans
              
t = 9

a = recursiveMatch(t)
for i in a:
    print ''.join(i)
print

b = iterativeMatchV1(t)
for i in b:
    print ''.join(i)
print

c = iterativeMatchV2(t)
for i in c:
    print ''.join(i)
print

print 'len a, b, c :', len(a), len(b), len(c)

print a == b, b == c, a == c