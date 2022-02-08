# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from dataset.create_dataset import DatasetCreator
from define import IMAGE_HEIGHT, IMAGE_WIDTH, DATASET_PATH
from model.model import run_model, save_model
from model.predict import predict_plt

if __name__ == '__main__':
    creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    val_creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    _train_ds = creator.load(DATASET_PATH + "train/").shuffle_and_repeat().batch(100)
    _val_ds = val_creator.load(DATASET_PATH + "val/").shuffle_and_repeat().batch(10)
    model = run_model(_train_ds, _val_ds, epochs=3, steps_per_epoch=100)
    save_model(model, "./save/model")
    test_creator = DatasetCreator(IMAGE_HEIGHT, IMAGE_WIDTH)
    _test_ds = test_creator.load(DATASET_PATH + "test/")
    predict_plt(model, _test_ds.base_ds())
