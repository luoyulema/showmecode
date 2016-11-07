import os
import glob
import re
textDir = r'c:\\showmecode\\code\\7'
filepath = glob.glob(os.path.join(textDir, '*.txt'))

for i in filepath:
	with open(i) as text:
		text = text.read()
		words = re.findall(r'[\w\-\_\.]+', text)
		dic = {}
		for word in words:
			if dic.has_key(word):
				dic[word] += 1
			else:
				dic[word] = 1
		print sorted(dic.iteritems(),key=lambda d:d[1],reverse=True)

