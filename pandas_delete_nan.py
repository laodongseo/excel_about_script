# -*- coding: utf-8 -*-
"""
批量删除excel或者csv含有空白单元格的行
"""
import os
import pandas as pd



def excel_del_nan(xcel_files):
	for excel_file in excel_files:
		excel_file_name,ext = os.path.splitext(excel_file)
		with pd.ExcelWriter('{0}_new.xlsx'.format(excel_file_name)) as writer: 
			df_dict = pd.read_excel(excel_file,sheet_name=None)
			citys = df_dict.keys()
			for city in citys:
				df = df_dict[city]
				df.dropna(axis=0,how='any',inplace=True)
				df.to_excel(writer,sheet_name=city,index=False)


def csv_del_nan(csv_files,encode_now='GB18030'):
	for csv_file in csv_files:
		csv_file_name,ext = os.path.splitext(csv_file)
		with pd.ExcelWriter('{0}_new.xlsx'.format(csv_file_name)) as writer:
				df = pd.read_csv(csv_file,encoding=encode_now)
				df.dropna(axis=0,how='any',inplace=True)
				df.to_excel(writer,index=False)

if __name__ == "__main__":
	excel_excel_files = ['./小区_sale_分城市.xlsx','./小区_rent_分城市.xlsx']
	# excel文件
	excels = ['小区_rent.csv_分城市.xlsx']
	# csv文件
	csvs = ['小区_sale.csv','小区_rent.csv']
	csv_del_nan(csvs,'GBK')
