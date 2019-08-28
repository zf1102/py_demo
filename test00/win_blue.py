"""
    作者：zf
    功能：
    版本：1.0
    日期：20190213
    新增功能：
"""
import requests
from bs4 import BeautifulSoup


def main():
    """
        主函数
    """
    # 双色球开奖期号（从19016期开始）
    f_num = 19016
    # 用于接下来判断是否需要换行
    times = 1
    # while循环，获取开奖号码
    while f_num >= 18001:
        # 每一期的开奖地址
        url = "http://kaijiang.500.com/shtml/ssq/"+str(f_num)+".shtml"
        # 获取了页面，并完成了GBK的转码
        website_info = requests.get(url, timeout=30)
        # html.parser解析器
        soup = BeautifulSoup(website_info.text, "lxml")
        # 获取所有li标签中class为ball_blue的内容
        blue_ball = soup.find_all('li', 'ball_blue')
        # 要写入文件的地址
        file = open(r'C:\Users\Administrator\Desktop\双色球蓝球.txt', 'a+', encoding='utf-8')
        # 判断本次开奖号码已全部打印完，换行打印下一期
        file.write(str(blue_ball)+"\n")
        # 关闭打开文件
        file.close()
        f_num = f_num-1
    # 已完成打印
    else:
        print("Done")


if __name__ == '__main__':
    main()


