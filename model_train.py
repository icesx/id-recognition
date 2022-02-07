# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import tensorflow as tf
from tensorflow import keras

from dataset.create_dataset import DatasetCreator
from dataset.dataset_sample import take_sample
from define import IMAGE_WIDTH, IMAGE_HEIGHT, MAX_CAPTCHA, CHAR_SET_LEN, IMAGE_CHANNELS
from predict import predict
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
        keras.layers.Dense(MAX_CAPTCHA * CHAR_SET_LEN, activation="softmax"),
        keras.layers.Reshape([MAX_CAPTCHA, CHAR_SET_LEN]),
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


if __name__ == '__main__':
    creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    val_creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    # dataset_path = "/OTHER/dataset/captcha/char-4-epoch-4/"
    dataset_path = "/OTHER/dataset/id_card/"
    _train_ds = creator.load(dataset_path + "train/").shuffle_and_repeat().batch(100)
    _val_ds = val_creator.load(dataset_path + "val/").shuffle_and_repeat().batch(10)
    model = run_model(_train_ds, _val_ds, epochs=3, steps_per_epoch=100)
    # save_model(model,"./save/model")
    test_creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    _test_ds = test_creator.load(dataset_path + "val/")
    predict(model, _test_ds.base_ds())
