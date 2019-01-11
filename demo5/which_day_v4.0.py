"""
    作者：zf
    功能：输入某年某月某日，判断是当年的第几天
    版本：4.0
    日期：20181018
    新增功能：将月份及其对应天数通过字典表示
"""
from datetime import datetime


def is_leap_year(year):
    """
        判断是否为闰年
        是则返回True
        否则返回False
    """
    flag = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        flag = True

    return flag


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 月份--天数 字典
    # month_day_dict = {1: 31,
    #                   2: 28,
    #                   3: 31,
    #                   4: 30,
    #                   5: 31,
    #                   6: 30,
    #                   7: 31,
    #                   8: 31,
    #                   9: 30,
    #                   10: 31,
    #                   11: 30,
    #                   12: 31
    #                   }

    # 类似V3.0版本的set集合
    day_month_dict = {28: 2, 30: {4, 6, 9, 11}, 31: {1, 3, 5, 7, 8, 10, 12}}

    # 初始值
    days = 0
    days += day

    # for i in range(1, month):
    #     days += month_day_dict[i]

    for i in range(1, month):
        if i in day_month_dict[30]:
            days += 30
        elif i in day_month_dict[31]:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
