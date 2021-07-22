# -*- coding: utf-8 -*-
"""
1个excel里面每个sheet对另外1个excel的同名sheet做vlookup
"""
import pandas as pd
import os


# merge两列数据类型要一致
def vlookup(excel_left,excel_right,cols_right_need,left_col,right_col):
	df_dict = pd.read_excel(excel_left,sheet_name=None)
	df_right = pd.read_excel(excel_right,sheet_name=None,header=None)
	name_res = os.path.splitext(excel_left)[0]

	with pd.ExcelWriter(f'{name_res}_vlookup_res.xlsx') as writer:
		for sheet_name,df_sheet in df_dict.items():
			cols_right_need.extend(right_col)
			df = df_sheet.merge(df_right[sheet_name][cols_right_need],left_on=left_col, right_on=right_col,how='left')
			df['communityid'] = df['communityid'].astype('string')
			df.to_excel(writer,sheet_name=sheet_name,index=False)


if __name__ == '__main__':
	dic = {
	'excel_left':'xiaoqu_hebing_str_del_repeat_add_col.xlsx',
	'excel_right':'111.xlsx',
	'cols_right_need':['小区url','状态码'], # excel_right到excel_left的列
	'left_col':['小区url'], # 以什么列为基准vlookup
	'right_col':['小区url'] # 以什么列为基准vlookup
	}
	vlookup(**dic)
