# -*- coding:UTF-8 -*-
"""
2个excel的sheet名一样
2个excel每2个相同的sheet根据某1列或者二多列求并集合并
"""
import pandas as pd
from urllib.parse import unquote

# 最终excel列的顺序
cols_last = ['cityid','cityname','sale房源','rent房源','总房源']
# 指定多重索引(2个excel哪些列求并集)
index_cols = ['communityid','communityname']

df_dict_rent = pd.read_excel('小区_sale_add_city_del_nan_str_city.xlsx',sheet_name=None)
df_dict_sale = pd.read_excel('小区_rent_add_city_del_nan_str_city.xlsx',sheet_name=None)
sheet_names_rent,sheet_names_sale, = df_dict_rent.keys(),df_dict_sale.keys()

if sheet_names_rent == sheet_names_sale:
    with pd.ExcelWriter('xiaoqu_hebing.xlsx') as writer:
        for sheet_name in sheet_names_rent:
            df_rent = df_dict_rent[sheet_name]
            df_sale = df_dict_sale[sheet_name]
            cityid, city_name = df_sale['cityid'].to_list()[0], df_sale['cityname'].to_list()[0]
            del df_sale['cityid'],df_sale['cityname']
            del df_rent['cityid'],df_rent['cityname']
            
            # 分别set索引
            df_rent.set_index(index_cols, inplace=True)
            df_sale.set_index(index_cols, inplace=True)

            # 索引求交集
            rent_index = df_rent.index.to_list()
            sale_index = df_sale.index.to_list()
            index_all = rent_index + sale_index
            index_all_unique = set(index_all)
            print(sheet_name,len(rent_index),len(sale_index),len(index_all), len(index_all_unique))

            # 分别重新索引
            df_rent_new = df_rent.reindex(index_all_unique, fill_value=0)
            df_sale_new = df_sale.reindex(index_all_unique, fill_value=0)

            # 修改特定列
            df_rent_new['cityname'] = city_name
            df_sale_new['cityid'] = cityid
            # df_rent_new.rename(columns={"COUNT(*)": "租房房源"},inplace=True)
            # df_sale_new.rename(columns={"COUNT(*)": "二手房房源"},inplace=True)
            # del df_sale_new['cityid'],df_sale_new['cityname']

            # 拼接
            df_last = pd.concat([df_rent_new, df_sale_new], axis=1)
            df_last['总房源'] = df_last['rent房源'] + df_last['sale房源']
            df_last = df_last[cols_last]
            df_last.to_excel(writer,sheet_name=city_name)
else:
    print('检查2个excel文件是否对应')
