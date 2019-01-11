"""
    作者：zf
    功能：计算空气质量指数AQI
    版本：10.0
    日期：20181122
    新增功能：数据过滤与数据可视化
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data[['City', 'AQI']])

    print('基本信息:')
    print(aqi_data.info())

    print('数据预览:')
    print(aqi_data.head(5))

    # 数据清洗
    # 只保留AQI>0的数据
    # clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    filter_condition = aqi_data['AQI'] > 0
    clean_aqi_data = aqi_data[filter_condition]

    # 基本统计
    print('AQI最大值:', clean_aqi_data['AQI'].max())
    print('AQI最小值:', clean_aqi_data['AQI'].min())
    print('AQI平均值:', clean_aqi_data['AQI'].mean())

    # top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='pie', x='City', y='AQI', title='空气质量最好的50个城市',
                      figsize=(20, 10))
    plt.savefig('top50_aqi_pie.png')
    plt.show()


if __name__ == '__main__':
    main()

