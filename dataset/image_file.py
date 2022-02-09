# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import pathlib
import random

import tensorflow as tf

from model.model_define import ModelDefine


class ImageInfo:

    def __init__(self, path, md: ModelDefine):
        self.__path = pathlib.Path(path)
        self.__label = self.__detect_label()
        self.__label_vector = md.char_list_vector(self.__label)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__path) + "->" + str(self.__label)

    @property
    def path_str(self):
        return str(self.__path)

    @property
    def path(self):
        return self.__path

    @property
    def label_vector(self):
        return self.__label_vector

    def __detect_label(self):
        return self.__path.name.split(".")[0]


def __image_paths(root, md: ModelDefine) -> [ImageInfo]:
    root_path = pathlib.Path(root)
    images = sorted(list(root_path.glob('*')))
    image_infos = [ImageInfo(path, md) for path in images]
    random.shuffle(image_infos)
    print("First 10 image_infos: ", image_infos[:10])
    return image_infos


def image_labels(root: str, md: ModelDefine) -> [ImageInfo]:
    root_path = pathlib.Path(root)
    image_infos = __image_paths(root_path, md)
    print("First 1 images: ", image_infos[:1])
    print("First 1 labels indices: ", [i.label_vector for i in image_infos[:1]])
    return image_infos


def image_byte_array(path, md: ModelDefine):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=md.image_channels())
    image = tf.image.resize(image, [md.image_height(), md.image_width()])
    image /= 255.0
    return image
