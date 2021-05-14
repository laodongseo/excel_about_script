
# -*- coding:UTF-8 -*-
"""
批量处理某个文件夹下多个excel(每个sheet)或者csv
把科学计数法的列(必须是整数否则有误差)变为字符串显示
支持传入多个列
"""
import pandas as pd
import os

def func(element):
    if '/subway/' in element:
        return '地铁'
    return '非地铁'


def add_col(excel_file,sheet_name):
    with pd.ExcelWriter(f'{excel_file}_add_col.xlsx',sheet_name=sheet_name) as writer:
        df = pd.read_excel(excel_file)
        df['是否地铁'] = df['url'].apply(func)
        print(df)
        df.to_excel(writer, sheet_name=sheet_name, index=False)


if __name__ == "__main__":
    excel_file = './2021kwd_url_core_city_unique_one_sheet.xlsx'
    sheet_name = 'Sheet1'
    add_col(excel_file,sheet_name)
