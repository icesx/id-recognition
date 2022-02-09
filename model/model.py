# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import tensorflow as tf
from tensorflow import keras

from model.model_define import ModelDefine
from utils import tf_board
from utils.gpu_init import gpu_init


def run_model(train_ds, val_ds, md: ModelDefine):
    gpu_init()
    _model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu",
                            input_shape=(md.image_height(), md.image_width(), md.image_channels())),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (1, 1), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dense(md.label_len() * md.label_space_len(), activation="softmax"),
        keras.layers.Reshape([md.label_len(), md.label_space_len()]),
    ])
    _model.compile(optimizer="adam",
                   loss="categorical_crossentropy",
                   metrics=['accuracy'])
    _model.summary()
    _model.fit(train_ds,
               epochs=md.epochs(),
               steps_per_epoch=md.steps_per_epoch(),
               validation_steps=md.steps_per_epoch(),
               validation_data=val_ds,
               callbacks=[tf_board.tb.tf_board_instance(md.name())]
               )
    return _model


def save_model(_model, export_dir):
    print("save model ", _model, "to dir ", export_dir)
    tf.saved_model.save(_model, export_dir=export_dir)
    print("saved")
