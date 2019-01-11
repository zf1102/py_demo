"""
    作者：zf
    功能：汇率兑换
    版本：V5.0
    日期：20180821
    5.0 新增功能：
        1、程序结构化
        2、简单函数定义 lambda

    TODO:(1)保存多种货币汇率而不是单一汇率->集合操作 (2)获取实时汇率->网络爬虫
"""


# def convert_currency(im, er):
#     """
#         汇率兑换函数
#     """
#     out = im * er
#     return out


def main():
    """
        主函数
    """
    # 汇率
    USD_VS_RMB = 6.77

    # 带单位的货币输入
    currency_str_value = input('请输入带单位的货币金额：')

    # 获取货币单位
    unit = currency_str_value[-3:]

    # 判断货币单位  pass为占位符
    if unit == 'CNY':
        exchange_rate = 1/USD_VS_RMB

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        # 使用lambda定义函数
        convert_currency2 = lambda x: x * exchange_rate

        # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)
        out_money = convert_currency2(in_money)
        print('转换后的金额：', out_money)
    else:
        print('不支持该种货币！')


if __name__ == '__main__':
    main()
