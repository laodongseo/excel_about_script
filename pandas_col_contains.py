import pandas as pd
import os
import sys
"""
读取目录下的excel文件,每个文件做筛选
文本筛选,筛选某1列是否包含某些字符及不包含某些字符
筛选条件支持正则,每个excel可有多个sheet,各sheet被筛选的列名要一致
"""


# 获取某目录下的特定文件(含路径),ext为文件后缀(带点)
def get_files(file_path, ext):
    file_list = []
    dir_or_files = os.listdir(file_path)
    # dir_or_file不带路径
    for dir_or_file in dir_or_files:
        # 添加路径
        dir_file_path = os.path.join(file_path, dir_or_file)
        # 保留文件,去除文件夹
        if not os.path.isdir(dir_file_path):
            if os.path.splitext(dir_file_path)[-1] == ext:
                file_list.append(dir_file_path)
    return file_list


def contains_col(excel_file,ReStrContain=None,ReStrNotContain=None):
    if not ReStrContain and not ReStrContain:
        print('无筛选条件,退出...')
        sys.exit()
    df_dict = pd.read_excel(excel_file,sheet_name=None)
    base_name = os.path.basename(excel_file)
    file_name = os.path.splitext(base_name)[0]
    new_file = os.path.join(new_path, f'{file_name}_col_res.xlsx')
    with pd.ExcelWriter(new_file) as writer:
        for sheet_name,df_sheet in df_dict.items():
            if ColName in df_sheet.columns.values.tolist():
                df_sheet.loc[:,ColName] = df_sheet.loc[:,ColName].astype('string')
                # contains空字符串序列全为True(NA值除外)
                if not ReStrNotContain:
                    bool_res = (df_sheet[ColName].str.contains(f'{ReStrContain}'))
                else:
                    bool_res = (df_sheet[ColName].str.contains(f'{ReStrContain}')) & (~df_sheet[ColName].str.contains(f'{ReStrNotContain}'))
                # 筛选结果
                df_sheet_res = df_sheet[bool_res]
                print(f'{excel_file},{sheet_name}筛选:',df_sheet_res.shape[0])
                df_sheet_res.to_excel(writer,sheet_name=sheet_name,index=False)
            else:
                print(f'{excel_file},{sheet_name},无{ColName}列')

def main(file_list):
    for excel_file in file_list:
        contains_col(excel_file, ReStrContain, ReStrNotContain)


if __name__ == "__main__":
    excel_path = './excel_done'
    new_path = './myexcel'
    ColName = '标题' # 被筛选的列名
    ReStrContain = '北京|上海'  # 包含的元素(空字符串代表无限制条件),字符串或者正则
    ReStrNotContain = '二手|限购'  # 不包含的元素(空字符串代表无限制条件),字符串或者正则
    file_list = get_files(excel_path,'.xlsx')
    main(file_list)
