#!/usr/bin/env python
# -*- coding:utf-8 -*-

import win32com.client
import pygame
import pyttsx3
import sys
import this

"""
win32com
    微软语音接口，用于测试系统接口
    win32com.client.Dispatch
        调用系统语音
        文字转语音
pyttsx3
    python语音接口
"""

def win32VoiceFun(voiceList):
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    while True:
        speaker.Speak(",".join(voiceList))

"""
读文件
背景音乐
封面照片
"""
def pygamePyttsx3():
    # pygame开始
    pygame.init()  # 初始化
    pygame.mixer.init()
    music_name = "E:\\07-python\\07-projectList\\a01PythonLearn\\file\\a08PythonPro\\龙的传人.mp3"
    music_name = music_name.encode('utf-8')  # 歌曲中文字体转换

    pygame.mixer.music.load(music_name)  # 加载歌曲
    pygame.mixer.music.play()  # 播放

    screen = pygame.display.set_mode([500, 646])  # 界面大小
    pygame.mixer.music.set_volume(0.2)  # 声音设置

    img = pygame.image.load("E:\\07-python\\07-projectList\\a01PythonLearn\\file\\a08PythonPro\\龙的传人.jpg")  # 界面封面
    screen.blit(img, (0, 0))
    pygame.display.update()
    # pygame结束

    # pyttsx3开始
    with open("E:\\07-python\\07-projectList\\a01PythonLearn\\file\\a08PythonPro\\龙的传人.txt", "r",
              encoding="utf-8") as f:
        msg_list = f.readlines()  # 把字符串转换成列表
    engine = pyttsx3.init()  # 驱动初始化

    # 调整评率
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    # 调整音量
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 2)
    engine = pyttsx3.init()
    for k in range(2):
        for each in msg_list:
            engine.say(each)
    engine.runAndWait()
    # 设置打开界面的关闭方法，没有的话打开的界面没法关闭
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    # pyttsx3结束

if __name__ == '__main__':
    voiceList = [
        "臭宝，你个大坏蛋，就知道看电视剧，嗷嗷嗷",
        "啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        "啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        "啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        "啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
    ]
    win32VoiceFun(voiceList)
    #pygamePyttsx3()
    #y = (lambda x: x ** 2 + x * 5 - x)(-4)
    #print(y)





