import glob, os, re

path = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\paper.csv"
path_temp = r"D:\测试数据集\dblp\dblp_csv\dblp_converted\paper.csv"
# count = 0
# for name in glob.glob(path + r"\*.csv"):
#     tsv_file = open(name, 'r', encoding='utf-8')
#     csv_file = open(os.path.splitext(name)[0] + "row500_test.csv", 'w', encoding='utf-8')
#     for i in range(500):
#         data = tsv_file.readline()
#         if len(data) == 0:
#             break
#         if data != '""\n':
#             # data = '"' + '","'.join(re.split(r'[\t\n]', data.strip('\n'))) + '"\n'
#
#             csv_file.writelines(data)
#         else:
#             continue
#
#     tsv_file.close()
#     csv_file.close()
#     count += 1
#     print("Convert {} .tsv file to .csv file".format(count))


csv_origin = open(path_temp, 'r', encoding='utf-8')
csv_target = open(os.path.splitext(path_temp)[0] + "_stripped.csv", 'w', encoding='utf-8')
while True:
    data = csv_origin.readline()
    # print(data)
    if len(data) == 0:
        break
    data = data.replace('\\', '')
    csv_target.writelines(data)

csv_origin.close()
csv_target.close()
