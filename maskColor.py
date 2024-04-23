import cv2
import numpy as np

def preprocess(image):
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    vNew = np.clip(v, 5, 250)
    # with np.printoptions(threshold=np.inf): print(vNew)
    newimage = cv2.merge([h, s, vNew])
    newimage = cv2.cvtColor(newimage, cv2.COLOR_HSV2BGR)
    # cv2.imshow("mask", newimage)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return newimage
    # cv2.imwrite("./dataset/percontohan.png", newimage)

#harus HSV space
image = cv2.imread("./dataset/2.png")
preprocess(image)