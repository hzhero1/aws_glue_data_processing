import chardet

f = open(r"C:\Users\huangzh\Desktop\测试数据集\imdb\tsv2csv\name_basics.csv",'rb') #打开文件
data = f.readline()
a = chardet.detect(data)
print(a)
f.close()