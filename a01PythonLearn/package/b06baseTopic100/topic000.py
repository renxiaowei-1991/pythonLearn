
import file

base_path="D:\\02helloWorld\\03Python\\a01pythonLearn\\package\\b06baseTopic100\\"

for i in range(51, 101, 1):
    try:
        file01 = open(base_path + "topic" + str(i).rjust(3, "0") + ".py", "w+")
    except BaseException as be:
        print("报错：{ex}".format(ex=be))
    else:
        print("文件创建成功！")
    finally:
        if not file01.closed:
            file01.close()

