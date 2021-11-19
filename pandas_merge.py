# -*- coding: utf-8 -*-
"""
1个excel里面每个sheet对另外1个excel的第1个sheet做vlookup
"""
import pandas as pd
import os


# # merge两列数据类型要一致
def vlookup(excel_left,excel_right,cols_right_need,left_col,right_col):
	# 参数为None 代表读取所有sheet
	df_left = pd.read_excel(excel_left)
	df_right = pd.read_excel(excel_right)

	with pd.ExcelWriter('./merge_res.xlsx') as writer:
		if not cols_right_need:
			df = df_left.merge(df_right,left_on=left_col, right_on=right_col)
		else:
			cols_right_need.extend(right_col) # 防止没有right_col
			cols_right_need = set(cols_right_need) # 防止right_col重复
			df = df_left.merge(df_right[cols_right_need],left_on=left_col, right_on=right_col)
		df.to_excel(writer,index=False)


if __name__ == '__main__':
	dic = {
	'excel_left':r'C:\Users\Administrator\Desktop\排名5i5j.com_5i5j.com_2021.07.27.xls',
	'excel_right':r'E:\py3script-工作\5i5j\j监控\2020小区词监控2020\2021xiaoqu_kwd_city_含表头_one_sheet.xlsx',
	'cols_right_need':[], # excel_right到excel_left的列
	'left_col':['关键字'], # 以什么列为基准vlookup
	'right_col':['kwd'] # 以什么列为基准vlookup
	}
	vlookup(**dic)
