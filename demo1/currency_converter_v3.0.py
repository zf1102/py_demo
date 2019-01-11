"""
    作者：zf
    功能：汇率兑换
    版本：V3.0
    日期：20180820
    3.0 新增功能：程序一直运行，直到用户选择退出
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额(退出请输入Q)：')

i = 0

while currency_str_value != 'Q':
    # 统计循环次数
    i = i + 1
    print('循环次数为：', i)

    # 获取货币单位
    unit = currency_str_value[-3:]

    # 判断货币单位  pass为占位符
    if unit == 'CNY':

        # 输入为人民币
        rmb_str_value = currency_str_value[:-3]
        # 将纯数字字符串转换为数字
        rmb_value = eval(rmb_str_value)
        # 汇率计算
        usd_value = rmb_value / USD_VS_RMB
        # 输出
        print('美元(USD)金额是：', usd_value)

    elif unit == 'USD':

        # 输入为美元
        usd_str_value = currency_str_value[:-3]
        # 将纯数字字符串转换为数字
        usd_value = eval(usd_str_value)
        # 汇率计算
        rmb_value = usd_value * USD_VS_RMB
        # 输出
        print('人民币(CNY)金额是：', rmb_value)

    else:
        print('其他货币：', unit)

    print('********************************************************')
    # 带单位的货币输入
    currency_str_value = input('请输入带单位的货币金额(退出请输入Q)：')

print('程序已退出')
