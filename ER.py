from pyhanlp import *


def er_process(path_original, path_target, keyword, recognizer):
    file_origin = open(path_original, 'r', encoding='gbk')
    path_target = path_target + keyword + '.csv'
    file_target = open(path_target, 'w', encoding='utf-8')
    file_target.writelines("contrib_institution_display,NS,NT,NI,NR\n")
    count = 0
    while True:
        data = file_origin.readline()
        if not data:
            file_origin.close()
            file_target.close()
            break
        data = data.split(',')
        if data[1] == '中国':
            line = [data[0], [], [], [], []]
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
                elif '/ni' in item:
                    line[3].append(item.split('/ni')[0])
                elif '/nr' in item:
                    line[4].append(item.split('/nr')[0])
            for i in range(1, 5):
                line[i].sort()
                line[i] = '\"' + ','.join(line[i]) + '\"'
            line = ','.join(line) + '\n'
            file_target.writelines(line)
            count += 1
            print('write {} lines.'.format(count))


org = '安徽财经大学管理科学与工程学院'

Segment = JClass("com.hankcs.hanlp.seg.Segment")
Term = JClass("com.hankcs.hanlp.seg.common.Term")

segment = HanLP.newSegment().enableOrganizationRecognize(True)
seg = segment.seg(org)

path_o = r"C:\Users\huangzh\Desktop\实体识别\20201116-机构.csv"
path_t = r"C:\Users\huangzh\Desktop\实体识别\\"

er_process(path_o, path_t, 'result_cn', segment)

# seg = seg.iterator()
# tmp_list = []
# for i in seg:
#     tmp_list.append(str(i))
#
# print(tmp_list)
#
# line = [[], [], []]
# for item in tmp_list:
#     if '/nt' in item:
#         line[0].append(item.split('/nt')[0])
#     elif '/ns' in item:
#         line[1].append(item.split('/ns')[0])
#     else:
#         line[2].append(item.split('/')[0])
# print(line)


# def er_process(path_original, path_target, keyword, recognizer):
#     file_origin = open(path_original, 'r', encoding='gbk')
#     path_target = path_target + keyword + '.csv'
#     file_target = open(path_target, 'w', encoding='utf-8')
#     file_target.writelines("contrib_institution_display,NR,NS,NT\n")
#     count = 0
#     while True:
#         data = file_origin.readline()
#         if not data:
#             file_origin.close()
#             file_target.close()
#             break
#         data = data.split(',')
#         if data[1] == '中国':
#             line = [data[0], [], [], []]
#             result = recognizer(list(data[0]))
#             for item in result:
#                 if item[1] == 'NR':
#                     line[1].append(item[0])
#                 elif item[1] == 'NS':
#                     line[2].append(item[0])
#                 elif item[1] == 'NT':
#                     line[3].append(item[0])
#             for i in range(1, 4):
#                 line[i] = '\"' + ','.join(line[i]) + '\"'
#             line = ','.join(line) + '\n'
#             file_target.writelines(line)
#             count += 1
#             print('write {} lines.'.format(count))

# er_process(path_o, path_t, 'result_cn', recognizer_cn)
