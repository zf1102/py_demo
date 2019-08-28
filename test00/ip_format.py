"""
    作者：zf
    功能：IP地址LOG日志格式化
    版本：1.0
    日期：20190122
"""
import os


def data_format(file1):
    with open(file1, encoding='UTF-8') as input:
        lines = input.readlines()  # 读取每一行

    a = ''  # 空字符
    for line in lines:
        # strip是去掉每行末尾的换行符\n
        a += line.strip() + ' '
    # 将a分割成每个字符串
    c = a.split('---------------------------------------------------------------')
    # 将c的每个字符不以任何符号直接连接, strip("\n") 删除空行
    b = '\n'.join(c).strip("\n")
    return b


def mk_dir(path1):
    folder = os.path.exists(path1)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        # makedirs 创建文件时如果路径不存在会创建这个路径
        os.makedirs(path1)
        print("---  new folder...  ---")
    else:
        print("---  There is this folder!  ---")


def main():
    """
        主函数
    """
    # 在Python中\是转义符，\u表示其后是UNICODE编码，因此\User会报错，需要在字符串前面加r
    path = r'C:\Users\Administrator\Documents\Tencent Files\462239531\FileRecv\log\201901'

    # 列出文件夹下所有的目录与文件
    file_list = os.listdir(path)
    for i in range(0, len(file_list)):
        file = os.path.join(path, file_list[i])
        if os.path.isfile(file):
            print(file)
            str_a = data_format(file)
            # 创建新目录
            path_new = path + '_new'
            mk_dir(path_new)
            # 命名新文件
            file_list_new = file_list[i].replace('.', '_new.')
            file_new = os.path.join(path_new, file_list_new)
            print(file_new)
            # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            with open(file_new, 'w') as f:
                f.write(str_a)
                print("[ The write operation is complete! ]")


if __name__ == '__main__':
    main()


