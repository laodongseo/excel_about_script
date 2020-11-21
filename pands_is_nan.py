# -*- coding:UTF-8 -*-
"""
批量检查excel或者csv是否有空值并输出含空值的列
"""
import pandas as pd
from urllib.parse import unquote


def excel_isnan(excels):
    for excel in excels:
        df_dict = pd.read_excel(excel,sheet_name=None)
        for sheet,df_sheet in df_dict.items():
            cols = df_sheet.columns
            for col in cols:
                my_series = df_sheet[col]
                if len(my_series) != my_series.count():
                    print(excel,'存在空值:',sheet,col)


def csv_isnan(csvs,encode_now='GB18030'):
    for csv in csvs:
        df_sheet = pd.read_csv(csv,encoding=encode_now)
        cols = df_sheet.columns
        for col in cols:
            my_series = df_sheet[col]
            if len(my_series) != my_series.count():
                print(csv,'存在空值:',col)

if __name__ == "__main__":
    # excel文件
    excels = ['小区_rent.csv_分城市.xlsx']
    # csv文件
    csvs = ['小区_sale.csv','小区_rent.csv']
    csv_isnan(csvs,'GBK')
