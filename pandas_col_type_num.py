# -*- coding: utf-8 -*-
"""
pandas指定一列来计算该列分类的个数
"""
import pandas as pd


def split_sheet(excel_file,col_name):
    with open(f'{excel_name}_{col_name}_count.txt','w',encoding='utf-8') as f:
        # 读取excel
        df_dict = pd.read_excel(f'{excel_name}.xlsx',sheet_name=None)
        for sheet_name,df_sheet in df_dict.items():
            # 循环每一类写入
            f.write(f'sheet:{sheet_name}\n')
            col_uniques = df_sheet[col_name].drop_duplicates().to_list()
            col_uniques.sort()
            for col in col_uniques:
                bool_df = df_sheet[col_name] == col
                my_df = df_sheet[bool_df]
                row_num = my_df.shape[0]
                f.write(f'{col}\t{row_num}\n')
            f.write('\n')
        

if __name__ == '__main__':
    excel_name = './bdpc1无排名次数' # 无后缀
    col_name = 'city'
    split_sheet(excel_name,col_name)
