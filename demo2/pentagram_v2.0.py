"""
    作者：zf
    功能：五角星的绘制
    版本：2.0
    日期：20180823
    新增功能：循环操作绘制重复不同大小的图形
"""
import turtle


def draw_pentagram(length):
    """
        绘制五角星
    """
    # 计数器
    count = 1
    while count < 6:
        turtle.forward(length)
        turtle.right(144)
        # count = count + 1
        count += 1


def main():
    """
        主函数
    """
    # 画笔位置、颜色、粗细初始化
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(1.5)
    turtle.pencolor('green')

    length = 100

    while length < 200:
        draw_pentagram(length)
        # length = length + 20
        length += 20

    turtle.exitonclick()


if __name__ == '__main__':
    main()
