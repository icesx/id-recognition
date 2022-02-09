# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import tensorflow as tf
from tensorflow import keras

from model.model_define import IdModelDefine
from model.predict import predict

if __name__ == '__main__':
    md = IdModelDefine()
    export_dir = md.save_path()
    model = keras.models.load_model(export_dir)
    label_predict = predict(model, md.test_path() + "/990196488967963319.png", md)
    label_predict = tf.math.argmax(label_predict, axis=-1)
    print(str(label_predict))
