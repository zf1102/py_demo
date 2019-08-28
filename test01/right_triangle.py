"""
    作者：zf
    功能：计算斜边长度
    版本：1.0
    日期：20181115
"""


def cal_hypotenuse(right_1, right_2):
    hypotenuse = (right_1 ** 2 + right_2 ** 2) ** 0.5
    return hypotenuse


def main():
    """
        主函数
    """
    right_str = input("请输入两条直角边(以逗号分隔):")
    right_1 = int(right_str[:1])
    right_2 = int(right_str[-1:])
    hypotenuse = cal_hypotenuse(right_1, right_2)
    print("计算出斜边长度为:{}".format(hypotenuse))


if __name__ == "__main__":
    main()