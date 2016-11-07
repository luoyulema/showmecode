
"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</citys>
</root>
"""
from bs4 import BeautifulSoup
from bs4 import Comment
import xlrd
import json
import os


def readxls(path):
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_name('Sheet')
    ncols = ws.ncols
    nrows = ws.nrows
    dic = {}
    for i in range(0, nrows):
        for k in range(0, ncols):
            dic[str(ws.row_values(i)[0])] = ws.row_values(i)[1:]
    xml = json.dumps(dic, encoding='utf-8')
    print 'sucessfully'
    return xml


def writexml(xml):
    file = open('student.xml', 'w')
    xml = BeautifulSoup(open('student.xml'), 'xml', from_encoding='utf-8')
    root = xml.new_tag('root')
    xml.append(root)
    roots = xml.root
    student = xml.new_tag('students')
    roots.append(student)
    students = roots.students
    comment = xml.new_string(
        '\n学生信息表\n"id":[名字,数学,语文,英文]\n', Comment)
    student.append(comment)
    student.append(xml)
    i = xml.prettify()
    file.write(i)
    file.close()
