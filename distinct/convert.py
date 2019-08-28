"""
    作者：zf
    功能：
    版本：1.0
    日期：20190730
    新增功能：
"""
import json


def main():
    """
        主函数
    """

    # 要读取的文件地址
    file_in = open(r'C:\Users\Administrator\Desktop\FK-20190729.2\result_rme.2.txt', 'r', encoding='utf-8')
    # 要写入的文件地址
    file_out = open(r'C:\Users\Administrator\Desktop\FK-20190729.2\convert_result.txt', 'w', encoding='utf-8')

    head = next(file_in)
    print('基本信息:')
    print(head)

    # for i in range(1):
    #     f = file_in.readline().strip()

    for line in file_in:
        f = line.strip()
        str1 = '\t'.join(f.split('\t')[0:2])
        a = f.split('\t')[-1].encode('utf-8').decode("unicode_escape")
        print(a)
        array = json.loads(a)
        for j in array:
            print(j)
            line = '{0}\t{1}\t{2}\n'.format(str1, j['name'], j['phone'])
            print(line)
            file_out.write(line)
    file_out.close()
    print("Done!")


if __name__ == '__main__':
    main()


