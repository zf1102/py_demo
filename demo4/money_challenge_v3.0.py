"""
    作者：zf
    功能：52周存钱挑战
    版本：3.0
    日期：20180829
    新增功能：使用循环直接计数
"""
import math


def main():
    """
        主函数
    """
    # 每周存入金额
    money_per_week = 10
    # 递增金额
    increase_money = 10
    # 总共周数
    total_week = 52
    # 记录每周存款数的列表
    money_list = []

    for i in range(total_week):

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新信息
        money_per_week += increase_money


if __name__ == '__main__':
    main()
