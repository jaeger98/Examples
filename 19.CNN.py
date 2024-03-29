# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:58:57 2024

@author: jaege
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# MNIST 데이터 로드 및 전처리
(train_images1, train_labels), (test_images1, test_labels) = mnist.load_data()
train_images = train_images1.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images1.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# CNN 모델 구성
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 모델 훈련
history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

# 모델 평가
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

import numpy as np
predict = model.predict(test_images)
print("test Labels :\n",test_labels[:10])
print("Predictions :\n",np.argmax(predict[:10], axis=1))

i=7
plt.imshow(test_images1[i])
plt.title(np.argmax(predict[i:i+1], axis=1))
plt.show()