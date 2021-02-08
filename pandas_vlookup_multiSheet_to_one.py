# -*- coding: utf-8 -*-
"""
1个excel里面每个sheet对另外1个excel的第1个sheet做vlookup
"""
import pandas as pd
import os


def vlookup(excel_left,excel_right,cols_need,left_col,right_col):
	# 参数为None 代表读取所有sheet
	df_dict = pd.read_excel(excel_left,sheet_name=None)
	df_right = pd.read_excel(excel_right)
	name_res = os.path.splitext(excel_left)[0]

	with pd.ExcelWriter(f'{name_res}_vlookup_res.xlsx') as writer:
		for sheet_name,df_sheet in df_dict.items():
		    df = df_sheet.merge(df_right[cols_need],left_on=left_col, right_on=right_col)
		    df['communityid'] = df['communityid'].astype('string')
		    df.to_excel(writer,sheet_name=sheet_name,index=False)


if __name__ == '__main__':
	dic = {
	'excel_left':'xiaoqu_hebing_str_del_repeat_add_col.xlsx',
	'excel_right':'111.xlsx',
	'cols_need':['小区url','状态码'], # excel_right需要的数据列
	'left_col':'小区url', # 以什么列为基准vlookup
	'right_col':'小区url' # 以什么列为基准vlookup
	}
	vlookup(**dic)
