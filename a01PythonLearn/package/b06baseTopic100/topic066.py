import time

num = 0
while True:
    print("hello")
    num += 1
    if num >= 4:
        print("End of loop")
        break
    time.sleep(num)