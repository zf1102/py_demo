"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：8.0
    日期：20181116
    新增功能：网络爬虫，获取所有城市的信息并保存到csv文件中
"""
import csv
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
        # city_aqi.append((caption, value))
        city_aqi.append(value)
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
    # for city in city_list:
    #     city_name = city[0]
    #     city_pinyin = city[1]
    #     city_aqi = get_city_aqi(city_pinyin)
    #     print(city_name, city_aqi)
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']

    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录。(共{}条记录)'.format(i + 1, len(city_list)))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)


if __name__ == '__main__':
    main()



