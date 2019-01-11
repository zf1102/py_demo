"""
    作者:zf
    功能：BMR计算器
    版本：4.0
    日期：20180827
    新增功能：处理异常操作
"""


def main():
    """
        主函数
    """
    flag = input('是否退出程序(y/n)？')

    while flag == 'n':
        # 性别、体重(kg)、身高(cm)、年龄
        print('请输入一下信息,用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')

        try:
            gender = input_str.split(' ')[0]
            weight = float(input_str.split(' ')[1])
            height = float(input_str.split(' ')[2])
            age = int(input_str.split(' ')[3])

            if gender == '男':
                # 男性
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                # 女性
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print('基础代谢率：{}大卡'.format(bmr))
            else:
                print('暂不支持该性别的BMR计算')
        except ValueError:
            print('请输入正确信息！')
        except IndexError:
            print('输入的信息过少！')
        except:
            print('程序异常!')

        print('****************************')
        flag = input('是否退出程序(y/n)？')


if __name__ == '__main__':
    main()
