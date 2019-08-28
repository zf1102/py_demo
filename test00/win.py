"""
    作者：zf
    功能：
    版本：1.0
    日期：20190213
    新增功能：
"""


def main():
    """
        主函数
    """
    import random
    # 定义一个列表在1,33之间
    ball_list = list(range(1, 34))
    # 从1,33之间取出来6个数
    red_ball_list = random.sample(ball_list, 6)
    red_ball_list.sort()
    ball_all = ""
    red_ball_str = ""
    # 随机取出一个数字在1,16之间
    blue_ball = random.randint(1, 16)
    for i in red_ball_list:
        # red_ball_str += '%02d ' % i
        red_ball_str += "{:02d} ".format(i)
    # ball_all += '%s + %02d' % (red_ball_str, blue_ball)
    ball_all += "{:s}+ {:02d}".format(red_ball_str, blue_ball)
    print(ball_all)


if __name__ == '__main__':
    main()


