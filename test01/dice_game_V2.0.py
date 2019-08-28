"""
    作者：zf
    功能：投掷三个骰子，比大小
    版本：2.0
    日期：20181116
    新增功能：添加下注金额，赔率为 1:1
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
    money = 1000
    while money > 0:
        choice = input("big or small:")
        amount = int(input('How much you wanna bet ? -'))
        if amount <= money:
            if choice in choices:
                points = roll_dice()
                total = sum(points)
                win = choice == roll_result(total)
                if win:
                    print('The points are', points, 'U win !')
                    money += amount
                    print('U gained', amount, ', you have', money, 'now')
                else:
                    print('The points are', points, 'U lose !')
                    money -= amount
                    print('U lost', amount, ', you have ', money, 'now')
            else:
                print('Invalid Words')
                main()
        else:
            print('sorry, your money is not enough!')
    else:
        print('GAME OVER!')


if __name__ == "__main__":
    main()
