import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
plt.style.use('dark_background')

img_ori = cv2.imread('img/3.jpg')
height, width, channel = img_ori.shape

plt.figure(figsize=(12,10))
plt.imshow(img_ori, cmap='gray')
print(height, width, channel)