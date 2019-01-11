"""
    作者：zf
    功能：投掷骰子，显示点数的出现次数及频率
    版本：4.0
    日期：20181024
    新增功能：使用直方图可视化结果
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题，改为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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

    # 记录骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1+roll2)

    # 数据可视化，直方图
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('出现频率')
    plt.show()


if __name__ == '__main__':
    main()

