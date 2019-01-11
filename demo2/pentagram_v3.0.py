"""
    作者：zf
    功能：五角星的绘制
    版本：3.0
    日期：20180823
    新增功能：使用迭代函数绘制重复不同大小的图形
"""
import turtle


def draw_recursive_pentagram(length):
    """
        迭代绘制五角星
    """
    # 计数器
    count = 1
    while count < 6:
        turtle.forward(length)
        turtle.right(144)
        # count = count + 1
        count += 1
    # 五角星绘制完成，更新参数length
    length += 20
    if length < 200:
        draw_recursive_pentagram(length)


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

    draw_recursive_pentagram(length)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
