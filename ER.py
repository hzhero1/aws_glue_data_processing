from pyhanlp import *
from strsimpy.cosine import Cosine
from strsimpy.sorensen_dice import SorensenDice
from myutil import er_process, er_process_with_similarity
import numpy as np

org = '安徽财经大学管理科学与工程学院'

Segment = JClass("com.hankcs.hanlp.seg.Segment")
Term = JClass("com.hankcs.hanlp.seg.common.Term")

segment = HanLP.newSegment().enableOrganizationRecognize(True)
seg = segment.seg(org)

path_o1 = r"C:\Users\huangzh\Desktop\实体识别\result_cn.csv"
path_o2 = r"C:\Users\huangzh\Desktop\实体识别\result_cn2.csv"
path_t = r"C:\Users\huangzh\Desktop\实体识别\\"

cosine = Cosine(2)
sorensenDice = SorensenDice(2)
s0 = '"西北农业大学,西北农林科技大学农学院"'
s1 = '"德国汉诺威大学"'
# print(cosine.similarity(s0, s1))
# print(sorensenDice.similarity(s0, s1))

er_process_with_similarity(path_o1, path_o2, path_t, 'result_cn_with_similarity', cosine, sorensenDice)
# er_process(path_o, path_t, 'result_cn', segment)

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
