# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

from model.model_define import ModelDefine


class LabelVector:
    pass
    # def __init__(self, label_str, md: ModelDefine):
    #     self.__label_str = label_str
    #     self.__md = md
    #     if len(label_str) != md.label_len():
    #         with__format = "the label_str len({})!= {}".format(label_str, md.label_len())
    #         print(with__format)
    #         raise Exception(with__format)
    #     self.__label_vector = md.char_list_vector()
    #
    # @property
    # def label(self):
    #     return self.__label_str
    #
    # @property
    # def vector(self):
    #     return self.__label_vector


if __name__ == '__main__':
    lv = LabelVector("610123198301084512")
    print(list(lv.label))
    print(lv.vector)
    lv2 = LabelVector("610233940505040400")
    print(lv2.vector)
