import numpy as np
import cv2
import pywt

def DWT(coverImage, watermarkImage):
    # coverImage = cv2.resize(coverImage,(300,300))
    cv2.imshow('Cover Image',coverImage)
    # watermarkImage = cv2.resize(watermarkImage,(150,150))
    cv2.imshow('Watermark Image',watermarkImage)

    #DWT on cover image
    coverImage =  np.float32(coverImage)   
    coverImage /= 255;
    coeffC = pywt.dwt2(coverImage, 'haar')
    cA, (cH, cV, cD) = coeffC
    
    watermarkImage = np.float32(watermarkImage)
    watermarkImage /= 255;

    #Embedding
    # coeffW = (0.4*cA + 0.1*watermarkImage, (cH, cV, cD))
    watermarkImage = np.reshape(watermarkImage, (1500, 750, 2)) #30000
    coeffW = (np.dot(0.4, cA) + np.dot(0.1, watermarkImage), (cH, cV, cD))
    watermarkedImage = pywt.idwt2(coeffW, 'haar')
    cv2.imshow('Watermarked Image', watermarkedImage)

    # #Extraction
    # coeffWM = pywt.dwt2(watermarkedImage, 'haar')
    # hA, (hH, hV, hD) = coeffWM

    # extracted = (hA-0.4*cA)/0.1
    # extracted *= 255
    # extracted = np.uint8(extracted)
    # cv2.imshow('Extracted', extracted)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cover = cv2.imread("./dataset/3.png")
watermark = cv2.imread("./dataset/signature.png")

DWT(cover, watermark)