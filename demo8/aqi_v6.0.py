"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：6.0
    日期：20181115
    新增功能：网络爬虫，高效处理与解析
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', class_="span1")

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', class_="caption").text.strip()
        value = div_content.find('div', class_="value").text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city = input('请输入城市拼音:')
    # 文本解析
    city_aqi = get_city_aqi(city)

    print(city_aqi)


if __name__ == '__main__':
    main()



