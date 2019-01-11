"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：5.0
    日期：20181115
    新增功能：网络爬虫
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city = input('请输入城市拼音:')
    url = 'http://pm25.in/' + city
    url_text = get_html_text(url)

    # 文本解析
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''

    index = url_text.find(aqi_div)
    begin_idx = index + len(aqi_div)
    end_idx = begin_idx + 2
    aqi_val = url_text[begin_idx:end_idx]
    print('AQI为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()



