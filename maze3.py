# -*- coding: utf-8 -*-
"""

@author: yaolong3

#民间图灵奖#@图灵教育 提供《思考的乐趣：Matrix67数学笔记》http://t.cn/z0gjZz9 作为奖品。
“迷宫”题：从图左边入口处的2011进去，在迷宫里转悠，最后变成2012从右边出来。
可以在迷宫里转圈，可以重复之前走过的路，但不能回退。
周日11/11选出5位完成好的代码的同学送出。@梁斌penny @图灵谢工
http://weibo.com/1915548291/z4eTPtAnv
"""

import sys, os
import time
import threading
import Queue

s = ['//2)', '+7)', '*3)', '-5)', '//2)', '+7)', '*3)', '-5)', '', '']

def div3(v):
    if v % 3 == 0:
        return (v // 3,)
    return ()
    
def mul2(v):
    return (v * 2, v * 2 + 1)

#把4个算子分拆成逆时针和顺时针方向，
#分别用索引0123和4567表示逆时针和顺时针的/2+7*3-5，用8表示2011，9表示2012
#反向搜索的算子，由于除2操作的逆操作存在两个答案，所以算子返回的是元组
fsr = (mul2, lambda x:(x-7,), div3, lambda x:(x+5,),
       mul2, lambda x:(x-7,), div3, lambda x:(x+5,),
       lambda x:(x,), lambda x:(x,))
#正向搜索的算子
fsp = (lambda x:x//2, lambda x:x+7, lambda x:x*3, lambda x:x-5,
       lambda x:x//2, lambda x:x+7, lambda x:x*3, lambda x:x-5,
       lambda x:x)
#mp表示当前索引能到达的结点，用于正向搜索
mp = [[1, 6, 3], [0], [4, 1, 3], [2], [5], [3, 4, 6], [7], [4, 1, 6], [0, 5]]
#mr表示能到达当前结点的结点索引，用于反向搜索
mr = [[1, 8], [0, 2, 7], [3], [0, 2, 5], [2, 5, 7], [4, 8], [0, 5, 7], [6], [], [3]]
#用于正向搜索的队列
qp = Queue.Queue()
#用于反向搜索
qr = Queue.Queue()
#用于正向搜索状态去重和保存路径
sp = {}
#用于反向搜索
sr = {}

lock = threading.Lock()
retp = (0, 0)
retr = (0, 0)
flag = False
  
def bfsPositive(v=2011, index=8):
    global qp, sp, sr, flag, retp, retr
    qp.put((v, index, 2011, 8))
    while qp.qsize() > 0 and not flag:
        v, index, preValue, preIndex = qp.get()
        if (v, index) in sp:
            continue
        if (v, index) in sr:
            lock.acquire()
            if not flag:
                retp = (preValue, preIndex)
                retr = (v, index)
                flag = True
            lock.release()
            break
        sp[(v, index)] = (preValue, preIndex)
        if v == 2012 and index == 3:
            lock.acquire()
            if not flag:
                retp = (preValue, preIndex)
                retr = None
                flag = True
            lock.release()
            break
        for i in mp[index]:
            qp.put((fsp[i](v), i, v, index))
    return

def bfsReverse(v=2012, index=3):
    global qr, sr, sp, flag, retp, retr
    qr = Queue.Queue()
    qr.put((v, index, 2012, 3))

    while qr.qsize() > 0 and not flag:
        v, index, preValue, preIndex = qr.get()
        if (v, index) in sr:
            continue
        if (v, index) in sp:
            lock.acquire()
            if not flag:
                retr = (preValue, preIndex)
                retp = (v, index)
                flag = True
            lock.release()
            break
        sr[(v, index)] = (preValue, preIndex)

        if v == 2011 and (index == 0 or index == 5):
            lock.acquire()
            if not flag:
                retp = None
                retr = (v, index)
                flag = True
            lock.release()
            break
        for i in mr[index]:
            for j in fsr[index](v):
                qr.put((j, i, v, index))
    return

tp = threading.Thread(target = bfsPositive)
tr = threading.Thread(target = bfsReverse)

begin = time.time()

tp.start()
tr.start()
tp.join()
tr.join()

print 'retp:', retp, 'retr:', retr
a = []
if retp:
    t = retp
    while t[0] != 2011:
        a.insert(0, t)
        t = sp[t]
if retr:
    t = retr
    while t[0] != 2012:
        a.append(t)
        t = sr[t]
end = time.time()

print a, len(a) + 1
print
print '('*(len(a) + 1) + '2011' + ''.join([s[i[1]] for i in a]) + '-5)'
print
print 'time:', end - begin
print 'done!'

