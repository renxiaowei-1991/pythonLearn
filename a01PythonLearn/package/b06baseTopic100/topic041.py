import math

# 求球的体积
def get_volume(r=10):
    # r ** 3(r的三次方)
    volume = 4/3 * math.pi * r ** 3
    return volume


# 求球的面积
def get_area(r=10):
    # r ** 2(r的二次方)
    area = 4 * math.pi * r ** 2
    return area


r = 2
print(f"半径为 {r} 的球的体积为：", get_volume(r))
print(f"半径为 {r} 的球的面积为：", get_area(r))
