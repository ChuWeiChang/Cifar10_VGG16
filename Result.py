# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:05:37 2021

@author: duked
"""

from PyQt5 import QtWidgets
from UI2 import Ui_MainWindow
import cv2
import numpy as np
from keras.models import load_model
from keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randrange

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.model = load_model("./model.h5")
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.B1.clicked.connect(self.B1)
        self.ui.B2.clicked.connect(self.B2)
        self.ui.B3.clicked.connect(self.B3)
        self.ui.B4.clicked.connect(self.B4)
        self.ui.B5.clicked.connect(self.B5)
        (self.X_train, self.Y_train), (self.X_test, self.Y_test) = cifar10.load_data()
        self.Y_title = self.Y_train
        self.X_train = self.X_train.astype("float32") / 255
        self.X_test = self.X_test.astype("float32") / 255
        self.Y_train = to_categorical(self.Y_train)
        self.Y_test = to_categorical(self.Y_test)
    def B1(self):
        import matplotlib
        matplotlib.use('Qt5Agg')
        cla = {"0":"aiplane",
               "1":"automobile",
               "2":"bird",
               "3":"cat",
               "4":"deer",
               "5":"dog",
               "6":"frog",
               "7":"horse",
               "8":"ship",
               "9":"truck"}
        plt.figure(figsize = (10,10))
        for i in range(9):
            a = randrange(self.X_train.shape[0])
            
            plt.subplot(3,3,i+1).imshow(self.X_train[a])
            plt.title(cla[str(self.Y_title[a][0])])
            plt.axis("off")
            plt.show()
    def B2(self):
        batchsize=32
        lr=0.001
        opt = "SGD"
        print("hyperparameters:")
        print("batch size: " ,format(batchsize))
        print("learning rate: " ,format(lr))
        print("optimizer: " + opt)
    def B3(self):
        self.model.summary()
    def B4(self):
        img1 = mpimg.imread('./accuracy.png')
        img2 = mpimg.imread('./loss.png')
        plt.figure()
        plt.subplot(2,1,1).imshow(img1)
        plt.axis("off")
        plt.subplot(2,1,2).imshow(img2)
        plt.axis("off")
        plt.show()
    def B5(self):
        number = int(self.ui.lineEdit.text())
        img = self.X_test[number]
        X_test_img = img.reshape(-1,32, 32, 3).astype("float32")
        plt.figure(figsize = (10,10))
        plt.subplot(1,2,1)
        plt.imshow(img)
        plt.axis("off")
        plt.subplot(1,2,1)
        plt.imshow(img)
        plt.axis("off")
        
        probs = self.model.predict(X_test_img)
        values = ["aiplane",
               "automobile",
               "bird",
              "cat",
              "deer",
               "dog",
               "frog",
               "horse",
               "ship",
               "truck"]
        plt.subplot(1,2,2)
        plt.title("Probabilities for Each Image Class")
        plt.bar(np.arange(0,10,1), probs.reshape(10))
        plt.xticks(np.arange(0,10,1),values, rotation = "vertical")
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
