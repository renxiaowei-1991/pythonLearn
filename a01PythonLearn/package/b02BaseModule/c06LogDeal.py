#!/usr/bin/env pytnon
# -*- coding:utf-8 -*-

import file


class LogDeal:
    def __init__(self):
        self.def_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\log\\"
        self.def_file = "log01.log"

    def write_log(self, log):
        try:
            log01 = open(self.def_path + self.def_file, 'a+', encoding='utf-8')
            log01.write(log + "\n")
        except IOError:
            print("写日志IO异常！")
        else:
            print("日志写入成功！")
        finally:
            if not log01.closed:
                log01.close()
