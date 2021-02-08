# -*- coding: utf-8 -*-
"""
1个excel里面
每个sheet指定几列删除重复行
指定保留first还是last
"""
import pandas as pd

excel_name = 'xiaoqu_hebing_str.xlsx'
col_names = ['communityid']
first_last = 'last'

# 参数为None 代表读取所有sheet
df_dict = pd.read_excel(excel_name,sheet_name=None)

with pd.ExcelWriter('{0}_del_repeat.xlsx'.format(excel_name)) as excel_writer:
    for sheet_name,df_sheet in df_dict.items():
        df_new = df_sheet.drop_duplicates(subset=col_names,keep=first_last).copy()
        df_new['communityid'] = df_new['communityid'].astype('string')
        df_new.to_excel(excel_writer,sheet_name=sheet_name,index=False)
