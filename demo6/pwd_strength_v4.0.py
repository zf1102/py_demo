"""
    作者：zf
    功能：判断密码强度
    版本：4.0
    日期：20181023
    新增功能：文件读操作
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
    # try_times = 5
    #
    # while try_times > 0:
    #
    #     password = input('请输入密码：')
    #
    #     # 密码强度
    #     strength_level = 0
    #
    #     # 规则1、密码长度 >= 8
    #     if len(password) >= 8:
    #         strength_level += 1
    #     else:
    #         print('密码长度要求至少8位！')
    #     # 规则2、密码包含数字
    #     if number_exist(password):
    #         strength_level += 1
    #     else:
    #         print('密码要求包含数字！')
    #     # 规则3、密码包含字母
    #     if letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('密码要求包含字母！')
    #
    #     f = open('password_3.0.txt', 'a')
    #     f.write('密码：{}, 强度：{}\n'.format(password, strength_level))
    #     f.close()
    #
    #     if strength_level == 3:
    #         print('恭喜，密码强度合格！')
    #         break
    #     else:
    #         try_times -= 1
    #         print('密码强度不合格！')
    # if try_times <= 0:
    #     print('尝试次数过多，密码设置失败！')

    # 读取文件
    f = open('password_3.0.txt', 'r')

    # 1.read()
    # content = f.read()
    # print(content)

    # 2.readline(),多行需文件遍历
    # line = f.readline()
    # print(line)

    # 3.readlines(),返回值为list类型
    for line in f.readlines():
        print('read: {}'.format(line))

    f.close()


if __name__ == '__main__':
    main()

