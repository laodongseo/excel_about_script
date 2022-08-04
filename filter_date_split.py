#coding:utf8
"""
先把日期列转为日期格式
分割不同区间日期到不同sheet
"""
import pandas as pd
import os
from datetime import datetime


file_path = 'concat_res.xlsx'
date_ranges = [('20220101','20220527')]
res_file = os.path.splitext(file_path)[0]+f'_分日期.xlsx'
# 邀约注册表
df = pd.read_excel(file_path)
# 去掉列头空格
df.columns = [i.strip() for i in df.columns]
# 转为日期格式
df['日期']=df['日期'].astype('string')
df['日期'] = df['日期'].apply(lambda x:datetime.strptime(str(x), '%Y%m%d'))
df['日期'] = df['日期'].astype('datetime64[ns]')
df['周数'] = df['日期'].dt.isocalendar().week
df['月'] = df['日期'].dt.month
df['季度'] = df['日期'].dt.quarter
df['周区间'] = df[['日期','周数']].groupby('周数')['日期'].transform(lambda x:f'{x.iloc[0]}_{x.iloc[-1]}')
df['周区间'] = df['周区间'].astype('string').str.replace('2022-| 00:00:00','',regex=True)


f = pd.ExcelWriter(res_file,datetime_format='YYYY-MM-DD')
for start,end in date_ranges:
	start_date = datetime.strptime(start,'%Y%m%d')
	end_date = datetime.strptime(end,'%Y%m%d')
	bool_date = (df['日期'] <= end_date) & (df['日期'] >= start_date)
	df_daterange = df[bool_date].copy()
	df_daterange.to_excel(f,sheet_name=f'{start}-{end}',index=False)
df.to_excel(f,sheet_name='全量',index=False)
f.close()
