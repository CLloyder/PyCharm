import requests #导入界面抓取库
import numpy as np #导入数组控制库
import xlwt #导入excel库

url ='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?cb=datatable2065887&type=GJZB&sty=ZGZB&js=(%7Bdata%3A%5B(x)%5D%2Cpages%3A(pc)%7D)&p=1&ps=20&mkt=12&pageNo=1&pageNum=1&_=1618420607118'
html = requests.get(url) #抓取网页源代码
tex= html.text #转换为文本

texs= tex.split('"') #将文本切割
x=len(texs) #测量texs长度
i=0
j=0
texss=[]
savepath='中国城镇固定资产投资.xls'  #定义必要变量
for i in range(1,x,2):
    texss = texss + texs[i].split(',')  #将所需结果切割并储存于一维列表
texss=np.array(texss)   #将列表转为一维数组
texss.resize((int)(len(texss) / 5), 5)  #将一维数组转为固定列为5的二维数组
datalist = texss    #赋值

def saveData(datalist, savepath):   #定义储存数据函数
    print("save.......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('中国 城镇固定资产投资', cell_overwrite_ok=True)  #创建工作表
    col = ("月份","当月（亿元）","同比增长","环比增长","自年初累计（亿元）")
    for i in range(0,5):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,len(datalist)):
        data = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])  #数据
    book.save(savepath) #保存

saveData(datalist,savepath) #储存在当前目录

