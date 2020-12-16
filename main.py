from myutil import *

num_extract_10w = 100000
num_extract_1w = 10000
path_name_baiscs = r"D:\测试数据集\imdb\imdb_csv\processed\name_basics_new.csv"
path_title_basics = r"D:\测试数据集\imdb\imdb_csv\title_basics_new.csv"
path_title_akas = r"D:\测试数据集\imdb\imdb_csv\processed\title_akas_new.csv"
path_title_principles = r"D:\测试数据集\imdb\imdb_csv\title_principals_new.csv"

path_paper = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\processed\paper_new.csv"
path_paper_author = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\processed\paper_authors_new.csv"
path_paper_venue = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\processed\paper_venue_new.csv"
path_paper_fos = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\paper_fos.csv"

path_AMOT = r"D:\测试数据集\TFACC\AMOT\AMOT_csv"
path_AMOT_target = r"D:\测试数据集\TFACC\AMOT\AMOT_csv\empty_processed\\"

path = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\paper_venue.csv"

# process_empty_value_dblp(path)

# txt2csv(r"D:\测试数据集\TFACC\AMOT\test_result")
# batch_process_empty_value_AMOT(r"D:\测试数据集\TFACC\AMOT\test_result", r"D:\测试数据集\TFACC\AMOT\test_result\processed\\")
# batch_backslash_processing(r"D:\测试数据集\TFACC\AMOT\test_result\processed",
#                            r"D:\测试数据集\TFACC\AMOT\test_result\processed\final\\")
process_empty_value_dblp(r"D:\测试数据集\TFACC\AMOT\test_result\processed\final\test_result_2017.csv")
## extract imdb
# random_extract(path_title_basics, num_extract_1w, 200, 720, "_sub_1w")
# random_extract(path_title_basics, num_extract_10w, 20, 72, "_sub_10w")
# random_extract(path_name_baiscs, num_extract_1w, 200, 1000, "_sub_1w")
# random_extract(path_name_baiscs, num_extract_10w, 20, 100, "_sub_10w")
# random_extract(path_title_akas, num_extract_1w, 200, 2300, "_sub_1w")
# random_extract(path_title_akas, num_extract_10w, 20, 230, "_sub_10w")
# random_extract(path_title_principles, num_extract_1w, 200, 4000, "_sub_1w")
# random_extract(path_title_principles, num_extract_10w, 20, 400, "_sub_10w")

# extract dblp
# random_extract(path_paper, num_extract_1w, 200, 490, "_sub_1w")
# random_extract(path_paper, num_extract_10w, 20, 49, "_sub_10w")
# random_extract(path_paper_author, num_extract_1w, 200, 1500, "_sub_1w")
# random_extract(path_paper_author, num_extract_10w, 20, 150, "_sub_10w")
# random_extract(path_paper_venue, num_extract_1w, 200, 480, "_sub_1w")
# random_extract(path_paper_venue, num_extract_10w, 20, 48, "_sub_10w")
# random_extract(path_paper_fos, num_extract_1w, 200, 4500, "_sub_1w")
# random_extract(path_paper_fos, num_extract_10w, 20, 450, "_sub_10w")

# split_file(path, 5000000)

# batch_process_empty_value_AMOT(path_AMOT, path_AMOT_target)

# count = 0
# with open(r"D:\测试数据集\dblp\dblp_csv\dblp_converted\processed\paper_authors_new.csv", 'r', encoding='utf-8') as f:
#     while True:
#         count += 1
#         data = f.readline()
#         if not data:
#             break
#         if '\x00' in data:
#             print('line {}: {}'.format(count, data))
#             # print(data.replace('\x00', ' '))
