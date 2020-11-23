
# -*- coding:UTF-8 -*-
"""
批量处理多个excel或者csv
把科学计数法的列(必须是整数)变为字符串显示
"""
import pandas as pd
import os


def excel_to_str(excel_files, *cols):
    for excel_file in excel_files:
        excel_file_name, ext = os.path.splitext(excel_file)
        with pd.ExcelWriter('{0}_new.xlsx'.format(excel_file_name)) as writer:
            df_dict = pd.read_excel(excel_file, sheet_name=None)
            sheets = df_dict.keys()
            for sheet in sheets:
                df = df_dict[sheet]
                for col in cols:
                    df[col] = df[col].astype('int64').astype('str')
                df.to_excel(writer, sheet_name=sheet, index=False)


def csv_to_str(csv_files, *cols, encode_now='GB18030'):
    for csv_file in csv_files:
        csv_file_name, ext = os.path.splitext(csv_file)
        with pd.ExcelWriter('{0}_new.xlsx'.format(csv_file_name)) as writer:
            df = pd.read_csv(csv_file, encoding=encode_now)
            for col in cols:
                df[col] = df[col].astype('int64').astype('str')
            df.to_excel(writer, index=False)


if __name__ == "__main__":
    # excel文件
    excel_files = ['./小区_sale.csv_分城市.xlsx', './小区_rent.csv_分城市.xlsx']
    # csv文件
    csvs = ['小区_sale.csv', '小区_rent.csv']
    # 对应的函数
    excel_to_str(excel_files, 'communityid')
