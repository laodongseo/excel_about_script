
# -*- coding:UTF-8 -*-
"""
指定1列或者多列为依据来求2个excel的差集
"""
import pandas as pd
import os


# 差集df1 - df2
def diff_excel(df1,df2):
    df1 = df1.append(df2)
    df1 = df1.append(df2) # 若追加1次,最后结果无法去掉属于2但不属于1的
    diff_df = df1.drop_duplicates(keep=False)
    return diff_df



def main():
    df_excel_1 = pd.read_excel(Excel_1)
    df1 = df_excel_1[TargetCols]

    df_excel_2 = pd.read_excel(Excel_2)
    df2 = df_excel_2[TargetCols]

    diff_df = diff_excel(df1,df2)
    if diff_df.shape[0] == 0:
        print('全部重复,不用对比,结束...')
        return
    df_res = diff_df.merge(df_excel_1,on=TargetCols)
    df_res.to_excel('diff_excel.xlsx',index=False)


if __name__ == "__main__":
    # 指定1列或多列对比,求Excel_1减Excel_2
    Excel_1 = 'test1.xlsx' 
    Excel_2 = 'test2.xlsx' 
    # 对比列
    TargetCols = ['communityid','communityname']
    main()
