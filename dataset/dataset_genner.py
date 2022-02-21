# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import os
import shutil

from model.model_define import ModelDefine


class DatasetGenn(object):
    def __init__(self, md: ModelDefine):
        self._md = md

    def gen_train(self, count):
        self.__gen_images(self._md.train_path(), count)

    def gen_val(self, count):
        self.__gen_images(self._md.val_path(), count)

    def gen_test(self, count):
        self.__gen_images(self._md.test_path(), count)

    def __gen_images(self, img_dir, count):
        if os.path.exists(img_dir):
            shutil.rmtree(img_dir)
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        print("TO delete dataset dir %s" % img_dir)
        self._gen_dataset(img_dir, count)

    def _gen_dataset(self, img_dir, count):
        pass
