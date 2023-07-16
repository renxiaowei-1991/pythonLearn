import file

def check_user_name(user_name):
    user_file = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\p077_users.txt"
    rs: bool = False
    if len(user_name) <= 6:
        print("长度小于6位，请重新输入")
        return rs

    user_list = []
    with open(user_file, "r+", encoding="utf-8") as f:
        try:
            for user in f.readlines():
                # 去除字符串头尾的指定字符串，默认是空格和换行，否则会匹配错误
                user_list.append(user.strip())
        except BaseException as be:
            print(f"异常 {be}")

    print(user_list)
    # 和上面的检测分开是因为如果长度都不够，就不用进行下面的检测了
    if user_name in user_list:
        print("用户名已存在，请重新输入")
        return rs
    else:
        print("用户名检测通过")
        with open(user_file, "a+", encoding="utf-8") as f:
            try:
                f.write("\n" + user_name)
                print("新用户名已保存")
            except BaseException as be:
                print(f"写入异常， {be}")
        return True



while True:
    if check_user_name(input("请输入用户名: ")):
        break
