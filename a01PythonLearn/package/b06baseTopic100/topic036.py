
def acceleration_speed(v1, v2, t1, t2):
    """
    加速度函数
    """
    try:
        speed = (v2 - v1)/(t2 - t1)
    except BaseException as be:
        print(f"计算加速度异常：{be}")
    else:
        print(f"开始时间: {t1}, 结束时间: {t2}, 起始速度: {v1}, 结束速度: {v2}, 加速度是：{speed}")
        return speed


if __name__ == "__main__":
    print(acceleration_speed(0, 10, 0, 20))
