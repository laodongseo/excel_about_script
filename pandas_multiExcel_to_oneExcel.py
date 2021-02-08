# ‐*‐coding:utf‐8‐*‐
"""
读取某个目录下多个excel合并成1个excel
每个excel第一列为表头,多个csv根据表头上下合并
"""
import os
import pandas


# 获取某个目录下的特定文件(含路径,非递归),ext为文件后缀(带点)
def get_files(file_path,ext):
    file_list = []
    dir_or_files = os.listdir(file_path)
    # dir_or_file纯文件名+后缀,不带路径
    for dir_or_file in dir_or_files:
        # 给目录或者文件添加路径
        dir_file_path = os.path.join(file_path, dir_or_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            pass
        else:
            if os.path.splitext(dir_file_path)[-1] == ext:
                file_list.append(dir_file_path)
    return file_list


def concat_file(files):
    df_concat = pandas.DataFrame()
    for file in files:
        # 参数为None 代表读取所有sheet
        df = pandas.read_excel(file,header=0)
        # 循环每个df拼接成一个,0是上下拼接
        df_concat = pandas.concat([df_concat, df],axis=0)
        # 写入新的excel
        df_concat.to_excel(f'{root_path}_concat_res.xlsx',index=False)


if __name__ == "__main__":
    root_path = r"./1/"
    files = get_files(root_path,'.xlsx')
    concat_file(files)
