# ‐*‐coding:utf‐8‐*‐
"""
指定起始行,偏移量,是否保留公式
起始行从1开始算,便移量=0是删除所有行,偏移量=1删除第一行
is_data_only参数是否保留公式1保留,2不保留
"""
from openpyxl import load_workbook


# 从第start_num行开始删(包含start_num行),共删除offset_num行
def delete_row(filepath,newfile,start_num,offset_num,is_data_only=0):
    wb = load_workbook(filepath,data_only=False if is_data_only==0 else True)
    for ws in wb:
    	if ws.title != '汇总':
            ws.delete_rows(start_num,offset_num)
    wb.save('{0}.xlsx'.format(newfile))


delete_row('bdmo重点词首页词监控top1_10分布.xlsx','bdmo重点词首页词监控top1_10分布',3,30)
董⃰某⃰人
