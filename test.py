import os, re, csv, hashlib, time, datetime, codecs

# 记录规则执行开始时间
start = time.perf_counter()
count = 0
file = open(r"D:\测试数据集\TFACC\AMOT\test_result\processed\test_result_2017.csv", 'w', encoding='utf-8')
with open(r"D:\测试数据集\TFACC\AMOT\AMOT_csv\test_result_2017.csv", 'r', encoding='utf-8') as f:
    while True:
        # data = re.split(r'[\t]', f.readline())
        # data = '"' + '","'.join(re.split(r'[\t\n]', f.readline().strip('\n'))) + '"\n'
        # data = [f.readline()[-1]]
        # data = f.readline().split(',')

        data = f.readline()
        if not data:
            f.close()
            file.close()
            break
        if data.count(',') > 13:
            print(data)
            count += 1
        else:
            file.writelines(data)

    print(count)

# print('\n')
