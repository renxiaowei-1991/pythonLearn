import random
import string


def random_get_passwd(passwd_len: int):
    """
    随机密码生成器
    :param passwd_len: 指定随机生成的密码的长度
    :return: 返回字符串密码
    """
    passwd_char = ""
    # 小写字母字符串
    # print(string.ascii_lowercase)
    # 大写字母字符串
    # print(string.ascii_uppercase)
    # 数字字符串
    # print(string.digits)
    # 标点符号字符串
    # print(string.punctuation)

    # 密码基数列表，密码字符选择的基础
    passwd_char = passwd_char + \
                  string.ascii_lowercase + \
                  string.ascii_uppercase + \
                  string.digits + \
                  string.punctuation
    # random.sample: 从字符串中随机选取指定位数的字符的列表
    return "".join(random.sample(passwd_char, passwd_len))


print(random_get_passwd(20))
