# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

from define import ID_LEN, CHAR_SET, CHAR_SET_LEN


class LabelVector:
    def __init__(self, label_str):
        self.__label_str = label_str
        if len(label_str) != ID_LEN:
            with__format = "the label_str len({})!= {}".format(label_str, ID_LEN)
            print(with__format)
            raise Exception(with__format)
        self.__label_vector = self.__char_list_vector()

    @property
    def label(self):
        return self.__label_str

    @property
    def vector(self):
        return self.__label_vector

    def __char_list_vector(self):
        return [np.array(to_categorical(int(i), CHAR_SET_LEN)) for i in list(self.__label_str)]

    @staticmethod
    def __char2vec(c):
        vector = np.zeros(CHAR_SET_LEN)
        for j in range(CHAR_SET_LEN):
            if CHAR_SET[j] == c:
                vector[j] = 1
        return vector


if __name__ == '__main__':
    lv = LabelVector("610123198301084512")
    print(list(lv.label))
    print(lv.vector)
    lv2 = LabelVector("610233940505040400")
    print(lv2.vector)
