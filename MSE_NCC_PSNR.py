import numpy as np
import cv2
import pandas as pd
import skimage as skimg

#good MSE: 0
#good PSNR: 30 - 50 db
#good ncc: 1

def nilaiGambar(img, imgwm, nomorGambar):
    hasil_mse = skimg.metrics.mean_squared_error(img, imgwm)
    hasil_psnr1 = skimg.metrics.peak_signal_noise_ratio(img, imgwm)
    hasil_psnr2 = PSNR(img, imgwm)
    hasil_ncc = NCC(img, imgwm)

    print('Gambar nomor ', nomorGambar)
    print ('MSE: ', hasil_mse)
    print ('PSNR  skimg: ', hasil_psnr1)
    print ('PSNR manual: ', hasil_psnr2)
    print ('NCC: ', hasil_ncc)

def PSNR(original, watermarked):
    MSE = np.mean((original - watermarked)**2)
    if (MSE == 0): return 100
    return 20*np.log10(255.0/np.sqrt(MSE))

def NCC(original, watermarked):
    return np.sum((original - np.mean(original)) * (watermarked - np.mean(watermarked)) / ((np.std(original) * np.std(watermarked)) * original.size))

# print("baca gambar dulu")
gambarasli = cv2.imread('./dataset/signature.png', cv2.IMREAD_GRAYSCALE)
# gambarmodifikasi = cv2.imread('./hasil/trialWm1/wm4.png', cv2.IMREAD_GRAYSCALE)
# nilaiGambar(gambarasli, gambarmodifikasi, '4')

path = [
    './hasil/trialWm1/hsv/1.png',
    './hasil/trialWm1/hsv/2.png',
    './hasil/trialWm1/hsv/3.png',
    './hasil/trialWm1/hsv/4.png'
]

for i in path:
    gambar = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    nilaiGambar(gambar, gambarasli)