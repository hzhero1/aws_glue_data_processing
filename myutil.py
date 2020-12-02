import os, random, hashlib, glob, re


def tsv2csv(path_directory):
    count = 0
    for name in glob.glob(path_directory + r"\*.tsv"):
        tsv_file = open(name, 'r', encoding='utf-8')
        csv_file = open(os.path.splitext(name)[0] + ".csv", 'w', encoding='utf-8')
        while True:
            data = tsv_file.readline().replace('"', '""')
            if data:
                data = '"' + '","'.join(re.split(r'[\t\n]', data.strip('\n'))) + '"\n'
                csv_file.writelines(data)
            else:
                break
        tsv_file.close()
        csv_file.close()
        count += 1
        print("Convert {} .tsv file to .csv file".format(count))


def txt2csv(path_directory):
    count = 0
    for name in glob.glob(path_directory + r"\*.csv"):
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


def empty_column_processing(path_directory):
    count = 0
    for name in glob.glob(path_directory + r"\*.csv"):
        tsv_file = open(name, 'r', encoding='utf-8')
        csv_file = open(os.path.splitext(name)[0] + "row500_test.csv", 'w', encoding='utf-8')
        # for i in range(500):
        while True:
            data = tsv_file.readline()
            if len(data) == 0:
                break
            if data != '""\n':
                csv_file.writelines(data)
            else:
                continue
        tsv_file.close()
        csv_file.close()
        count += 1
        print("Convert {} .tsv file to .csv file".format(count))


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
            csv_origin.close()
            csv_target.close()
            print("Task finished.")
            break


# 空值处理
def process_empty_value_imdb(path):
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
            csv_target.writelines(data)
            row_count += 1
            print('Processed {} rows.'.format(row_count))
        else:
            csv_origin.close()
            csv_target.close()
            break


def process_empty_value_dblp(path):
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
                if len(value) == 0 or value == '""':
                    hl.update(str(md5_count).encode(encoding='utf-8'))
                    md5_count += 1
                    data[i] = hl.hexdigest()
                elif value == '\n':
                    hl.update(str(md5_count).encode(encoding='utf-8'))
                    md5_count += 1
                    data[i] = hl.hexdigest() + '\n'
            data = ','.join(data)
            csv_target.writelines(data)
            row_count += 1
            print('Processed {} rows.'.format(row_count))
        else:
            csv_origin.close()
            csv_target.close()
            break


def batch_process_empty_value_AMOT(path_directory, target_directory):
    file_count = 0
    for path in glob.glob(path_directory + r"\*.csv"):
        csv_origin = open(path, 'r', encoding='utf-8')
        csv_target = open(target_directory + os.path.split(path)[1], 'w', encoding='utf-8')
        md5_count = 0
        # row_count = 0
        hl = hashlib.md5()
        while True:
            data = csv_origin.readline()
            if data:
                data = data.split(',')
                for i, value in enumerate(data):
                    if len(value) == 0 or value == '""':
                        hl.update(str(md5_count).encode(encoding='utf-8'))
                        md5_count += 1
                        data[i] = hl.hexdigest()
                    elif value == '\n' or value == '""\n':
                        hl.update(str(md5_count).encode(encoding='utf-8'))
                        md5_count += 1
                        data[i] = hl.hexdigest() + '\n'
                data = ','.join(data)
                csv_target.writelines(data)
                # row_count += 1
                # print('Processed {} rows.'.format(row_count))
            else:
                csv_origin.close()
                csv_target.close()
                break
        file_count += 1
        print('Processed {} files.'.format(file_count))


# 处理反斜杠
def backslash_processing(path):
    csv_origin = open(path, 'r', encoding='utf-8')
    csv_target = open(os.path.splitext(path)[0] + "_stripped.csv", 'w', encoding='utf-8')
    while True:
        data = csv_origin.readline()
        if len(data) == 0:
            break
        data = data.replace('\\', '')
        csv_target.writelines(data)

    csv_origin.close()
    csv_target.close()


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
