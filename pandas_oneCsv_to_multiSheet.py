# ‐*‐coding:utf‐8‐*‐
"""
读取某个目录下所有csv文件
每个csv文件的sheet按照某指定的1列拆分的多个sheet保存成excel
csv默认编码为GB18030,默认第一行为表头
"""
import os
import pandas as pd


def get_file_path(root_path, ext):
    file_list = []
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 添加目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        suffix = os.path.splitext(dir_file_path)[1]
        file_list.append(dir_file_path) if ext in suffix else file_list
    return file_list


def split_sheet(file_csvs):
    for file in file_csvs:
        with pd.ExcelWriter(f'{file}_{col_name}.xlsx') as writer:
            df = pd.read_csv(file, sep=',', encoding='GB18030', header=0)
            citys = df[col_name].drop_duplicates().values
            for city in citys:
                bool_res = df[col_name] == city
                df_sheet = df[bool_res]
                df_sheet.to_excel(writer, sheet_name=str(city), index=False)


if __name__ == "__main__":
    root_path = r"./1/"
    file_csvs = get_file_path(root_path, '.csv')
    col_name = 'cityid' # 要拆分的列
    split_sheet(file_csvs)
