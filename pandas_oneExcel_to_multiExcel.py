# -*- coding: utf-8 -*-
import pandas as pd

"""
pandas指定一列来拆分excel为多个excel
默认读取为第1个sheet
"""


def split_file(excel_file,col_name):
    df = pd.read_excel(f'{excel_file}.xlsx')
    col_uniques = df[col_name].drop_duplicates().to_list()
    for col in col_uniques:
        res = df[col_name] == col # 布尔判断
        df[res].to_excel(f'{excel_name}{col}.xlsx',index=False)


if __name__ == '__main__':
    excel_name = './pc_core_0608' # 无后缀
    col_name = '城市'
    split_file(excel_name,col_name)
