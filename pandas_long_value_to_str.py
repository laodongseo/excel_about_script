
# -*- coding:UTF-8 -*-
"""
批量处理某个文件夹下多个excel或者csv
把科学计数法的列(必须是整数否则有误差)变为字符串显示
支持传入多个列
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
    file_path,ext = './','.xlsx'
    files = get_files(file_path,ext)
    if ext == '.csv':
        csv_to_str(files,'communityid')
    else:
        excel_to_str(files,'communityid')
