# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

from model.model_define import ModelDefine

_IMAGE_HEIGHT = 32
_IMAGE_WIDTH = 256
_IMAGE_CHANNELS = 3
_CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
_LABEL_LEN = 18
_LABEL_SPACE_LEN = 10
_DATASET_PATH = "/OTHER/dataset/id_card/"


class IdModelDefine(ModelDefine):

    def __init__(self):
        super().__init__("id",
                         dataset_path=_DATASET_PATH,
                         image_width=_IMAGE_WIDTH,
                         image_height=_IMAGE_HEIGHT,
                         image_channels=_IMAGE_CHANNELS,
                         charset=_CHAR_SET,
                         label_len=_LABEL_LEN,
                         label_space_len=_LABEL_SPACE_LEN)


    def steps_per_epoch(self):
        return 100

    def epochs(self):
        return 5

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(int(i), self.label_space_len())) for i in list(label_str)]

    def format_y(self, label_vector):
        return ''.join(map(lambda x: str(x), label_vector))
