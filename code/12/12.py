# _*_ coding:utf-8_*_

f = open('1.txt', 'r+').read().decode('utf8')
content = f.split()
word = raw_input('>').decode('gbk')
if word in content:
    print 'Freedom'
else:
    print 'HumanRights'
