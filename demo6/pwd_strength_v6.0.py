"""
    作者：zf
    功能：判断密码强度
    版本：6.0
    日期：20181024
    新增功能：将文件操作封装成类，面向对象编程
"""


class PwdTool:
    """
        密码工具类
    """
    def __init__(self, pwd_str):
        self.pwd_str = pwd_str
        self.strength_level = 0

    def pwd_rule(self):
        # 规则1、密码长度 >= 8
        if len(self.pwd_str) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')
        # 规则2、密码包含数字
        if self.number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')
        # 规则3、密码包含字母
        if self.letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    def number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False
        for c in self.pwd_str:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def letter_exist(self):
        """
            判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.pwd_str:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    try_times = 5
    filepath = 'password_6.0.txt'
    # 实例化文件工具类
    file_tool = FileTool(filepath)

    while try_times > 0:

        password = input('请输入密码：')
        # 实例化对象
        pwd_tool = PwdTool(password)
        pwd_tool.pwd_rule()

        # 写文件
        line = '密码：{}, 强度：{}\n'.format(password, pwd_tool.strength_level)
        file_tool.write_file(line)

        if pwd_tool.strength_level == 3:
            print('恭喜，密码强度合格！')
            break
        else:
            try_times -= 1
            print('密码强度不合格！')
    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    # 读文件
    lines = file_tool.read_file()
    print(lines)


if __name__ == '__main__':
    main()

