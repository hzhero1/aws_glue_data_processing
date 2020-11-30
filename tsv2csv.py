import glob, os, re, random
from myutil import  random_extract

# path = r"D:\测试数据集\imdb\imdb_csv\新建文件夹"
num_extract_10w = 100000
num_extract_1w = 10000
path_name_baiscs = r"D:\测试数据集\imdb\imdb_csv\processed\name_basics_new.csv"
path_title_basics = r"D:\测试数据集\imdb\imdb_csv\title_basics_new.csv"
path_title_akas = r"D:\测试数据集\imdb\imdb_csv\processed\title_akas_new.csv"
path_title_principles = r"D:\测试数据集\imdb\imdb_csv\title_principals_new.csv"
path = r"D:\测试数据集\imdb\新建文件夹 (2)"


random_extract(path_title_basics, num_extract_1w, 200, 720, "_sub_1w")
# random_extract(path_title_basics, num_extract_10w, 20, 72, "_sub_10w")
# random_extract(path_name_baiscs, num_extract_1w, 200, 1000, "_sub_1w")
# random_extract(path_name_baiscs, num_extract_10w, 20, 100, "_sub_10w")
# random_extract(path_title_akas, num_extract_1w, 200, 2300, "_sub_1w")
# random_extract(path_title_akas, num_extract_10w, 20, 230, "_sub_10w")
# random_extract(path_title_principles, num_extract_1w, 200, 4000, "_sub_1w")
# random_extract(path_title_principles, num_extract_10w, 20, 400, "_sub_10w")

# count = 0
# for name in glob.glob(path + r"\*.tsv"):7
#     tsv_file = open(name, 'r', encoding='utf-8')
#     csv_file = open(os.path.splitext(name)[0] + ".csv", 'w', encoding='utf-8')
#     while True:
#         data = tsv_file.readline().replace('"', '""')
#         if data:
#             data = '"' + '","'.join(re.split(r'[\t\n]', data.strip('\n'))) + '"\n'
#             csv_file.writelines(data)
#         else:
#             break
#     tsv_file.close()
#     csv_file.close()
#     count += 1
#     print("Convert {} .tsv file to .csv file".format(count))
