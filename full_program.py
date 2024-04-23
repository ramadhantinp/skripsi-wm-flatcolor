from dwt_watermark import DWT_Watermark
import cv2
import numpy as np
import inquirer

def preprocess(image):
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    vNew = np.clip(v, 5, 250)
    # with np.printoptions(threshold=np.inf): print(vNew)
    newimage = cv2.merge([h, s, vNew])
    newimage = cv2.cvtColor(newimage, cv2.COLOR_HSV2BGR)
    return newimage

# print("baca gambar dulu")
# watermark = cv2.imread('./dataset/signature.png', cv2.IMREAD_GRAYSCALE)
# gambarasli = cv2.imread('./dataset/5.png')
# gambarPreproses = preprocess(gambarasli)
# print("watermarking...")
# gambarWm = DWT_Watermark().embed(gambarPreproses, watermark)
# cv2.imshow("gambar diwatermark", gambarWm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('./hasil/trial1/gambarWm5.png', gambarWm)

print("baca gambar dulu")
gambarWm = cv2.imread('./hasil/trial1/gambarWm4.png')
print ("mengekstraksi watermark...")
watermarkBaru = DWT_Watermark().extract(gambarWm)
# watermarkIntegral = cv2.integral(src=watermarkBaru)
# watermarkInt8 = watermarkIntegral/watermarkIntegral.max()
cv2.imshow("ekstraksi watermark", watermarkBaru)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('./hasil/trialWm1/wm4.png', watermarkBaru)