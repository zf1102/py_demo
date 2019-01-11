"""
    作者：zf
    功能：判断密码强度
    版本：1.0
    日期：20181019
"""


def number_exist(pwd_str):
    """
        判断字符串中是否含有数字
    """
    for c in pwd_str:
        if c.isnumeric():
            return True
    return False


def letter_exist(pwd_str):
    """
        判断字符串中是否含有字母
    """
    for c in pwd_str:
        if c.isalpha():
            return True
    return False


def main():
    """
        主函数
    """
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
    else:
        print('密码强度不合格！')


if __name__ == '__main__':
    main()

