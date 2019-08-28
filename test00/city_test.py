"""
    作者：zf
    功能：
    版本：1.0
    日期：20190219
    新增功能：
"""
import requests
from bs4 import BeautifulSoup


def main():
    """
        主函数
    """
    file = open(r'C:\Users\Administrator\Desktop\city_position.csv', 'a+', encoding='utf-8')
    file.write("code,name,longitude,latitude" + "\n")
    with open('test.txt') as f_input:
        lines = f_input.readlines()  # 读取每一行

    for line in lines:
        print(line.strip())
        url = "https://restapi.amap.com/v3/config/district?" + "key=3b6a1870b65097b2fa6cc3d141d00be6&" \
              + "subdistrict=0&extensions=base&keywords=" + line.strip()

        print(url)
        # 获取了页面，并完成了GBK的转码
        website_info = requests.get(url, timeout=30)
        soup = BeautifulSoup(website_info.text, "lxml")
        string = str(eval(str(soup)[15:-18])["districts"])[1:-1]
        print(string)
        dis = eval(string)
        file.write(dis["adcode"] + "," + dis["name"] + "," + dis["center"] + "\n")

    file.close()


if __name__ == '__main__':
    main()


