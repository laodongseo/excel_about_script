# -*- coding: utf-8 -*-
"""
读取某个目录下多个csv文件合并为1个excel1个sheet
"""
import os
import pandas as pd


def file_names(file_dir):
    csv_files=[]
    for file in os.listdir(file_dir):
        if os.path.splitext(file)[1] == '.csv':
            csv_files.append(file)
    return csv_files


def make_excel(csv_files,encode_csv):
    df_concat = pd.DataFrame()
    for file in csv_files:
        csv_file =  path + file
        df = pd.read_csv(csv_file,encoding=encode_csv,header=0)
        # 循环每个df拼接成一个
        df_concat = pd.concat([df_concat,df],sort=False)
        # 写入新的excel
    df_concat.to_excel('res_oneSheet.xlsx',index=False)

if __name__ == '__main__':
    path = './1/' # 结尾加斜线
    csv_files=file_names(path)
    make_excel(csv_files,encode_csv='GBK')


