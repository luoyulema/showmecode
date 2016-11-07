#_*_coding:utf-8_*_

import re
file = open('1.txt', 'r+').read().decode('utf8')
content = file.split()
check = raw_input('Please input your sentence:').decode('gbk')
for i in content:
    matches = re.compile(i)
    result = matches.match(check)
    if result:
        check = check.replace(i, '*')
    else:
        pass
print check
