# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from pathlib import Path

IMAGE_HEIGHT = 32
IMAGE_WIDTH = 256
CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHAR_SET_LEN = len(CHAR_SET)
MAX_CAPTCHA = 18


def work_dir():
    return str(Path(__file__).parent)


root = work_dir()
