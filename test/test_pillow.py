# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

from PIL import Image

from define import root
from draw.draw_pillow import create_image, draw_text, noise, show_image


def tmp(name):
    return root + "/tmp/" + name;


def white():
    img = Image.new('RGB', (200, 200), (255, 255, 255))
    img.save(tmp("bg.png"), "PNG")


if __name__ == '__main__':
    font_path = root + "/fonts/simhei.ttf"
    img_bg = create_image(size=(200, 200), color=(255, 255, 255))
    img = draw_text(img_bg, font_path, '中国123A', rotate=96, position=(10, 10))
    img = draw_text(img, font_path, '中国123B', rotate=0, position=(30, 10))
    noise(img, 200, 200, 10, 100)
    show_image(img)
