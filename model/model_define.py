# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import string

import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

SAVE_MODEL_ = "./save/model/"


class ModelDefine:

    def __init__(self):
        pass

    def image_height(self):
        pass

    def image_width(self):
        pass

    def train_path(self):
        pass

    def val_path(self):
        pass

    def test_path(self):
        pass

    def steps_per_epoch(self):
        pass

    def epochs(self):
        pass

    def val_batch(self):
        pass

    def train_batch(self):
        pass

    def name(self):
        pass

    def image_channels(self):
        pass

    def label_len(self):
        pass

    def charset_len(self):
        pass

    def charset(self):
        pass

    def save_path(self):
        return SAVE_MODEL_ + self.name()

    def char_list_vector(self, label_str):
        pass

    def label_space_len(self):
        pass

    def format_y(self, label_vector):
        pass


class IdModelDefine(ModelDefine):
    __IMAGE_HEIGHT = 32
    __IMAGE_WIDTH = 256
    __IMAGE_CHANNELS = 3
    __CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    __CHAR_SET_LEN = len(__CHAR_SET)
    __LABEL_LEN = 18
    __LABEL_SPACE_LEN = 10
    __DATASET_PATH = "/OTHER/dataset/id_card/"

    def image_height(self):
        return self.__IMAGE_HEIGHT

    def image_width(self):
        return self.__IMAGE_WIDTH

    def train_path(self):
        return self.__DATASET_PATH + "train/"

    def val_path(self):
        return self.__DATASET_PATH + "val/"

    def test_path(self):
        return self.__DATASET_PATH + "test/"

    def steps_per_epoch(self):
        return 100

    def epochs(self):
        return 5

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def name(self):
        return "id"

    def image_channels(self):
        return self.__IMAGE_CHANNELS

    def label_len(self):
        return self.__LABEL_LEN

    def charset_len(self):
        return self.__CHAR_SET_LEN

    def label_space_len(self):
        return self.__LABEL_SPACE_LEN

    def charset(self):
        return self.__CHAR_SET

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(int(i), self.label_space_len())) for i in list(label_str)]

    def format_y(self, label_vector):
        return ''.join(map(lambda x: str(x), label_vector))


class CaptchaModelDefine(ModelDefine):
    __CHAR_SET_OR = [
        list(string.digits),
        list(string.ascii_lowercase),
        list(string.ascii_uppercase),
    ]
    __IMAGE_CHANNELS = 3
    __CHAR_SET = sum(__CHAR_SET_OR, [])
    __CHAR_SET_LEN = len(__CHAR_SET)
    __LABEL_LEN = 4
    __LABEL_SPACE_LEN = 256
    __IMAGE_WIDTH = 40 + 20 * __LABEL_LEN
    __IMAGE_HEIGHT = 100
    __DATASET_PATH = "/OTHER/dataset/captcha/"

    def image_height(self):
        return self.__IMAGE_HEIGHT

    def image_width(self):
        return self.__IMAGE_WIDTH

    def train_path(self):
        return self.__DATASET_PATH + "train/"

    def val_path(self):
        return self.__DATASET_PATH + "val/"

    def test_path(self):
        return self.__DATASET_PATH + "test/"

    def steps_per_epoch(self):
        return 100

    def epochs(self):
        return 20

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def name(self):
        return "captcha"

    def image_channels(self):
        return self.__IMAGE_CHANNELS

    def label_len(self):
        return self.__LABEL_LEN

    def charset_len(self):
        return self.__CHAR_SET_LEN

    def label_space_len(self):
        return self.__LABEL_SPACE_LEN

    def charset(self):
        return self.__CHAR_SET

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(ord(i), self.label_space_len())) for i in list(label_str)]

    def format_y(self, label_vector):
        return ''.join(map(lambda x: chr(x), label_vector))
