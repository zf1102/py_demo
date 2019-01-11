"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：2.0
    日期：20181108
    新增功能：输出到json文件中
"""
import json


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city["aqi"])
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')

    # ensure_ascii=False解决中文乱码问题
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()

    print(city_list)


if __name__ == '__main__':
    main()



