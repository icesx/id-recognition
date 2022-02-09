# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import itertools
import os
import random
import shutil

from captcha.image import ImageCaptcha

from dataset.dataset_genner import DatasetGenn
from model.model_define import ModelDefine, CaptchaModelDefine


class GenCaptcha(DatasetGenn):
    def __init__(self, md: ModelDefine):
        self._md = md

    def _gen_dataset(self, _dir, count):
        choices = list(itertools.permutations(self._md.charset(), self._md.label_len()))
        self.__gen_captcha(_dir, choices=choices,
                           max_images_count=count)

    def __gen_captcha(self, img_dir, choices, max_images_count):
        image = ImageCaptcha(width=self._md.image_width(), height=self._md.image_height())
        samples = random.sample(choices, max_images_count)
        for i in samples:
            captcha = ''.join(i)
            fn = os.path.join(img_dir, '%s.png' % (captcha))
            print("write %s" % fn)
            image.write(captcha, fn)


if __name__ == '__main__':
    GenCaptcha(CaptchaModelDefine()).gen_dataset("/OTHER/dataset/captcha/train", 10)
