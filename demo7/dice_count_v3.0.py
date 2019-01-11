"""
    作者：zf
    功能：投掷骰子，显示点数的出现次数及频率
    版本：3.0
    日期：20181024
    新增功能：可视化同时投掷两个骰子的结果
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 100

    # 初始化列表
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    # 分别记录骰子的结果
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):
            if (roll1+roll2) == j:
                roll_dict[j] += 1

    print(result_list)

    for i, result in roll_dict.items():
        print('点数{}出现的次数是：{},频率是：{}'.format(i, result, result / total_times))

    # 数据可视化，散点图
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()

