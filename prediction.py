from keras.models import load_model
from PIL import Image
import numpy as np


def predict_digit(img):
    img = Image.open(img)
    model = load_model('mnist.h5')
    # resize image to 28x28 pixels
    img = img.resize((28, 28))
    # convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    # reshaping to support our model input and normalizing
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0
    # predicting the class
    res = model.predict([img])[0]
    print(np.argmax(res), max(res))
    return np.argmax(res), max(res)


predict_digit('5Test.png')
