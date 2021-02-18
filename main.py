from myutil import *

path_origin = r"D:\规则发现数据集\新建文件夹\Software\FLOSSmole\新建文件夹"
path_target = r"D:\规则发现数据集\新建文件夹\Software\FLOSSmole"
# replace_character_batch(';', ',', 'csv', 'csv', path_origin, path_target)
with open(r"D:\规则发现数据集\新建文件夹\Complementary\covid-19-main\data\worldwide-aggregate.csv", 'r', encoding='utf-8') as f:
    head = f.readline().split(',')
    head = [col + ' string' for col in head]
    print(','.join(head))
    f.close()
# txt2csv(path_origin)
# process_empty_value_dblp(path)

# txt2csv(r"D:\测试数据集\TFACC\AMOT\test_result")
# batch_process_empty_value_AMOT(r"D:\测试数据集\TFACC\AMOT\test_result", r"D:\测试数据集\TFACC\AMOT\test_result\processed\\")
# batch_backslash_processing(r"D:\测试数据集\TFACC\AMOT\test_result\processed",
#                            r"D:\测试数据集\TFACC\AMOT\test_result\processed\final\\")
# process_empty_value_dblp(r"D:\测试数据集\TFACC\AMOT\test_result\processed\final\test_result_2017.csv")
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

# backslash_processing(r"C:\Users\huangzh\Desktop\新建文件夹 (3)\order.csv")

# split_file(path, 5000000)

# batch_process_empty_value_AMOT(path_AMOT, path_AMOT_target)
