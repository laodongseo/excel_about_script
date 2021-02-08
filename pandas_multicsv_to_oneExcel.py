# -*- coding: utf-8 -*-
"""
读取某个目录下多个csv文件合并为1个excel的1个sheet
csv第一列为表头,多个csv根据表头上下合并
"""
import os
import pandas as pd


# 获取某个目录下的特定文件(含路径,非递归),ext为文件后缀(带点)
def get_files(file_path,ext):
    file_list = []
    dir_or_files = os.listdir(file_path)
    # dir_or_file纯文件名+后缀,不带路径
    for dir_or_file in dir_or_files:
        # 给目录或者文件添加路径
        dir_file_path = os.path.join(file_path, dir_or_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            pass
        else:
            if os.path.splitext(dir_file_path)[-1] == ext:
                file_list.append(dir_file_path)
    return file_list


def make_excel(csv_files,encode_csv):
    df_concat = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv(file,encoding=encode_csv,header=0)
        # 循环每个df拼接成一个
        df_concat = pd.concat([df_concat,df],sort=False)
        # 写入新的excel
    df_concat.to_excel(f'{path}res_oneSheet.xlsx',index=False)


if __name__ == '__main__':
    path = './1/' # 结尾加斜线
    csv_files=get_files(path,'.csv')
    make_excel(csv_files,encode_csv='GBK')


