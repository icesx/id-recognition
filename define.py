# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from pathlib import Path

def work_dir():
    return str(Path(__file__).parent)


root = work_dir()
