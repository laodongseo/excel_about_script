# ‐*‐ coding: utf‐8 ‐*‐
"""

"""

import pandas as pd  
citys = """
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
citys = [city.strip() for city in citys.split('\n') if city.strip()]
df_header = pd.DataFrame(columns=citys)


df = pd.read_excel('活动报名分配明细-20220722.xlsx')
df_fenpei = df[~(df['经纪人ID']==0)].copy()
with pd.ExcelWriter('结果.xlsx',date_format='YYYY-MM-DD') as f:
	for sheet,df_sheet in {'报名':df,'分配':df_fenpei}.items():
		df_pivot = df_sheet.pivot_table(values=['报名时间'], index=['报名日期'], columns=['城市'], aggfunc='count')
		df_pivot = df_pivot.droplevel(level=0,axis=1)
		df_res = df_header.append(df_pivot).fillna(0)
		df_res[citys].to_excel(f,sheet_name=sheet)
