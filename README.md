# id-recognition
基于tensorflow2 使用CNN进行图片中数字或者文字序列的识别

### 基本过程

1. 生成数字序列图片
2. 使用CNN进行卷积识别

### CNN设计

参考AlexNet，结构如下

```python
    _model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), activation="relu"),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Conv2D(64, (1, 1), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dense(ID_LEN * CHAR_SET_LEN, activation="softmax"),
        keras.layers.Reshape([ID_LEN, CHAR_SET_LEN]),
    ])
```

1. ID_LEN：生成的id号码的长度
2. CHAR_SET_LEN：生成Id号码的字符集（0-9）长度

### 使用

#### 生成数据集

```sh
python3 idcard_genner.py
```

#### 训练模型

```sh
python3 model_train.py
```

### 预测

```sh
python3 model_predict.py
```

在默认的参数情况下，基本上可以达到100%的准确率。



### 参考地址

https://github.com/JackonYang/captcha-tensorflow

