# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import datetime
import itertools
import string


def test_list():
    str = "abdcd"
    print(list(str))
    list_ = []
    list_.extend(str)
    print(list_)


def test_permutation():
    choices = [
        list(map(str, range(10))),
        list(string.ascii_lowercase),
        list(string.ascii_uppercase),
    ]
    choices = sum(choices, [])
    print(choices)
    samples = itertools.permutations(choices, 4)
    print(list(samples))


def test_permutation2():
    _CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(list(itertools.permutations(_CHAR_SET, 4)))


if __name__ == '__main__':
    test_list()
    test_permutation2()
    print("./tmp/logs/tb/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
