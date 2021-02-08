# -*- coding: utf-8 -*-
"""
统计1个excel里面每个sheet的某一列哪些值有重复
存在重复则把重复的值及重复次数写入excel
"""
import pandas as pd


def get_repeat(excel_name,col_name):
    # 参数为None 代表读取所有sheet
    df_dict = pd.read_excel(f'{excel_name}.xlsx',sheet_name=None)
    # 循环每个df拼接成一个
    df_end = pd.DataFrame()
    for sheet_name,df_sheet in df_dict.items():
        series_ = df_sheet[col_name].value_counts()
        series_res = series_[series_ > 1]
        frame = series_res.to_frame()
        frame = frame.reset_index()
        frame['sheet_name'] = sheet_name # 添加列用于区分
        df_end = pd.concat([df_end,frame])
    df_end.to_excel(f'{excel_name}{col_name}_repeat.xlsx',index=False)


if __name__ == '__main__':
    excel_name = 'pc_core_0608_new' # 不带后缀
    col_name = '城市'
    get_repeat(excel_name,col_name)
