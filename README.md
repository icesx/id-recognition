# id-recognition
<<<<<<< HEAD
使用tensorflow进行图片中数字或者文字序列的识别

### captcha

### 基本原理

1. 使用captcha生成验证码的数据集。

2. 采用基本的卷积神经网络，进行训练。基本的网络结构如下

   ```python
       model = keras.Sequential([
           keras.layers.Conv2D(32, (3, 3), input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 1)),
           keras.layers.PReLU(),
           keras.layers.MaxPool2D((2, 2), strides=2),
           keras.layers.Conv2D(64, (3, 3)),
           keras.layers.PReLU(),
           keras.layers.MaxPool2D((2, 2), strides=2),
           keras.layers.Conv2D(64, (3, 3), padding="same"),
           keras.layers.PReLU(),
           keras.layers.MaxPool2D((2, 2), strides=2),
           keras.layers.Conv2D(96, (3, 3), padding="same"),
           keras.layers.PReLU(),
           keras.layers.MaxPool2D((2, 2), strides=2),
           keras.layers.Conv2D(120, (3, 3), padding="same"),
           keras.layers.PReLU(),
           keras.layers.MaxPool2D((2, 2), strides=2, padding="same"),
           keras.layers.Flatten(),
           keras.layers.Dense(MAX_CAPTCHA * CHAR_SET_LEN),
           keras.layers.Reshape([MAX_CAPTCHA, CHAR_SET_LEN]),
           keras.layers.Softmax()
       ])
   ```

3. 不知道为何如果没有`keras.layers.PReLU()`会无法收敛，后续再找资料查询一下。

4. MAX_CAPTCHA 为验证码的长度

5. CHAR_SET_LEN为验证码的所有字符集的长度

6. 相当于对神经网络预测one-hot编码

### 训练过程

=======
id-recognition
>>>>>>> cdcaca27417a25e0bd174c9e8c08582d3692be39
