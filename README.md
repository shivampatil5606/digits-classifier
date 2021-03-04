# Digit Classifier 
This is a simple digit classifier on mnist dataset using a simple sequential model.

The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems
You can read more about mnist dataset here : https://en.wikipedia.org/wiki/MNIST_database

It takes the dataset from the keras library so you don't have to download it. But i recommend to atleast go through it.                                                              
**Dataset** : http://yann.lecun.com/exdb/mnist/


**Installation** : 
```pip install keras, tensorflow, numpy, pillow```

Here you will find two files.
The file kerasmnist.py helps to create a **Sequential** model and save the model in .h5 format.
In this file we import the valid libraries and load the datset from keras library.


The file prediction.py helps to prdict the number. We pass the image path to the function predict.



