import os, random, hashlib


# 随机抽取数据
def random_extract(path_csv, num_extract, range_lower, range_upper, suffix):
    csv_origin = open(path_csv, 'r', encoding='utf-8')
    csv_target = open(os.path.splitext(path_csv)[0] + suffix + ".csv", 'w', encoding='utf-8')
    count_row = 0
    row = csv_origin.readline()
    csv_target.writelines(row)
    while True:
        num_skip_row = random.randint(range_lower, range_upper)
        for i in range(num_skip_row):
            row = csv_origin.readline()
        csv_target.writelines(row)
        count_row += 1
        if count_row >= num_extract:
            break


# 控制处理
def process_empty_value(path):
    csv_origin = open(path, 'r', encoding='utf-8')
    csv_target = open(os.path.splitext(path)[0] + "_new.csv", 'w', encoding='utf-8')
    md5_count = 0
    row_count = 0
    hl = hashlib.md5()

    while True:
        data = csv_origin.readline()
        if data:
            data = data.split(',')
            for i, value in enumerate(data):
                if r'\N' in value:
                    hl.update(str(md5_count).encode(encoding='utf-8'))
                    md5_count += 1
                    data[i] = data[i].replace(r'\N', hl.hexdigest())
            data = ','.join(data)
            # data = '"' + '","'.join(re.split(r'[|\n]', data.strip('\n'))) + '"\n'
            csv_target.writelines(data)
            row_count += 1
            print('Processed {} rows.'.format(row_count))
        else:
            break


# 文件分段
def split_file(path, split_num):
    csv_origin = open(path, 'r', encoding='utf-8')
    fragment = 1
    while True:
        csv_target = open(os.path.splitext(path)[0] + "_" + str(fragment) + ".csv", 'w', encoding='utf-8')
        for i in range(split_num):
            data = csv_origin.readline()
            csv_target.writelines(data)
            if len(data) == 0:
                print("Split fragment{}.".format(fragment))
                csv_origin.close()
                csv_target.close()
                return 0
        print("Split fragment{}.".format(fragment))
        csv_target.close()
        fragment += 1
