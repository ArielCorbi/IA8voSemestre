import tensorflow as tf
from keras import layers, models
import os
import numpy as np
import cv2
import random


width = 48
height = 48

ruta_train = 'archive/ck/CK+48/'
ruta_predict = 'archive/CK+48/surprise/S010_002_00000012.png'

'''
sadness
archive/ck/CK+48/sadness/S501_006_00000039.png"
'''
'''
anger
archive/ck/CK+48/sadness/S066_004_00000010.png
'''
'''
anger
archive/CK+48/anger/S026_003_00000015.png
'''
'''
disgust
archive/CK+48/disgust/S131_010_00000018.png
'''
'''
archive/CK+48/fear/S504_004_00000014.png
'''
'''
happy
/archive/CK+48/happy/S099_004_00000014.png
'''
train_x = []
train_y = []

labels = os.listdir(ruta_train)
for i in os.listdir(ruta_train):
    for j in os.listdir(ruta_train + i):
        img = cv2.imread(ruta_train+i+'/'+j)
        resized_image = cv2.resize(img, (width, height))

        train_x.append(resized_image)

        for x,y in enumerate(labels):
            if y == i:
                array = np.zeros(len(labels))
                array[x] = 1
                train_y.append(array)

x_data = np.array(train_x)
y_data = np.array(train_y)

model = tf.keras.Sequential([
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(width, height, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(7, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 200

model.fit(x_data, y_data, epochs=epochs)

model.save('emociones2.keras')

model = models.load_model('emociones2.keras')

my_image = cv2.imread(ruta_predict)
my_image = cv2.resize(my_image, (width, height))
my_image = my_image / 255.0 

result = model.predict(np.array([my_image]))[0]

for i, label in enumerate(labels):
    porcentaje = result[i] * 100
    print(f"{label}: {porcentaje:.2f}%")

cv2.imshow('Hola', cv2.imread(ruta_predict))
cv2.waitKey(0)
