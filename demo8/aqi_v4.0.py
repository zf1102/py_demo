"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：4.0
    日期：20181109
    新增功能：判断输入文件的格式
"""
import json
import csv
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        解码csv文件
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('不支持的文件格式！')


if __name__ == '__main__':
    main()



