import json
from openpyxl import Workbook


def turntoxls(path):
    file = open(path, 'r+').read()
    filejson = json.loads(file, encoding='gb2312')
    wb = Workbook()
    ws = wb.active
    for row in filejson:
        ws.append(row)
    wb.save('number.xls')
