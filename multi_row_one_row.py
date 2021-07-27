# -*- coding: utf-8 -*-
"""
AA 12
AA 34
BB 56
BB 78
转为
AA 12-34
BB 56-78
"""
import pandas as pd
import numpy as np
import os


# grouyby函数来实现(速度比concat1慢很多)
def concat1(df_,col_name):
	items = [str(item) for item in df_[col_name].values.tolist()]
	row_str = '\t'.join(items)
	return row_str


# 数据透视表函数来实现
def concat2(series_col):
	items = [str(item) for item in series_col.values.tolist()]
	row_str = '\t'.join(items)
	return row_str



if __name__ == "__main__":
	excel_file = '小区词(租房二手房)收录.xlsx'
	df = pd.read_excel(f'{excel_file}')
	col_name = 'URL'

	# df_table  = df.groupby(['小区id']).apply(concat1,col_name)
	df_table  = pd.pivot_table(df,values=col_name, index=['小区id','city'],
                    aggfunc=concat2)
	df_table.to_excel('12.xlsx')
