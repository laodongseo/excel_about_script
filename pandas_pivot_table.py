# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
import numpy as np

excel_name = '2021_5i5j_lianjia租房二手房收录.xlsx'
sheet_name = '总表(南宁分离)'
df = pd.read_excel(f'{excel_name}',sheet_name=sheet_name)
df_table  = pd.pivot_table(df,values='url', index=['城市', '是否地铁','房源范围'],
                    columns=['是否收录'], aggfunc='count')
df_table.to_excel('11.xlsx')
