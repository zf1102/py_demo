"""
    作者：zf
    功能：手机号判断
    版本：1.0
    日期：20181116
"""


def number_judge(number):
    d = {'1705': 'mobile', '1709': 'union', '1700': 'telecom'}
    cn_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178]
    cn_union = [130, 131, 132, 155, 156, 185, 186, 145, 176]
    cn_telecom = [133, 153, 180, 181, 189, 177]
    if number[:3] == '170':
        for number[:4] in d.keys():
            result_str = d[number[:4]]
    else:
        if int(number[:3]) in cn_mobile:
            result_str = 'mobile'
        elif int(number[:3]) in cn_union:
            result_str = 'union'
        elif int(number[:3]) in cn_telecom:
            result_str = 'telecom'
        else:
            result_str = 'No operator'
    return result_str


def main():
    """
        主函数
    """
    number = input('Enter your number:')
    if len(number) < 11:
        print('Invalid length,your number should be in 11 digits')
    else:
        result = number_judge(number)
        if result == 'No operator':
            print('No such a operator')
        else:
            print('Operator : china', result)


if __name__ == '__main__':
    main()