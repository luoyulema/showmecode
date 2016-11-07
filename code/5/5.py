import re
import os
import sys


class Number(object):
    """docstring for Number"""

    def __init__(self, path):
        self.path = path
        print path

    def __open(self):
        path = self.path
        with open(path, 'r+') as f:
            f = f.read()
            f = re.findall(r'[\w\-\_\.]+', f)
            return f

    def number(self):
        f = self.__open()
        print len(f)

    def details(self):
        f = self.__open()
        detail = {}
        for i in f:
            if detail.has_key(i):
                detail[i] += 1
            else:
                detail[i] = 1
        print detail
