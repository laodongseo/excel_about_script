# -*- coding: utf-8 -*-
"""
pandas指定一列来拆分excel的sheet为多个sheet
默认读取为第1个sheet,默认第一行为表头
"""
import pandas as pd


def split_sheet(excel_file,col_name):
    # 读取excel
    df = pd.read_excel(f'{excel_name}.xlsx')
    col_uniques = df[col_name].drop_duplicates().to_list()
    # 配置url写入excel不是链接
    with pd.ExcelWriter(f'{excel_name}_{col_name}_multi_sheet.xlsx',engine_kwargs={"options":{'strings_to_urls': False}}) as excel_writer:
        # 循环每一类写入
        for col in col_uniques:
            bool_df = df[col_name] == col
            my_df = df[bool_df]
            # my_df2 = my_df.drop_duplicates(subset=['名称','城市'])
            my_df.to_excel(excel_writer,sheet_name=col,index=False)

if __name__ == '__main__':
    excel_name = './2021kwd_url_core_city_unique_one_sheet' # 无后缀
    col_name = 'city'
    split_sheet(excel_name,col_name)
