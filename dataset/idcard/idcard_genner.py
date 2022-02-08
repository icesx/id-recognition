# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# 3/23/21

import copy
import os
import random

import cv2
import freetype
import numpy as np

from dataset.dataset_genner import DatasetGenn
from model.model_define import ModelDefine


class TextDrawer(object):
    def __init__(self, ttf):
        self._face = freetype.Face(ttf)

    def draw_text(self, image, pos, text, text_size, text_color):
        '''
        draw chinese(or not) text with ttf
        :param image:     image(numpy.ndarray) to draw text
        :param pos:       where to draw text
        :param text:      the context, for chinese should be unicode type
        :param text_size: text size
        :param text_color:text color
        :return:          image
        '''
        self._face.set_char_size(text_size * 64)
        metrics = self._face.size
        ascender = metrics.ascender / 64.0

        # descender = metrics.descender/64.0
        # height = metrics.height/64.0
        # linegap = height - ascender + descender
        ypos = int(ascender)

        # if not isinstance(text, unicode):
        # text = text.decode('utf-8')
        img = self.draw_string(image, pos[0], pos[1] + ypos, text, text_color)
        return img

    def draw_string(self, img, x_pos, y_pos, text, color):
        '''
        draw string
        :param x_pos: text x-postion on img
        :param y_pos: text y-postion on img
        :param text:  text (unicode)
        :param color: text color
        :return:      image
        '''
        prev_char = 0
        pen = freetype.Vector()
        pen.x = x_pos << 6  # div 64
        pen.y = y_pos << 6

        hscale = 1.0
        matrix = freetype.Matrix(int(hscale) * 0x10000, int(0.2 * 0x10000), \
                                 int(0.0 * 0x10000), int(1.1 * 0x10000))
        cur_pen = freetype.Vector()
        pen_translate = freetype.Vector()

        image = copy.deepcopy(img)
        for cur_char in text:
            self._face.set_transform(matrix, pen_translate)

            self._face.load_char(cur_char)
            kerning = self._face.get_kerning(prev_char, cur_char)
            pen.x += kerning.x
            slot = self._face.glyph
            bitmap = slot.bitmap

            cur_pen.x = pen.x
            cur_pen.y = pen.y - slot.bitmap_top * 30
            self.draw_ft_bitmap(image, bitmap, cur_pen, color)

            pen.x += slot.advance.x
            prev_char = cur_char

        return image

    def draw_ft_bitmap(self, img, bitmap, pen, color):
        '''
        draw each char
        :param bitmap: bitmap
        :param pen:    pen
        :param color:  pen color e.g.(0,0,255) - red
        :return:       image
        '''
        x_pos = pen.x >> 6
        y_pos = pen.y >> 6
        cols = bitmap.width
        rows = bitmap.rows

        glyph_pixels = bitmap.buffer

        for row in range(rows):
            for col in range(cols):
                if glyph_pixels[row * cols + col] != 0:
                    img[y_pos + row][x_pos + col][0] = color[0]
                    img[y_pos + row][x_pos + col][1] = color[1]
                    img[y_pos + row][x_pos + col][2] = color[2]


class GenIdCard(DatasetGenn):
    def __init__(self, md: ModelDefine):
        self._textDrawer = TextDrawer('fonts/OcrB2.ttf')
        self._md = md

    def __random_text(self):
        text = ''
        for i in range(self._md.charset_len()):
            c = random.choice(self._md.charset())
            text = text + c
        return text

    def __draw_image(self):
        label = self.__random_text()
        img = np.zeros([self._md.image_height(), self._md.image_width(), self._md.image_channels()])
        color_ = (255, 255, 255)
        pos = (0, 0)
        text_size = 21
        image = self._textDrawer.draw_text(img, pos, label, text_size, color_)
        return image, label

    def gen_dataset(self, _dir, count):
        for _ in range(count):
            image_data, label = self.__draw_image()
            if os.path.exists(_dir) is False:
                os.mkdir(_dir)
            png_ = _dir + label + ".png"
            print(png_)
            cv2.imwrite(png_, image_data)
