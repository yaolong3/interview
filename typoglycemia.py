# -*- coding: utf-8 -*-
"""

@author: yaolong3

Typoglycemia是个新词，描述的是人们识别一段文本时的一个有趣的现象：
只要每个单词的首尾字母正确，中间的字母顺序完全打乱也没有关系，
照样可以正常理解。例如这么一段文字：
http://weibo.com/1560442584/z3Q2QkGOT
"""

import os, sys, random, time
import ctypes

def MakeTypoglycemia(text):
    c_text = ctypes.c_buffer(text)
    i = 0
    bi = 0
    flag = False
    while i < len(c_text):
        if c_text[i].isalpha(): #97 <= ord(c_text[i]) <= 122 or 65 <= ord(c_text[i]) <= 90:
            if flag:
                if bi <= i - 3:
                    j =  random.randint(bi + 1, i - 1)
                    c_text[j], c_text[i-1] = c_text[i-1], c_text[j]
            else:
                flag = True
                bi = i
        else:
            flag = False
        i += 1
    return c_text.value

text = '''
I couldn't believe that I could actually understand what I was reading: 
the phenomenal power of the human mind. 
According to a research team at Cambridge University, 
it doesn't matter in what order the letters in a word are, 
the only important thing is that the first and last letter be in the right place. 
The rest can be a total mess and you can still read it without a problem. 
This is because the human mind does not read every letter by itself, 
but the word as a whole. Such a condition is appropriately called Typoglycemia.

Amazing, huh? Yeah and you always thought spelling was important.
'''

#print text
print MakeTypoglycemia(text)

