# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import tensorflow as tf
from tensorflow import keras

from define import IMAGE_WIDTH, IMAGE_HEIGHT, ID_LEN, CHAR_SET_LEN, IMAGE_CHANNELS
from utils import tf_board
from utils.gpu_init import gpu_init


def run_model(train_ds, val_ds, epochs, steps_per_epoch):
    gpu_init()
    _model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (1, 1), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dense(ID_LEN * CHAR_SET_LEN, activation="softmax"),
        keras.layers.Reshape([ID_LEN, CHAR_SET_LEN]),
    ])
    _model.compile(optimizer="adam",
                   loss="categorical_crossentropy",
                   metrics=['accuracy'])
    _model.summary()
    _model.fit(train_ds,
               epochs=epochs,
               steps_per_epoch=steps_per_epoch,
               validation_steps=steps_per_epoch,
               validation_data=val_ds,
               callbacks=[tf_board.tb.tf_board_instance("id-recognition")]
               )
    return _model


def save_model(_model, export_dir):
    print("save model ", _model, "to dir ", export_dir, "..")
    tf.saved_model.save(_model, export_dir=export_dir)
    print("saved")
