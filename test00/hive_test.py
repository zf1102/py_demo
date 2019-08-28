"""
    作者：zf
    功能：
    版本：1.0
    日期：20190211
    新增功能：
"""
from impala.dbapi import connect


def main():
    """
        主函数
    """
    # \U表示其后是UNICODE编码
    # 必须设置auth_mechanism参数，与 hive-site.xml 配置文件中 hive.server2.authentication 配置项的值一致
    # PLAIN 代表不启用认证，也就是 hive.server2.authentication 的默认值：NONE。
    conn = connect(host='192.168.1.84', port=10000, auth_mechanism='PLAIN', database='imp', user='hadoop')
    cur = conn.cursor()

    cur.execute('SHOW DATABASES')
    print(cur.fetchall())
    """
        a = "SELECT SUM(f_virtual_gained_asset) as `购物玛瑙币返还总量` FROM t_user_virtual_asset_gained_detail WHERE f_fromtype = 1" \
            " AND f_activity_id = 'ACT0001' AND f_create_time >= '2019-01-01' AND f_create_time <  '2019-02-01'"
        sql = a
        cur.execute(sql)
        x = cur.fetchall()
        # 要写入文件的地址
        file = open(r'C:\\Users\Administrator\Desktop\123.txt', 'a+', encoding='utf-8')
        for i in x:
            print(i)
            # file.write(str(i[0])+"\n")
        # 关闭打开文件
        file.close()
    """
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()


