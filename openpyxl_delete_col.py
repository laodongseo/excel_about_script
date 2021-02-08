# ‐*‐coding:utf‐8‐*‐
"""
指定列数开始和结尾
列数起始索引为1
1个excel每个sheet的起始到结尾列
"""

from openpyxl import load_workbook


def delete_row(filepath,newfile,num1,num2):
    wb = load_workbook(filepath,data_only=True)
    for ws in wb:
        ws.delete_cols(num1,num2)
    wb.save(newfile)

if __name__ == "__main__":
    excel_name = '长沙' # 无后缀
    delete_row(f'{excel_name}.xlsx',f'{excel_name}_del_col.xlsx',1,3)
