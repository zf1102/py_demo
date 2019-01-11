"""
    作者：zf
    功能：52周存钱挑战
    版本：4.0
    日期：20180829
    新增功能：灵活设置参数
"""
import math


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
        计算n周内的存款金额
    """
    # 记录每周存款数的列表
    money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新信息
        money_per_week += increase_money


def main():
    """
        主函数
    """
    # 每周存入金额
    money_per_week = float(input('请输入每周存入的金额：'))
    # 递增金额
    increase_money = float(input('请输入每周递增的金额：'))
    # 总共周数
    total_week = int(input('请输入存款周数：'))
    # 调用函数
    save_money_in_n_weeks(money_per_week, increase_money, total_week)


if __name__ == '__main__':
    main()
