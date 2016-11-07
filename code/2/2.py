import random
import os
import sys
#随机生成验证码s

def yanzhenma(number, length=8):
    str = "abcdefghijklmnopqastuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number <= 0:
        print "Plaease input valid number"
    else:
        infile = open('2.txt', 'w')
        for i in range(1, number + 1):
            index = random.sample(str, length)
            nstr = ''.join(index)
            infile.write(nstr + '\n')

