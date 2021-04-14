#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
#GET方法
import requests
from bs4 import BeautifulSoup
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'}
url = 'http://data.eastmoney.com/cjsj/gdzctz.html'
strhtml = requests.get(url)
print(strhtml.text)
'''


import requests
import re
from bs4 import BeautifulSoup

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'}
url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?cb=datatable4409505&type=GJZB&sty=ZGZB&js=(%7Bdata%3A%5B(x)%5D%2Cpages%3A(pc)%7D)&p=1&ps=20&mkt=12&pageNo=1&pageNum=1&_=1618413759830'
strhtml = requests.get(url, head)
strhtml.encoding = 'utf-8'
#soup = BeautifulSoup(strhtml.content, "html.parser")
#table = soup.find('body')
print(strhtml)



'''
#歪路
datalist = []
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', 'table-model')
for tb in table:
    tr = tb.find_all('tr')
    for j in tr[1:]:
        td = j.find_all('td')
        Date = td[0].get_text().strip()
        Investment = td[1].get_text().strip()
        Growth1 = td[2].get_text().strip()
        Growth2 = td[3].get_text().strip()
        Accumulation = td[4].get_text().strip()
        datalist.append([Date, Investment, Growth1, Growth2, Accumulation])
#print(datalist)
'''



