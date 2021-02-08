# -*- coding: utf-8 -*-
"""
去除公式和空行
空行可选一个空单元格为空或者整行全部为空则为空行
"""
import pandas as pd


excel_name = '2020友链小区交换'
any_all = 'any'
# 参数为None 代表读取所有sheet
df_dict = pd.read_excel(f'{excel_name}.xlsx',sheet_name=None,header=None)
with pd.ExcelWriter(f'{excel_name}_res.xlsx') as writer:
    for sheet,df in df_dict.items():
        df.dropna(axis=0,how=any_all,inplace=True) # 删除空行
        df.to_excel(writer,sheet_name=sheet,index=False,header=None)
