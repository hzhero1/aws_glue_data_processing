import os, re, csv, hashlib, time, datetime

#记录规则执行开始时间
start = time.perf_counter()
with open(r"C:\Users\huangzh\Desktop\实体识别\20201116-机构.csv", 'r', encoding='utf-8') as f:
    for i in range(10):
        # data = re.split(r'[\t]', f.readline())
        # data = '"' + '","'.join(re.split(r'[\t\n]', f.readline().strip('\n'))) + '"\n'
        # data = [f.readline()[-1]]
        # data = f.readline().split(',')
        data = f.readline()
        # for i, value in enumerate(data):
        #     if value == '""':
        #         print(len(value))
        print(data)
    f.close()

# print('\n')


