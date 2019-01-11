"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：7.0
    日期：20181116
    新增功能：网络爬虫，获取所有城市的信息
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


def get_all_cities():
    """
        获取所有城市及url
    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', class_="bottom")[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)


if __name__ == '__main__':
    main()



