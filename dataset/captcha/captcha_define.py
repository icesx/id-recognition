# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import string

import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

from model.model_define import ModelDefine

__CHAR_SET_OR = [
    # list(string.digits),
    list(string.ascii_lowercase),
    list(string.ascii_uppercase),
]
_IMAGE_CHANNELS = 3
_CHAR_SET = sum(__CHAR_SET_OR, [])
_LABEL_LEN = 4
_LABEL_SPACE_LEN = 256
_IMAGE_WIDTH = 40 + 20 * _LABEL_LEN
_IMAGE_HEIGHT = 100
_DATASET_PATH = "/OTHER/dataset/captcha/"


class CaptchaModelDefine(ModelDefine):

    def __init__(self):
        super().__init__("captcha",
                         dataset_path=_DATASET_PATH,
                         image_width=_IMAGE_WIDTH,
                         image_height=_IMAGE_HEIGHT,
                         image_channels=_IMAGE_CHANNELS,
                         charset=_CHAR_SET,
                         label_len=_LABEL_LEN,
                         label_space_len=_LABEL_SPACE_LEN)

    def steps_per_epoch(self):
        return 300

    def epochs(self):
        return 20

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(ord(i), self.label_space_len())) for i in list(label_str)]

    def format_y(self, label_vector):
        return ''.join(map(lambda x: chr(x), label_vector))
