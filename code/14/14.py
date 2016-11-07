from bs4 import BeautifulSoup
import urllib
import urllib2
from urlparse import urlsplit
import os


def openUrl(path):
    url = path
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    img = soup.find_all('img', {'class': 'BDE_Image'})
    for i in img:
        download(i['src'])

    print "downloaded"


def download(src):
    if not os.path.exists('file'):
        os.mkdir('file')
    file = urllib.urlopen(src).read()
    filename = os.path.basename(urlsplit(src)[2])
    imgs = open(os.path.join('file',filename), 'wb')
    imgs.write(file)
    imgs.close()
