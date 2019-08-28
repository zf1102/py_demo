"""
    作者：zf
    功能：投掷三个骰子，比大小
    版本：1.0
    日期：20181115
"""
import random


def roll_dice(number=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while number > 0:
        point = random.randrange(1, 7)
        points.append(point)
        number -= 1
    return points


def roll_result(total):
    is_big = 11 <= total <= 18
    is_small = 3 <= total <= 10
    if is_big:
        return 'big'
    elif is_small:
        return 'small'


def main():
    """
        主函数
    """
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['big', 'small']
    choice = input("big or small:")
    if choice in choices:
        points = roll_dice()
        total = sum(points)
        win = choice == roll_result(total)
        if win:
            print('The points are', points, 'U win !')
        else:
            print('The points are', points, 'U lose !')
    else:
        print('Invalid Words')
        main()


if __name__ == "__main__":
    main()
