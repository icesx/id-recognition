# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from dataset.captcha.captcha_genner import GenCaptcha
from dataset.idcard.idcard_genner import GenIdCard


def genn_id_card():
    genn = GenIdCard()
    genn.gen_dataset("/OTHER/dataset/id_card/train/", 10000)
    genn.gen_dataset("/OTHER/dataset/id_card/val/", 1000)
    genn.gen_dataset("/OTHER/dataset/id_card/test/", 100)


def genn_captcha():
    genn = GenCaptcha()
    genn.gen_dataset("/OTHER/dataset/captcha/train/", 1000)
    genn.gen_dataset("/OTHER/dataset/captcha/val/", 1000)
    genn.gen_dataset("/OTHER/dataset/captcha/test/", 10)


if __name__ == '__main__':
    # genn_id_card()
    genn_captcha()
