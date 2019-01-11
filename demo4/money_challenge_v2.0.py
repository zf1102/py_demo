"""
    作者：zf
    功能：52周存钱挑战
    版本：2.0
    日期：20180828
    新增功能：记录每周的存款数
"""
import math


def main():
    """
        主函数
    """
    # 每周存入金额
    money_per_week = 10
    # 记录周数
    i = 1
    # 递增金额
    increase_money = 10
    # 总共周数
    total_week = 52
    # 账户累计
    saving = 0
    # 记录每周存款数的列表
    money_list = []

    while i <= total_week:
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))

        # 更新信息
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()
