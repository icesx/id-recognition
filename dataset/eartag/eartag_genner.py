# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import itertools
import os
from random import random

from dataset.dataset_genner import DatasetGenn
from model.model_define import ModelDefine


class EartagWrite():
    def __init__(self, image_width, image_height):
        pass


class GenEartag(DatasetGenn):
    def __init__(self, md: ModelDefine):
        super(md)

    def _gen_dataset(self, _dir, count):
        choices = list(itertools.permutations(self._md.charset(), self._md.label_len()))
        self.__gen_captcha(_dir, choices=choices,
                           max_images_count=count)

    def __gen_captcha(self, img_dir, choices, max_images_count):
        image = EartagWrite(width=self._md.image_width(), height=self._md.image_height())
        samples = random.sample(choices, max_images_count)
        for i in samples:
            captcha = ''.join(i)
            fn = os.path.join(img_dir, '%s.png' % (captcha))
            print("write %s" % fn)
            image.write(captcha, fn)
