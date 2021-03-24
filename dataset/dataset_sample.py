# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# 2/3/21


def take_sample(dataset, ratio):
    if ratio >= 1:
        raise Exception("ratio =" + str(ratio) + " must small than 1")
    return dataset.take(int(len(dataset) * ratio))
