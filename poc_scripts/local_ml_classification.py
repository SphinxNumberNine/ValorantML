import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import zipfile
import os

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

model = keras.models.load_model('config\\model.h5')
class_names = ['astra', 'breach', 'brimstone', 'chamber', 'cypher', 'fade', 'gekko', 'harbor', 'jett', 'kayo', 'killjoy', 'neon', 'omen', 'phoenix', 'raze', 'reyna', 'sage', 'skye', 'sova', 'viper', 'yoru']

def predict(img_path):
    img = keras.utils.load_img(img_path, target_size=(54, 72))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )



predict("assets\\test_dataset\\breach\\5041576.png")
predict("assets\\test_dataset\\reyna\\577209.png")