# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# 3/24/21
import matplotlib.pyplot as plt


def imange_show(train_images, train_labels):
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(train_labels[i])
    plt.show()


def imange_show_single(image, lable):
    plt.figure(figsize=(10, 10))
    plt.subplot(5, 5, 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(image, cmap=plt.cm.binary)
    plt.xlabel(lable)
    plt.show()
