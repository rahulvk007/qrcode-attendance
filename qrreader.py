import cv2

filename="ar.png"
img = cv2.imread(filename)
detect = cv2.QRCodeDetector()
value, points, straight_qrcode = detect.detectAndDecode(img)
print(value)