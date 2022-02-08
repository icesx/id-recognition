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


class IdModelDefine(ModelDefine):
    IMAGE_HEIGHT = 32
    IMAGE_WIDTH = 256
    IMAGE_CHANNELS = 3
    CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    CHAR_SET_LEN = len(CHAR_SET)
    LABEL_LEN = 18
    LABEL_SPACE_LEN = 10
    DATASET_PATH = "/OTHER/dataset/id_card/"

    def image_height(self):
        return self.IMAGE_HEIGHT

    def image_width(self):
        return self.IMAGE_WIDTH

    def train_path(self):
        return self.DATASET_PATH + "train/"

    def val_path(self):
        return self.DATASET_PATH + "val/"

    def test_path(self):
        return self.DATASET_PATH + "test/"

    def steps_per_epoch(self):
        return 100

    def epochs(self):
        return 3

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def name(self):
        return "id"

    def image_channels(self):
        return self.IMAGE_CHANNELS

    def label_len(self):
        return self.LABEL_LEN

    def charset_len(self):
        return self.CHAR_SET_LEN

    def label_space_len(self):
        return self.LABEL_SPACE_LEN

    def charset(self):
        return self.CHAR_SET

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(int(i), self.label_space_len())) for i in list(label_str)]


class CaptchaModelDefine(ModelDefine):
    IMAGE_CHANNELS = 3
    choices = [
        list(string.digits),
        list(string.ascii_lowercase),
        list(string.ascii_uppercase),
    ]
    CHAR_SET = sum(choices, [])
    CHAR_SET_LEN = len(CHAR_SET)
    LABEL_LEN = 4
    LABEL_SPACE_LEN = 256
    IMAGE_WIDTH = 40 + 20 * LABEL_LEN
    IMAGE_HEIGHT = 100
    DATASET_PATH = "/OTHER/dataset/captcha/"

    def image_height(self):
        return self.IMAGE_HEIGHT

    def image_width(self):
        return self.IMAGE_WIDTH

    def train_path(self):
        return self.DATASET_PATH + "train/"

    def val_path(self):
        return self.DATASET_PATH + "val/"

    def test_path(self):
        return self.DATASET_PATH + "test/"

    def steps_per_epoch(self):
        return 100

    def epochs(self):
        return 3

    def val_batch(self):
        return 10

    def train_batch(self):
        return 100

    def name(self):
        return "captcha"

    def image_channels(self):
        return self.IMAGE_CHANNELS

    def label_len(self):
        return self.LABEL_LEN

    def charset_len(self):
        return self.CHAR_SET_LEN

    def label_space_len(self):
        return self.LABEL_SPACE_LEN

    def charset(self):
        return self.CHAR_SET

    def char_list_vector(self, label_str):
        return [np.array(to_categorical(ord(i), self.label_space_len())) for i in list(label_str)]
