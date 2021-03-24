# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# 3/24/21
import tensorflow as tf


def gpu_init(memery_mb=6400):
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            tf.config.experimental.set_virtual_device_configuration(gpus[0], [
                tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memery_mb)])
        except RuntimeError as e:
            print(e)
