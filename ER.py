import hanlp

recognizer_cn = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
path_o = r"C:\Users\huangzh\Desktop\实体识别\20201116-机构.csv"
path_t = r"C:\Users\huangzh\Desktop\实体识别\\"


result1 = recognizer_cn(list('广西大学计算机与电子信息学院'))
print(result1)

# tokenizer = hanlp.load('LARGE_ALBERT_BASE')
# result2 = tokenizer('广西大学计算机与电子信息学院')
# print(result2)

# hanlp.pretrained.cws.LARGE_ALBERT_BASE


def er_process(path_original, path_target, keyword, recognizer):
    file_origin = open(path_original, 'r', encoding='gbk')
    path_target = path_target + keyword + '.csv'
    file_target = open(path_target, 'w', encoding='utf-8')
    file_target.writelines("contrib_institution_display,NR,NS,NT\n")
    count = 0
    while True:
        data = file_origin.readline()
        if not data:
            file_origin.close()
            file_target.close()
            break
        data = data.split(',')
        if data[1] == '中国':
            line = [data[0], [], [], []]
            result = recognizer(list(data[0]))
            for item in result:
                if item[1] == 'NR':
                    line[1].append(item[0])
                elif item[1] == 'NS':
                    line[2].append(item[0])
                elif item[1] == 'NT':
                    line[3].append(item[0])
            for i in range(1, 4):
                line[i] = '\"' + ','.join(line[i]) + '\"'
            line = ','.join(line) + '\n'
            file_target.writelines(line)
            count += 1
            print('write {} lines.'.format(count))


# er_process(path_o, path_t, 'result_cn', recognizer_cn)
