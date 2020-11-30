from myutil import process_empty_value

path_name_baiscs = r"D:\测试数据集\imdb\新建文件夹\name_basics.csv"
path_title_basics = r"D:\测试数据集\imdb\新建文件夹 (2)\title_basics.csv"
path_title_akas = r"D:\测试数据集\imdb\新建文件夹 (2)\title_akas.csv"
path_title_principles = r"D:\测试数据集\imdb\新建文件夹\title_principals.csv"


# process_empty_value(path_title_basics)
process_empty_value(path_name_baiscs)
process_empty_value(path_title_akas)
# process_empty_value(path_title_principles)

# s = 1
# hl = hashlib.md5()
# hl.update(str(s).encode(encoding='utf-8'))
# print(hl.hexdigest())
