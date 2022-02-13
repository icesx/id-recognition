# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import cv2
import numpy as np

from define import root
from draw.draw_low import TextDrawer


def draw():
    print(root)
    _textDrawer = TextDrawer(root + '/fonts/simhei.ttf')
    img = np.zeros([100, 100, 3])
    color_ = (255, 255, 255)
    pos = (0, 0)
    text_size = 21
    image = _textDrawer.draw_text(img, pos, "中华1A", text_size, color_)
    cv2.imwrite(root + "/tmp/zhrmghg.png", image)


if __name__ == '__main__':
    draw()
