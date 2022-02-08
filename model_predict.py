# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import tensorflow as tf
from tensorflow import keras

from define import IMAGE_WIDTH, IMAGE_HEIGHT, DATASET_PATH
from model.predict import predict

if __name__ == '__main__':
    export_dir = "./save/model"
    model = keras.models.load_model(export_dir)
    label_predict = predict(model, DATASET_PATH + "test" + "/990196488967963319.png", IMAGE_HEIGHT, IMAGE_WIDTH)
    label_predict = tf.math.argmax(label_predict, axis=-1)
    print(str(label_predict))
