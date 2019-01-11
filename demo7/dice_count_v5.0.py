"""
    作者：zf
    功能：投掷骰子，显示点数的出现次数及频率
    版本：5.0
    日期：20181024
    新增功能：科学计算
"""
import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题，改为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 100

    # 记录骰子的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(result_arr, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.9)

    # 设置x轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('出现频率')
    plt.show()


if __name__ == '__main__':
    main()

