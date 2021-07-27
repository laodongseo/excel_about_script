# -*- coding: utf-8 -*-
"""
AA	type1	ok
AA1	type2	no
AA2	type3	ok
BB1	type1	ok
BB2	type2	ok
BB3	type3	no
转为
AA	ok	AA1	no	AA2	ok
BB1	ok	BB2	ok	BB3	no
"""
import pandas as pd
import numpy as np
import os


excel_file = '小区词(租房二手房)收录.xlsx'
col_name = '页面类型' # 分类的列
need_cols = ['URL','收录情况'] # 除首次外,再次关联限定的列

df = pd.read_excel(excel_file)
gb = df.groupby(col_name)
n = 1
df_last = pd.DataFrame()
for name,df_gb in gb:
	df_gb.set_index('小区id',inplace=True)
	del df_gb[col_name]
	if n >1 :
		df_last = pd.concat([df_gb[need_cols],df_last],1)
	else:
		df_last = pd.concat([df_gb,df_last],1)
	n += 1

df_last.to_excel('aa.xlsx')
