"""
    作者：zf
    功能：
    版本：1.0
    日期：20190819
    新增功能：
"""
from time import sleep

# import pprint as pp
# my_mapping = [{'a': 23, 'b': 42, 'c': 0xc0ffee}, {'a': 231, 'b': 42, 'c': 0xc0ffee}]
# pp.pprint(my_mapping, width=10)


def progress(percent=0, width=50):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


def main():
    """
        主函数
    """
    for i in range(101):
        progress(i)
        sleep(0.1)


if __name__ == '__main__':
    main()


