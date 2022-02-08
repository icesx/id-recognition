# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import pathlib
import random

import tensorflow as tf

from dataset.label_vector import LabelVector
from define import IMAGE_CHANNELS


class ImageInfo:

    def __init__(self, path):
        self.__path = pathlib.Path(path)
        lv = LabelVector(self.__detect_label())
        self.__label_vector = lv.vector
        self.__label = lv.label

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


def __image_paths(root) -> [ImageInfo]:
    root_path = pathlib.Path(root)
    images = sorted(list(root_path.glob('*')))
    image_infos = [ImageInfo(path) for path in images]
    random.shuffle(image_infos)
    print("First 10 image_infos: ", image_infos[:10])
    return image_infos


def image_labels(root: object) -> [ImageInfo]:
    root_path = pathlib.Path(root)
    image_infos = __image_paths(root_path)
    print("First 1 images: ", image_infos[:1])
    print("First 1 labels indices: ", [i.label_vector for i in image_infos[:1]])
    return image_infos


def image_byte_array(path, height, width):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=IMAGE_CHANNELS)
    image = tf.image.resize(image, [height, width])
    image /= 255.0
    return image
