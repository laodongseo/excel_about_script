# -*- coding: utf-8 -*-
"""
同1个excel里多个sheet合并为1个sheet
sheet默认用第一行作为列索引
如果sheet无表头则修改header参数为None
合并后的大sheet新增一列label作为sheet标记方便区分
"""
import pandas as pd

excel_name = '2020kwd_url_core_city_unique'
# 参数为None 代表读取所有sheet
df_dicts = pd.read_excel(f'{excel_name}.xlsx',sheet_name=None,header=0)
# 创建空df用来连接
df_concat = pd.DataFrame()
# 循环每个df拼接成一个
for sheet_name,df_sheet in df_dicts.items():
	df_sheet['label'] = sheet_name # 新增一列作为sheet区分
	df_concat = pd.concat([df_concat,df_sheet],axis=0,sort=False)
# 写入新的excel
df_concat.to_excel(f'{excel_name}_res.xlsx',index=False)
