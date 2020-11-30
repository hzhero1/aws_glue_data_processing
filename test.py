import os, re, csv, hashlib, time, datetime

#记录规则执行开始时间
start = time.perf_counter()
with open(r"D:\测试数据集\imdb\imdb_csv\title_basics.csv", 'r', encoding='utf-8') as f:
    for i in range(100):
        # data = re.split(r'[\t]', f.readline())
        # data = '"' + '","'.join(re.split(r'[\t\n]', f.readline().strip('\n'))) + '"\n'
        # data = [f.readline()[-1]]
        data = f.readline().split(',')
        # print(data)
    f.close()
end = time.perf_counter()

print("规则执行时间：{}s".format(end-start))

