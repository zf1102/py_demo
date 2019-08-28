"""
    作者：zf
    功能：重量转换
    版本：1.0
    日期：20181115
"""


def weight_transfer(weight_g):
    weight_kg = weight_g / 1000
    return weight_kg


def main():
    """
        主函数
    """
    weight_g = int(input("请输入重量(单位为g)："))
    weight_kg = weight_transfer(weight_g)
    print("转换后的结果为{}kg".format(weight_kg))


if __name__ == "__main__":
    main()
