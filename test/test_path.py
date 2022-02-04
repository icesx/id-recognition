# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import pathlib

if __name__ == '__main__':
    root_path="/OTHER/dataset/id_card/train"
    root_path = pathlib.Path(root_path)
    images = sorted(list(root_path.glob('*')))
    print(images)