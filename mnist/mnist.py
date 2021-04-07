# -*- coding: utf-8 -*-
"""mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Ia2mhLIT8XTYeHktPDm4R4EuWtr68SQ
"""

import tensorflow as tf
import matplotlib.pyplot as plt
print(tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()

plt.xlabel('Digit')
plt.ylabel('Value')
plt.title('Training Data')
#plt.scatter(x_train,y_train)

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train , axis = 1)
x_test = tf.keras.utils.normalize(x_test , axis = 1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64 , activation = tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(64 , activation = tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(10 , activation = tf.keras.activations.softmax))

model.compile(optimizer = 'adam' ,
             loss = 'sparse_categorical_crossentropy',
             metrics = ['accuracy'])
history = model.fit(x_train,y_train,epochs=3, validation_data=(x_test, y_test))

train_loss = history.history['loss']
test_loss = history.history['val_loss']

epoch_count = range(1, len(train_loss) + 1)

plt.plot(epoch_count, train_loss, 'r--')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss during training')
plt.show();

plt.imshow(x_test[98])

#print(x_train[0])

predictions = model.predict([x_test])

import numpy as np

print(np.argmax(predictions[98]))

