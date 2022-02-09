# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical


def test_label():
    label = list("123456789")
    N_LABELS = 256
    print(label)
    label_vector = [np.array(to_categorical(ord(i), N_LABELS)) for i in label]
    print(label_vector)
    print("-----------------")
    label_vector = [np.array(to_categorical(int(i), 10)) for i in label]
    print(label_vector)


if __name__ == '__main__':
    test_label()
