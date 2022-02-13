# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

from PIL import Image, ImageFont
from PIL import ImageDraw

from define import root


class PillowDraw():
    def __init__(self, font):
        self.__bg = None
        self.__font = font

    def from_bg(self, image_bg):
        self.__bg = Image.open(image_bg)

    def rotate(self, rotate):
        pass


def tmp(name):
    return root + "/tmp/" + name;


def white():
    img = Image.new('RGB', (200, 200), (255, 255, 255))
    img.save(tmp("bg.png"), "PNG")


def open_image(image_path):
    return Image.open(image_path)


def create_image(size=(100, 100), color=(255, 255, 255)):
    return Image.new('RGB', size, color)


def save_image(img, image_path):
    img.save(image_path)


def show_image(img):
    img.show()


def draw_text(__img_bg, text, text_color=(0, 0, 255), rotate=0):
    draw = ImageDraw.Draw(__img_bg)
    font = ImageFont.truetype(root + "/fonts/simhei.ttf", 20)
    draw.text((0, 0), text, text_color, font=font)
    return __img_bg.rotate(rotate, expand=1)


if __name__ == '__main__':
    img_bg = create_image(size=(200, 200), color=(255, 255, 255))
    img = draw_text(img_bg, '中国123A', rotate=90)
    img = draw_text(img, '中国123A', rotate=0)
    show_image(img)
