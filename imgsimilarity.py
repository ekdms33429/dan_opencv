import cv2
from skimage.metrics import structural_similarity as compare_ssim

imageA = cv2.imread("screencap.png")
imageB = cv2.imread("img/kiwilogo.jpg")
imageC = imageA.copy()

tempDiff = cv2.subtract(imageA, imageB)

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

print(f"Similarity: {score:.5f}")

assert score, "다른 점 찾을 수 없음"