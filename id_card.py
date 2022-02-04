# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import tensorflow as tf
from tensorflow import keras

import tf_board
from dataset.create_dataset import DatasetCreator
from gpu_init import gpu_init

IMAGE_HEIGHT = 32
IMAGE_WIDTH = 256
MAX_CAPTCHA = 10
CHAR_SET_LEN = 18


def run_module(train_ds, val_ds, epochs, steps_per_epoch):
    gpu_init()
    module = keras.Sequential([
        keras.layers.Conv2D(32, (2, 2), activation="relu", input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (2, 2), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(128, (2, 2), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(180),
        keras.layers.Reshape([10, 18]),
        keras.layers.Flatten(),
        keras.layers.Softmax()
    ])
    module.compile(optimizer="adam",
                   loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                   metrics=['accuracy'])
    module.summary()
    module.fit(train_ds,
               epochs=epochs,
               steps_per_epoch=steps_per_epoch,
               validation_steps=steps_per_epoch,
               validation_data=val_ds,
               callbacks=[tf_board.tb.tf_board_instance("id-recognition")]
               )
    return module


def predict(module, test_images, test_lables):
    predic_module = keras.Sequential([module, keras.layers.Softmax()])
    prediced = predic_module.predict(test_images)
    print(test_lables[0], tf.argmax(prediced[0]))


def save_module(module, export_dir):
    print("save module ", module, "to dir ", export_dir, "..")
    tf.saved_model.save(module, export_dir=export_dir)
    print("saved")


if __name__ == '__main__':
    creator = DatasetCreator(IMAGE_WIDTH, IMAGE_HEIGHT)
    val_creator = DatasetCreator(IMAGE_WIDTH, IMAGE_HEIGHT)
    _train_ds = creator.load("/OTHER/dataset/id_card/train/").shuffle_and_repeat().batch(50)
    _val_ds = creator.load("/OTHER/dataset/id_card/val/").shuffle_and_repeat().batch(10)
    module = run_module(_train_ds, _val_ds, epochs=100, steps_per_epoch=20)
    # save_module(module)
