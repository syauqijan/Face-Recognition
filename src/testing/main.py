from step1 import *
from eigenfaces import *
from eucidilian import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

data = r'D:\Kelvin\code\python\Algeo02-21001\test\dataset'

images = imagevector(data)
mean = meanSetImg(images)

differenceimg = setDiffImg(images,mean)
covariance = covarian(differenceimg)
tempval, eigvect = find_eig_qr(covariance)
leneigen = round(len(differenceimg)*0.05)

eigfacearr = eigface(leneigen,eigvect,differenceimg)

test = r'D:\Kelvin\code\python\Algeo02-21001\test\dataset\Avril Lavigne37_681.jpg'
testimg = cv2.imread(test,0)
testimg = cv2.resize(testimg,(256,256))
testimg = np.array(testimg).flatten()
for i in range(256*256) :
    testimg[i] -= mean[i]

testimg = reshapeimg(testimg)
for i in range (len(differenceimg)):
    differenceimg[i] = reshapeimg(differenceimg[i])

wtest = weighttest(testimg,eigfacearr)
w = weightdata(differenceimg,eigfacearr)

x = euclidean_distance(wtest,w)
showimg(images,x)