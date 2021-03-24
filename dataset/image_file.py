# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import pathlib
import random

import tensorflow as tf

from utils import IDG

ALL_LABELS = dict()


def regist_label(label_name):
    label = ALL_LABELS.get(label_name)
    if label is None:
        label = LabelInfo(label_name, IDG.next_id())
        ALL_LABELS.update({label_name: label})
    return label


class LabelInfo:

    def __init__(self, label_name, label_idx):
        self.__label_name = label_name
        self.__label_idx = label_idx

    def __str__(self):
        return self.__label_name + ":" + str(self.__label_idx)

    def __repr__(self):
        return str(self)

    @property
    def label_name(self):
        return self.__label_name

    @property
    def label_idx(self):
        return self.__label_idx


class ImageInfo:

    def __init__(self, path):
        self.__path = path
        self.__label = regist_label(self.__detect_label())

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
    def label_info(self):
        return self.__label

    def __detect_label(self):
        return self.__path.parent.name


def __image_paths(root_path) -> [ImageInfo]:
    root_path = pathlib.Path(root_path)
    images = sorted(list(root_path.glob('*/*')))
    image_infos = [ImageInfo(path) for path in images]
    random.shuffle(image_infos)
    print("First 10 image_infos: ", image_infos[:10])
    return image_infos


def image_labels(root: object) -> [ImageInfo]:
    root_path = pathlib.Path(root)
    image_infos = __image_paths(root_path)
    print("First 10 images: ", image_infos[:10])
    print("First 10 labels indices: ", [i.label_info for i in image_infos[:10]])
    return image_infos


def image_byte_array(path, image_x, image_y):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [image_x, image_y])
    image /= 255.0
    return image
