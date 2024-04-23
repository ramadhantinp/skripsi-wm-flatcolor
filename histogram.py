import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('../dataset/selfmade/data_1a.png')
# img2 = cv2.imread('dataset/selfmade/data_2a.png', cv2.IMREAD_GRAYSCALE)
# img3 = cv2.imread('dataset/selfmade/data_3a.png', cv2.IMREAD_GRAYSCALE)
# img4 = cv2.imread('dataset/selfmade/data_4a.png', cv2.IMREAD_GRAYSCALE)
# img5 = cv2.imread('dataset/selfmade/data_5a.png', cv2.IMREAD_GRAYSCALE)
# img6 = cv2.imread('dataset/selfmade/data_6a.png', cv2.IMREAD_GRAYSCALE)
# img7 = cv2.imread('dataset/selfmade/data_1b.png', cv2.IMREAD_GRAYSCALE)
# images = [img1, img2, img3, img4, img5, img6, img7]

cv2.imshow('gambar', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# for i in range(len(images)):
    #crash
    # gambar = images[i]
    # cv2.imshow('gambar', gambar)
    # cv2.waitKey()
    # cv2.destroyAllWindows

    # no_judul = i+1
    # plt.hist(images[i].ravel(),256,[0,256])
    # plt.title('histogram data %i' %no_judul)
    # plt.show()