import os, re, csv, hashlib, time, datetime, codecs

# 记录规则执行开始时间
start = time.perf_counter()
count = 0
with open(r"C:\Users\huangzh\Desktop\实体识别\20201116-机构.csv", 'r', encoding='gbk') as f:
    while True:
        # data = re.split(r'[\t]', f.readline())
        # data = '"' + '","'.join(re.split(r'[\t\n]', f.readline().strip('\n'))) + '"\n'
        # data = [f.readline()[-1]]
        # data = f.readline().split(',')
        data = f.readline()
        if not data:
            break
        data = data.split(',')
        # for i, value in enumerate(data):
        #     if value == '""':
        #         print(len(value))
        print(data)
        count += 1
    f.close()
    print('Total lines: {}'.format(count))

# print('\n')
