# -*- coding: utf-8 -*-
"""
按固定行数分割1个大excel的第1个sheet文件为多个sheet
默认第一行为表头
"""
import pandas as pd
import math
import os


def split_excel(excel_file,constNum):
	df = pd.read_excel(excel_file)
	rows,cols = df.shape # 默认第一行表头不算行数
	split_times = math.floor(rows/constNum) # 标准分割次数
	split_rows_count = split_times*constNum # 标准分割所占用总行数
	new_list = [(start,start+constNum) for start in range(0,split_rows_count,constNum)]
	print(new_list)
	filename = os.path.basename(excel_file)
	# 标准行数文件,start,end为索引
	for start,end in new_list:
		excel_small = df[start:end]
		excel_small.to_excel(f'{filename}_{start+1}_{end}.xlsx',index=False)

	# 剩余的行分割出文件
	df[split_rows_count:].to_excel(f'{filename}_last.xlsx',index=False)


if __name__ == '__main__':
	excel_file = '2021-12-08_东莞_sale.xlsx'
	constNum = 200 # 固定行数分割excel
	split_excel(excel_file,constNum)
