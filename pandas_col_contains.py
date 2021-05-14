import pandas as pd
import os
import sys
"""
文本筛选
筛选某1列是否包含某些字符及不包含某些字符
筛选条件支持正则
excel可有多个sheet,各sheet被筛选的列名要一致
"""


def contains_col(excel_path,ReStrContain=None,ReStrNotContain=None):
    if not ReStrContain and not ReStrContain:
        print('无筛选条件,退出...')
        sys.exit()
    df_dict = pd.read_excel(excel_path,sheet_name=None)
    fname,ext = os.path.splitext(excel_path)
    with pd.ExcelWriter(f'{fname}_col_res.xlsx') as writer:
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
                print(f'{sheet_name}筛选:',df_sheet_res.shape[0])
                df_sheet_res.to_excel(writer,sheet_name=sheet_name,index=False)
            else:
                print(sheet_name,f'无{ColName}列')


if __name__ == "__main__":
    excel_path = './标题.xlsx'
    ColName = 'title' # 被筛选的列名
    ReStrContain = '北京|上海'  # 包含的元素(空字符串代表无限制条件),字符串或者正则
    ReStrNotContain = '二手|限购'  # 不包含的元素(空字符串代表无限制条件),字符串或者正则
    contains_col(excel_path,ReStrContain,ReStrNotContain)
