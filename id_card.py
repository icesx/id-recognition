# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import tensorflow as tf
from tensorflow import keras

from gen import *
from gpu_init import gpu_init
IMAGE_HEIGHT = 32
IMAGE_WIDTH = 256
MAX_CAPTCHA = 10
CHAR_SET_LEN = 18


# 生成一个训练batch
def get_next_batch(batch_size=1000):
    obj = gen_id_card()
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, 3])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA * CHAR_SET_LEN])

    for i in range(batch_size):
        image, text, vec = obj.gen_image()
        batch_x[i, :] = image
        batch_y[i, :] = vec
    return batch_x, batch_y


def load_mnist(batch_size=1000):
    train_images, train_labels = get_next_batch(batch_size)
    print(train_images.shape, len(train_images))
    print(train_labels.shape, len(train_labels))
    return train_images, train_labels


def run_module(train_images, train_lables):
    gpu_init()
    module = keras.Sequential([
        keras.layers.Conv2D(120, (2, 2), activation="relu", input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (2, 2), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (2, 2), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(180),
        keras.layers.Reshape([10,18]),
        keras.layers.Softmax()
    ])
    module.compile(optimizer="adam",
                   loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                   metrics=['accuracy'])
    module.summary()
    module.fit(train_images, train_lables, epochs=5, batch_size=128)
    return module


def predict(module, test_images, test_lables):
    predic_module = keras.Sequential([module, keras.layers.Softmax()])
    prediced = predic_module.predict(test_images)
    print(test_lables[0], tf.argmax(prediced[0]))


def evaluate(module, test_images, test_lables):
    test_loss, test_acc = module.evaluate(test_images, test_labels, verbose=2)
    print("testloss=", test_loss, "test_acc=", test_acc)


def save_module(module, export_dir):
    print("save module ", module, "to dir ", export_dir, "..")
    tf.saved_model.save(module, export_dir=export_dir)
    print("saved")


if __name__ == '__main__':
    train_images, train_labels = load_mnist()
    test_images, test_labels = load_mnist(batch_size=100)
    module = run_module(train_images, train_labels)
    evaluate(module, test_images, test_labels)
    predict(module, test_images, test_labels)
    save_module(module)
