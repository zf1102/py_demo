"""
    作者：zf
    功能：52周存钱挑战
    版本：5.0
    日期：20180904
    新增功能：根据用户输入的日期判断是当年的第几周并输出相应的存款金额
"""
import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
        计算n周内的存款金额
    """
    # 记录每周存款数的列表
    money_list = []
    # 每周账户累计
    saved_money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新信息
        money_per_week += increase_money
    return saved_money_list


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
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')

    week_num = input_date.isocalendar()[1]
    print('第{}周的存款: {}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()
