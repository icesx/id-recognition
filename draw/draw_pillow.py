# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def open_image(image_path):
    return Image.open(image_path)


def create_image(size=(100, 100), color=(255, 255, 255)):
    return Image.new('RGB', size, color)


def save_image(img, image_path):
    img.save(image_path)


def show_image(img):
    img.show()


def draw_text(__img_bg, font_path, text, text_color=(0, 0, 255), position=(0, 0), rotate=0):
    draw = ImageDraw.Draw(__img_bg)
    font = ImageFont.truetype(font_path, 20)
    draw.text(position, text, text_color, font=font)
    return __img_bg.rotate(rotate, expand=1, fillcolor=(255, 255, 255))


def random_color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return c1, c2, c3


def noise(image, width, height, line_count, point_count):
    draw = ImageDraw.Draw(image)
    for i in range(line_count):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, x2, y1, y2), fill=random_color())
    for i in range(point_count):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 3, y + 3), 0, 90, fill=random_color())
    return image
