# -*- coding:UTF-8 -*-
"""
批量检查某个文件夹里excel或者csv是否有空值并输出含空值的列

"""
import pandas as pd
import os

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
    file_path,ext = './','.xlsx'
    files = get_files(file_path,ext)
    if ext == '.csv':
        csv_isnan(files)
    else:
        excel_isnan(files)
