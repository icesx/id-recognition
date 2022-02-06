# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import tensorflow as tf
from tensorflow import keras

from dataset.create_dataset import DatasetCreator
from define import IMAGE_WIDTH, IMAGE_HEIGHT, MAX_CAPTCHA, CHAR_SET_LEN
from utils import tf_board
from utils.gpu_init import gpu_init


def run_model(train_ds, val_ds, epochs, steps_per_epoch):
    gpu_init()
    _model = keras.Sequential([
        keras.layers.Conv2D(32, (2, 2), activation="relu", input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (2, 2), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(128, (2, 2), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (1, 1), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(MAX_CAPTCHA * CHAR_SET_LEN, activation="softmax"),
        # keras.layers.Reshape([10, 18]),
        # keras.layers.Flatten(),
        keras.layers.Softmax()
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


def predict(_model, test_images, test_labels):
    predict_model = keras.Sequential([_model, keras.layers.Softmax()])
    predicted = predict_model.predict(test_images)
    print(test_labels[0], tf.argmax(predicted[0]))


def save_model(_model, export_dir):
    print("save model ", _model, "to dir ", export_dir, "..")
    tf.saved_model.save(_model, export_dir=export_dir)
    print("saved")


if __name__ == '__main__':
    creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    val_creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    _train_ds = creator.load("/OTHER/dataset/id_card/train/").shuffle_and_repeat().batch(1000)
    _val_ds = creator.load("/OTHER/dataset/id_card/val/").shuffle_and_repeat().batch(10)
    model = run_model(_train_ds, _val_ds, epochs=100, steps_per_epoch=100)
    # save_module(module)
