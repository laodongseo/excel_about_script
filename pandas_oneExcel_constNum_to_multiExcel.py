# -*- coding: utf-8 -*-
"""
按固定行数分割1个大excel的第1个sheet文件为多个sheet
默认第一行为表头
"""
import pandas as pd
import math


def split_excel(excel_name,split_num):
    df = pd.read_excel(f'{excel_name}.xlsx')
    rows,cols = df.shape # 行数列数,默认第一列表头不算行数
    value = math.floor(rows/split_num) # 标准分割次数
    rows_format = value*split_num # 标准分割所占用总行数
    new_list = [[i,i+split_num] for i in range(0,rows_format,split_num)]

    # 标准行数文件
    for i_j in new_list:
        i,j = i_j
        excel_small = df[i:j]
        excel_small.to_excel(f'{excel_name}_{i}_{j}.xlsx',index=False)

    # 剩余的行分割出的文件
    df[rows_format:].to_excel(f'{excel_name}_last.xlsx',index=False)


if __name__ == '__main__':
    excel_name = 'school_info' # 不带后缀
    split_num = 200 # 多个行分割为1个excel
    split_excel(excel_name,split_num)
