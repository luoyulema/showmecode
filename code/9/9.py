from urllib import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(urlopen('http://tieba.baidu.com/p/2166231880'))
for string in soup.stripped_strings:
    print string
