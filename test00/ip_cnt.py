"""
    作者：zf
    功能：
    版本：1.0
    日期：20190122
    新增功能：
"""
import os
import pandas as pd


def mk_dir(path1):
    folder = os.path.exists(path1)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        # makedirs 创建文件时如果路径不存在会创建这个路径
        os.makedirs(path1)
        print("---  new folder...  ---")
    else:
        print("---  There is this folder!  ---")


def data_cnt(file1, file2):
    with open(file1) as f_input:
        lines = f_input.readlines()  # 读取每一行

    list_ip = []
    list_cnt = []
    list_err = []

    for line in lines:
        result1 = line.find('/api/login/login')
        result2 = line.find('Login.php')

        err_count = 0
        if result1 >= 0:
            if result2 >= 0:
                err_count = 1
            list_str = line.split(' ')

            list_ip.append(list_str[4])
            list_cnt.append(1)
            list_err.append(err_count)

    data = {'ip': list_ip, 'ip_count': list_cnt, 'err_count': list_err}
    frame = pd.DataFrame(data)
    a = frame.groupby('ip').sum()
    a.to_csv(file2)


def main():
    """
        主函数
    """
    # 在Python中\是转义符，\u表示其后是UNICODE编码，因此\User会报错，需要在字符串前面加r
    path = r'C:\Users\Administrator\Documents\Tencent Files\462239531\FileRecv\log\201901_new'

    # 创建新目录
    path_cnt = path.replace('_new', '_cnt')
    mk_dir(path_cnt)

    # 列出文件夹下所有的目录与文件
    file_list = os.listdir(path)
    for i in range(0, len(file_list)):
        file = os.path.join(path, file_list[i])
        if os.path.isfile(file):
            print(file)
            # 命名新文件
            file_list_new = file_list[i].replace('new.log', 'cnt.csv')
            file_cnt = os.path.join(path_cnt, file_list_new)

            data_cnt(file, file_cnt)


if __name__ == '__main__':
    main()


