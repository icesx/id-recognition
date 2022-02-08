# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from dataset.dataset_loader import DatasetLoader
from model.model import run_model, save_model
from model.model_define import ModelDefine, CaptchaModelDefine, IdModelDefine
from model.predict import predict_plt


def train(md: ModelDefine):
    creator = DatasetLoader(md)
    val_creator = DatasetLoader(md)
    _train_ds = creator.load(md.train_path()).shuffle_and_repeat().batch(md.train_batch())
    _val_ds = val_creator.load(md.val_path()).shuffle_and_repeat().batch(md.val_batch())
    model = run_model(_train_ds, _val_ds, md)
    save_model(model, md.save_path())
    test_creator = DatasetLoader(md)
    _test_ds = test_creator.load(md.test_path())
    predict_plt(model, _test_ds.base_ds())


def train_captcha():
    pass


if __name__ == '__main__':
    # train(IdModelDefine())
    train(CaptchaModelDefine())
