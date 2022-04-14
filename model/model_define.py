# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

SAVE_MODEL_ = "./save/model/"


class ModelDefine:

    def __init__(self, name, dataset_path, image_width, image_height, image_channels, charset, label_len,
                 label_space_len):
        self._name = name
        self._DATASET_PATH = dataset_path
        self._IMAGE_HEIGHT = image_width
        self._IMAGE_WIDTH = image_height
        self._IMAGE_CHANNELS = image_channels
        self._CHAR_SET = charset
        self._LABEL_LEN = label_len
        # lable 向量空间长度，如char的向量空间长度为256
        self._LABEL_SPACE_LEN = label_space_len

    def label_len(self):
        return self._LABEL_LEN

    def label_space_len(self):
        return self._LABEL_SPACE_LEN

    def charset(self):
        return self._CHAR_SET

    def charset_len(self):
        return len(self._CHAR_SET)

    def image_height(self):
        return self._IMAGE_HEIGHT

    def image_width(self):
        return self._IMAGE_WIDTH

    def dateset_path(self):
        return self._DATASET_PATH

    def train_path(self):
        return self._DATASET_PATH + "train/"

    def val_path(self):
        return self._DATASET_PATH + "val/"

    def test_path(self):
        return self._DATASET_PATH + "test/"

    def image_channels(self):
        return self._IMAGE_CHANNELS

    def steps_per_epoch(self):
        pass

    def epochs(self):
        pass

    def val_batch(self):
        pass

    def train_batch(self):
        pass

    def name(self):
        return self._name

    def save_path(self):
        return SAVE_MODEL_ + self._name

    def char_list_vector(self, label_str):
        pass

    def format_y(self, label_vector):
        pass
