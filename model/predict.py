# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

from dataset.image_file import image_byte_array


def _format_y(y):
    return ''.join(map(lambda x: str(x), y))


def predict(model, img_path, image_height, image_width):
    return model.predict(np.expand_dims(image_byte_array(img_path, image_height, image_width), axis=0))


def predict_plt(model, ds):
    batch = 5
    take_time = 6
    '''
    take 6 time per 5 number
    '''
    ds = ds.batch(batch).take(take_time)
    fig, axes = plt.subplots(take_time, batch, figsize=(30, 20))
    _index = 0
    for element in ds.as_numpy_iterator():
        images = element[0]
        label = element[1]
        label_predict = model.predict_on_batch(images)
        label_true = tf.math.argmax(label, axis=-1)
        label_predict = tf.math.argmax(label_predict, axis=-1)
        for (lts, lps, img) in zip(label_true, label_predict, images):
            print("true:%s->predict:%s" % (lts, lps))
            ax = axes.flat[_index]
            ax.imshow(img)
            lps_str = _format_y(lps.numpy())
            lts_str = _format_y(lts.numpy())
            ax.set_title('predict: %s [%s]' % (lps_str, (lts_str is lts_str)))
            ax.set_xlabel('label: %s' % lts_str)
            ax.set_xticks([])
            ax.set_yticks([])
            _index += 1
    plt.show()
