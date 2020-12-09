import chardet

f = open(r"C:\Users\huangzh\Desktop\实体识别\20201116-机构.xlsx",'rb') #打开文件
data = f.readline()
a = chardet.detect(data)
print(a)
f.close()