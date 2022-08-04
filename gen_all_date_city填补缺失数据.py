"""
分月分城市 可能会缺少月和城市
"""

city_order = """
北京
杭州
天津
上海
南京
太原
常州
无锡
东莞
郑州
南昌
长沙
青岛
西安咸阳
临汾
呼和浩特
烟台
合肥
赤峰
临沂
"""
citys = [i.strip() for i in city_order.split('\n') if i.strip()]

df_config = pd.DataFrame()
DatetimeIndex = pd.date_range(start='20220427', end='20220721')
for city in citys:
	df_one = pd.DataFrame(index=DatetimeIndex)
	df_one['城市'] = city
	df_config = pd.concat([df_config,df_one],axis=0)
df_config.index.name='日期'
df_config.reset_index(inplace=True)
df_config.to_excel('aaa.xlsx',index=False)
