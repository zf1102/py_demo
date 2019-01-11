"""
    作者：zf
    功能：五角星的绘制
    版本：1.0
    日期：20180822
"""
import turtle


def main():
    """
        主函数
    """
    count = 1

    while count < 6:
        turtle.forward(300)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
