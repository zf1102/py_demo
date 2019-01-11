"""
    作者:zf
    功能：BMR计算器
    版本：2.0
    日期：20180827
    新增功能：根据用户输入计算BMR，程序持续运行
"""


def main():
    """
        主函数
    """
    flag = input('是否退出程序(y/n)？')

    while flag == 'n':
        # 性别、体重(kg)、身高(cm)、年龄
        gender = input('性别：')

        weight = float(input('体重(kg):'))

        height = float(input('身高(cm):'))

        age = int(input('年龄:'))

        if gender == '男':
            # 男性
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == '女':
            # 女性
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率：', bmr)
        else:
            print('暂不支持该性别的BMR计算')

        print('****************************')
        flag = input('是否退出程序(y/n)？')


if __name__ == '__main__':
    main()
