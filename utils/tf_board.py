# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import datetime

import tensorflow as tf


class __tensor_boader_single():
    def __init__(self):
        self.__tensor_board = None

    def tf_board_instance(self, name):
        if name is None:
            raise Exception(f"the name of model is {name}")
        log_dir = "./tmp/logs/tb/" + name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        if self.__tensor_board is None:
            print("created TensorBoard")
            self.__tensor_board = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0, profile_batch=0)
        return self.__tensor_board


tb = __tensor_boader_single()
