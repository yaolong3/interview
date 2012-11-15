# -*- coding: utf-8 -*-
"""

@author: yaolong3

#面试题# 从一个长字符串中查找包含给定字符集合的最短子串。
例如，长串为“aaaaaaaaaacbebbbbbdddddddcccccc”，
字符集为{abcd}，那么最短子串是“acbebbbbbd”。
如果将条件改为“包含且只包含给定字符集合”，你的算法和实现又将如何改动。

"""

import os, sys
import random, time

#查找包含给定字符集合的最短子串
def findSubString(s, cs):
    charset = [0] * 256
    for i in cs:
        charset[ord(i)] = 1
    # cntc存储每个字符集里的字符在[l, r]范围里出现的次数
    cntc = [0] * 256
    # m 表示已找到的在字符集里的字符个数
    m = 0
    l, r = 0, 0
    retl, retr = 0, len(s) - 1
    flag = False
    while r < len(s):
        c = ord(s[r])
        if charset[c]:
            if cntc[c] == 0:
                m += 1
            cntc[c] += 1
            if m == len(cs):
                flag = True
                while l < r:
                    if charset[ord(s[l])] == 0:
                        l += 1
                    elif cntc[ord(s[l])] > 1:
                        cntc[ord(s[l])] -= 1
                        l += 1
                    elif cntc[ord(s[l])] == 1:
                        break
                if r - l < retr - retl:
                    retl, retr = l, r
        r += 1
    if flag:
        return s[retl : retr + 1]
    return ''

#包含且只包含给定字符集合
def findSubStringContainsOnly(s, cs):
    charset = [0] * 256
    for i in cs:
        charset[ord(i)] = 1
    cntc = [0] * 256
    m = 0
    l, r = 0, 0
    retl, retr = 0, len(s)
    flag = False
    while r < len(s):
        c = ord(s[r])
        if charset[c]:
            if cntc[c] == 0:
                m += 1
            cntc[c] += 1
            if m == len(cs):
                flag = True
                while l < r:
                    if charset[ord(s[l])] == 0:
                        l += 1
                    elif cntc[ord(s[l])] > 1:
                        cntc[ord(s[l])] -= 1
                        l += 1
                    elif cntc[ord(s[l])] == 1:
                        break
                if r - l < retr - retl:
                    retl, retr = l, r
        #begin 加了这些
        else:
            #恢复cntc数组到初始状态
            if r - l < len(cs):
                while l < r:
                    cntc[ord(s[l])] = 0
                    l += 1
            else:
                for i in cs:
                    cntc[ord(i)] = 0
            while charset[ord(s[r])] == 0:
                r += 1
            m = 0
            l = r
            continue
        #end
        r += 1
    if flag:
        return s[retl : retr + 1]
    return ''
    
print findSubString('aaaaaaaaaacbebbbbbdddddddcccccc', 'abcd')
print findSubString('aaaaaaaaaacbebbbbbdddddddccccccdaadb', 'abcd')            

print findSubStringContainsOnly('aaaaaaaaaacbebbbbbdddddddcccccca', 'abcd')
print findSubStringContainsOnly('aaaaaaaaaacbebbbbbdddddddccccccdaadb', 'abcd')   
print findSubStringContainsOnly('aibicididfdddsaaaddccaabbib', 'abcd') 