# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import matplotlib.pyplot as plt


def plot_show(image):
    plt.figure()
    plt.imshow(image)
    plt.colorbar()
    plt.show()


def plot_shows(images, image_labels=None, figsize=(10, 10)):
    plt.figure(figsize=figsize)
    for i in range(len(images)):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(image_labels[i])
    plt.show()
