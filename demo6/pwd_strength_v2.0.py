"""
    作者：zf
    功能：判断密码强度
    版本：2.0
    日期：20181022
    新增功能：1、限制密码设置次数  2、循环的终止
"""


def number_exist(pwd_str):
    """
        判断字符串中是否含有数字
    """
    has_number = False
    for c in pwd_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def letter_exist(pwd_str):
    """
        判断字符串中是否含有字母
    """
    has_letter = False
    for c in pwd_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """
    try_times = 5

    while try_times > 0:

        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则1、密码长度 >= 8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')
        # 规则2、密码包含数字
        if number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')
        # 规则3、密码包含字母
        if letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 3:
            print('恭喜，密码强度合格！')
            break
        else:
            try_times -= 1
            print('密码强度不合格！')
    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()

