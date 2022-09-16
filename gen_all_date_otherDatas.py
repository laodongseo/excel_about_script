DictData = {
'date':pd.date_range(start='20220720', end='20220721'),
'city':['北京','上海','南京','苏州'],
'b_type':['租房','二手房','新房'],

}


rows = []
row = []
for date in DictData['date']:
	for city in DictData['city']:
		for b_type in DictData['b_type']:
			row.extend([date,city,b_type])
			rows.append(row)
			row = []

df = pd.DataFrame(data=rows,columns=DictData.keys())
with pd.ExcelWriter('aa.xlsx',datetime_format='YYYY-MM-DD') as f:
	df.to_excel(f,'aa')
