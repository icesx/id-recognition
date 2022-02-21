# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import os
import random

from dataset.dataset_genner import DatasetGenn
from define import root
from draw.draw_pillow import create_image, draw_text, noise, save_image
from model.model_define import ModelDefine


class EartagWrite():
    def __init__(self, image_width, image_height):
        self.__image_width = image_width
        self.__image_height = image_height
        self.__font_path = root + "/fonts/simhei.ttf"

    def write(self, label, label2, path):
        img_bg = create_image(size=(200, 200), color=(255, 255, 255))
        img = draw_text(img_bg, self.__font_path, label, rotate=96, position=(10, 10))
        img = draw_text(img, self.__font_path, label2, rotate=0, position=(30, 10))
        noise(img, 200, 200, 10, 100)
        save_image(img, path)


class GenEartag(DatasetGenn):
    def __init__(self, md: ModelDefine):
        super().__init__(md)

    def _gen_dataset(self, _dir, count):
        choices = [random.sample(self._md.charset() + self._md.charset(), self._md.label_len()) for i in range(count)]
        self.__gen_captcha(_dir, choices=choices,
                           max_images_count=count)

    def __gen_captcha(self, img_dir, choices, max_images_count):
        write = EartagWrite(self._md.image_width(), self._md.image_height())
        samples = random.sample(choices, max_images_count)
        for i in samples:
            label = ''.join(i)
            file_path = os.path.join(img_dir, '%s.png' % label)
            print("write %s" % file_path)
            write.write(label[:7], label[7:], file_path)
