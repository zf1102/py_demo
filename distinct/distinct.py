"""
    作者：zf
    功能：FK部门BQS多头申请实际值反馈的数据去重
    版本：1.0
    日期：20190225
"""


def main():
    """
        主函数
    """

    # 要读取的文件地址
    file_in = open(r'C:\Users\Administrator\Desktop\sql模版\distinct\MLP.xls', 'r', encoding='utf-8')
    # 要写入的文件地址
    file_out = open(r'C:\Users\Administrator\Desktop\sql模版\distinct\new-MLP.xls', 'w', encoding='utf-8')
    list_ref = []
    for line in file_in:
        tmp = line.strip()
        if tmp not in list_ref:
            list_ref.append(tmp)
            file_out.write(line)
    file_out.close()
    print("Done!")


if __name__ == '__main__':
    main()


