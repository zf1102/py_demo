"""
    作者：zf
    功能：利用递归函数绘制分形树
    版本：1.0
    日期：20180824
"""
import turtle


def draw_branch(length):
    """
        绘制分形树
    """
    if length > 5:
        # 绘制右侧树枝
        turtle.forward(length)
        print('向前', length)
        turtle.right(20)
        print('右转 20')
        draw_branch(length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(length - 15)

        # 返回到原点
        turtle.right(20)
        print('右转 20')
        turtle.backward(length)
        print('向后', length)


def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(80)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
