"""
    作者：zf
    功能：输入某年某月某日，判断是当年的第几天
    版本：2.0
    日期：20180911
    新增功能：用列表替换元组
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

    # 统计天数
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month_list[1] = 29

    days = sum(days_in_month_list[:month - 1]) + day

    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
