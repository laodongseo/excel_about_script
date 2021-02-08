# -*- coding: utf-8 -*-
"""
统计1个excel里面每个sheet的行数和列数及所有sheet的行列总数
第1行为表头 不计在内
"""
import pandas as pd

excel_name = 'xiaoqu_hebing_str_add'
# 参数为None 代表读取所有sheet
df_dict = pd.read_excel(f'{excel_name}.xlsx',sheet_name=None)
row_all = col_all = 0
with open('excel_tongji_res.txt','w',encoding='utf-8') as f:
	for sheet_name,df_sheet in df_dict.items():
	    row_num,col_num = df_sheet.shape
	    row_all += row_num
	    col_all += col_num
	    f.write(f'{sheet_name}\t{row_num}\t{col_num}\n')
	f.write(f'合计\t{row_all}\t{col_all}\n')

