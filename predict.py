# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import tensorflow as tf
from matplotlib import pyplot as plt


def _format_y(y):
    return ''.join(map(lambda x: str(x), y))


def predict(model, ds):
    batch = 5
    take_number = 6
    ds = ds.batch(batch)
    fig, axes = plt.subplots(take_number, batch, figsize=(30, 20))
    i = 0
    for element in ds.take(take_number).as_numpy_iterator():
        images = element[0]
        label = element[1]
        label_pred = model.predict_on_batch(images)
        label_true = tf.math.argmax(label, axis=-1)
        label_pred = tf.math.argmax(label_pred, axis=-1)
        for (lts, lps, imgs) in zip(label_true, label_pred, images):
            print("true:%s->predict:%s" % (lts, lps))
            ax = axes.flat[i]
            ax.imshow(imgs)
            ax.set_title('pred: %s' % _format_y(lps.numpy()))
            ax.set_xlabel('true: %s' % _format_y(lts.numpy()))
            ax.set_xticks([])
            ax.set_yticks([])
            i += 1
    plt.show()
