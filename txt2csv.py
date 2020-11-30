import glob, os, re

path = r"D:\测试数据集\TFACC\AMOT\AMOT_csv\tmp_origin"

count = 0
for name in glob.glob(path + r"\*.csv"):
    tsv_file = open(name, 'r', encoding='utf-8')
    csv_file = open(os.path.splitext(name)[0] + "_t.csv", 'w', encoding='utf-8')
    while True:
        data = tsv_file.readline()
        if data:
            data = '"' + '","'.join(re.split(r'[|\n]', data.strip('\n'))) + '"\n'
            csv_file.writelines(data)
        else:
            break
    tsv_file.close()
    csv_file.close()
    count += 1
    print("Convert {} .tsv file to .csv file".format(count))
