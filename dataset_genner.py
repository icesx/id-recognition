# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from dataset.captcha.captcha_define import CaptchaModelDefine
from dataset.captcha.captcha_genner import GenCaptcha
from dataset.eartag.eartag_define import EartagModelDefine
from dataset.eartag.eartag_genner import GenEartag
from dataset.idcard.idcard_define import IdModelDefine
from dataset.idcard.idcard_genner import GenIdCard


def gen_idcard():
    genn = GenIdCard(IdModelDefine())
    genn.gen_train(10000)
    genn.gen_val(1000)
    genn.gen_test(100)


def gen_captcha():
    genn = GenCaptcha(CaptchaModelDefine())
    genn.gen_train(30000)
    genn.gen_val(3000)
    genn.gen_test(300)


def gen_eartag():
    gen = GenEartag(EartagModelDefine())
    gen.gen_train(30)
    gen.gen_val(10)
    gen.gen_test(3)


if __name__ == '__main__':
    # genn_id_card()
    # genn_captcha()
    gen_eartag()
