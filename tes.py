import cv2
import pywt
import numpy as np

#read sign
signature = cv2.imread("./dataset/signature.png", cv2.IMREAD_GRAYSCALE)
signatureBin =  np.float32(signature)   
signatureBin /= 255
signatureBin = signatureBin.astype(int)
# with np.printoptions(threshold=np.inf):
#     print(signatureBin)

def tralala(LL):
    LLnew = LL
    if (len(signatureBin) < len(LL)):
        n = signatureBin
    else:
        n = LL
    for j in n:
        LLInt = LL[j]//1
        LLFloat = LL[j]%1
        LLInt = LLInt.astype('int32')
        #fungsi membadningkannya gak ngebandingin... kesel deh hgngggggg ih
        if (LLInt.any()%2 == 0): LLnew[j]=99
            # if (signatureBin[j].any() == 1): continue
            # else: LLnew[j] = 99
        else: continue

img = cv2.imread("./dataset/4.png", cv2.IMREAD_COLOR)
# cv2.imshow('hasil',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

b,g,r = cv2.split(img)
# cv2.imshow('blue', b)

coeffsb = pywt.dwt2(b, 'haar')
LLb, (LHb, HLb, HHb) = coeffsb
# coeffsg = pywt.dwt2(g, 'haar')
# LLg, (LHg, HLg, HHg) = coeffsg
# coeffsr = pywt.dwt2(b, 'haar')
# LLr, (LHr, HLr, HHr) = coeffsr
# print (LLb, LLg, LLr)

# hori1 = np.concatenate((LLb, LHb), axis=1) 
# hori2 = np.concatenate((HLb, HHb), axis=1)
# verti = np.concatenate((hori1, hori2), axis=0)
# cv2.imshow('tes b', verti)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
LLbnew = tralala(LLb)
with np.printoptions(threshold=np.inf): print(LLbnew)
# newcoeffsb = LLbnew, (LHb, HLb, HHb)
# watermarkedImageb = pywt.idwt2(newcoeffsb, 'haar')
# cv2.imshow('gambar b', watermarkedImageb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# hori1 = np.concatenate((LLg, LHg), axis=1) 
# hori2 = np.concatenate((HLg, HHg), axis=1)
# verti = np.concatenate((hori1, hori2), axis=0)
# cv2.imshow('tes g', verti)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# LLgnew = tralala(LLg)
# newcoeffsg = LLgnew, (LHg, HLg, HHg)
# watermarkedImageg = pywt.idwt2(newcoeffsg, 'haar')
# cv2.imshow('gambar g', watermarkedImageg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# hori1 = np.concatenate((LLr, LHr), axis=1) 
# hori2 = np.concatenate((HLr, HHr), axis=1)
# verti = np.concatenate((hori1, hori2), axis=0)
# cv2.imshow('tes h', verti)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# LLrnew = tralala(LLr)
# newcoeffsr = LLrnew, (LHr, HLr, HHr)
# watermarkedImager = pywt.idwt2(newcoeffsr, 'haar')
# cv2.imshow('gambar r', watermarkedImager)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #cara mergenya = ???
# newimg = cv2.merge(watermarkedImageb, watermarkedImageg, watermarkedImager)
# cv2.imshow('gambar', newimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # LLbBin = np.vectorize(np.binary_repr)(LLbBin, 9)

# # hori3 = np.concatenate((LLb, LLbBin), axis=1)
# # cv2.imshow('tes', hori3)