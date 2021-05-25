import pandas as pd
import os
import sys
"""
读取某路径下的excel文件
对每个文件的1列或者多列进行数值筛选后生成新文件
"""


# 获取某目录下的特定文件(含路径),ext为文件后缀(带点)
def get_files(file_path, ext):
    file_list = []
    dir_or_files = os.listdir(file_path)
    # dir_or_file不带路径
    for dir_or_file in dir_or_files:
        # 添加路径
        dir_file_path = os.path.join(file_path, dir_or_file)
        # 保留文件,去除文件夹
        if not os.path.isdir(dir_file_path):
            if os.path.splitext(dir_file_path)[-1] == ext:
                file_list.append(dir_file_path)
    return file_list


def main(excel_files):
    for excel_file in excel_files:
        df = pd.read_excel(excel_file)
        for col in cols:
            try:
                df[col] = df[col].astype('float64')
            except Exception as e:
                print(e)
                print(f'请检查{col}列数据是否未数值')
                sys.exit()
        df_new = df.query(condition)
        base_name = os.path.basename(excel_file)
        file_name = os.path.splitext(base_name)[0]
        new_file = os.path.join(new_path, f'{file_name}.xlsx')
        print(f'{excel_file}:排序完成')
        df_new.to_excel(new_file,index=False)


if __name__ == "__main__":
    excel_path = './excel_done'
    new_path = './myexcel'
    cols = ['付款人数','信誉','价格','tb-pdd'] # 需要排序的数值列
    # 排序条件,用反引号包裹非正常列名
    condition = '(1 <付款人数 <1000) & (1<信誉<10) & (100<价格<9999999) & (50<`tb-pdd`<9999999)'
    excel_files = get_files(excel_path,'.xlsx')
    main(excel_files)
