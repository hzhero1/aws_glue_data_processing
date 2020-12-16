import os, random, hashlib, glob, re
from strsimpy.cosine import Cosine


def er_process_with_similarity(path_original1, path_original2, path_target, keyword, similarity_list):
    file_origin1 = open(path_original1, 'r', encoding='utf-8')
    path_target = path_target + keyword + '.csv'
    file_target = open(path_target, 'w', encoding='utf-8')
    file_origin1.readline()
    file_target.writelines(
        "institution_1,NT & NZ,institution_2,NT & NZ,jaroWinkler,cosine,jaccard,normalizedLevenshtein\n")
    count1 = 0
    count2 = 0
    while True:
        file_origin2 = open(path_original2, 'r', encoding='utf-8')  # 打开源数据的备份，后面循环遍历
        file_origin2.readline()
        data1 = file_origin1.readline()
        if not data1:  # 读完关闭文件
            file_origin1.close()
            file_target.close()
            break
        data1 = data1.split('","')
        data1 = [data1[0], data1[2]]
        while True:
            data2 = file_origin2.readline()
            if not data2:
                file_origin2.close()
                break
            data2 = data2.split('","')
            line = data1.copy()
            line.append(data2[0][1:])
            line.append(data2[2])
            line = ['","'.join(line) + '"']
            for metric in similarity_list:
                line.append(str(metric.similarity(data1[1], data2[2])))
            line = ','.join(line) + '\n'
            file_target.writelines(line)  # 计算完当前行和所有行的相似度，写入行
            count2 += 1

        count1 += 1
        print('write {} entity'.format(count1))


def er_process(path_original, path_target, keyword, recognizer):
    file_origin = open(path_original, 'r', encoding='gbk')
    path_target = path_target + keyword + '.csv'
    file_target = open(path_target, 'w', encoding='utf-8')
    file_target.writelines("contrib_institution_display,NS,NT & NZ,NI,NR\n")
    count = 0
    while True:
        data = file_origin.readline()
        if not data:
            file_origin.close()
            file_target.close()
            break
        data = data.split(',')
        if data[1] == '中国':
            line = ['"' + data[0] + '"', [], [], [], []]
            result = recognizer.seg(data[0]).iterator()
            tmp_list = []
            for item in result:
                tmp_list.append(str(item))
            result = tmp_list
            for item in result:
                if '/ns' in item:
                    line[1].append(item.split('/ns')[0])
                elif '/nt' in item:
                    line[2].append(item.split('/nt')[0])
                elif '/nz' in item:
                    line[2].append(item.split('/nz')[0])
                elif '/ni' in item:
                    line[3].append(item.split('/ni')[0])
                elif '/nr' in item:
                    line[4].append(item.split('/nr')[0])
            for i in range(1, 5):
                if line[i]:
                    line[i].sort()
                    line[i] = '\"' + ','.join(line[i]) + '\"'
                else:
                    line[i] = '"null"'
            line = ','.join(line) + '\n'
            file_target.writelines(line)
            count += 1
            print('write {} lines.'.format(count))


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
    for name in glob.glob(path_directory + r"\*.txt"):
        tsv_file = open(name, 'r', encoding='utf-8')
        csv_file = open(os.path.splitext(name)[0] + ".csv", 'w', encoding='utf-8')
        while True:
            data = tsv_file.readline().replace('"', '""')
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


def batch_backslash_processing(path_directory, target_directory):
    file_count = 0
    for path in glob.glob(path_directory + r"\*.csv"):
        csv_origin = open(path, 'r', encoding='utf-8')
        csv_target = open(target_directory + os.path.split(path)[1], 'w', encoding='utf-8')
        while True:
            data = csv_origin.readline()
            if len(data) == 0:
                csv_origin.close()
                csv_target.close()
                break
            data = data.replace('\\', '')
            csv_target.writelines(data)


# 处理反斜杠
def backslash_processing(path):
    csv_origin = open(path, 'r', encoding='utf-8')
    csv_target = open(os.path.splitext(path)[0] + "_stripped.csv", 'w', encoding='utf-8')
    while True:
        data = csv_origin.readline()
        if len(data) == 0:
            csv_origin.close()
            csv_target.close()
            break
        data = data.replace('\\', '')
        csv_target.writelines(data)


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
