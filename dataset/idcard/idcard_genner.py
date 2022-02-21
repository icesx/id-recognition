# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# 3/23/21

import random

import cv2
import numpy as np

from dataset.dataset_genner import DatasetGenn
from define import root
from draw.draw_low import TextDrawer
from model.model_define import ModelDefine


class GenIdCard(DatasetGenn):
    def __init__(self, md: ModelDefine):
        super().__init__(md)
        self._textDrawer = TextDrawer(root + '/fonts/simhei.ttf')

    def __random_text(self):
        text = ''
        for i in range(self._md.charset_len()):
            c = random.choice(self._md.charset())
            text = text + c
        return text

    def __draw_image(self):
        label = self.__random_text()
        img = np.zeros([self._md.image_height(), self._md.image_width(), self._md.image_channels()])
        color_ = (255, 255, 255)
        pos = (0, 0)
        text_size = 21
        image = self._textDrawer.draw_text(img, pos, label, text_size, color_)
        return image, label

    def _gen_dataset(self, _dir, count):
        for _ in range(count):
            image_data, label = self.__draw_image()
            png_ = _dir + label + ".png"
            print(png_)
            cv2.imwrite(png_, image_data)
