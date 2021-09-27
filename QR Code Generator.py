import qrcode

code_generator = qrcode.make("2008:06:21 16:12:37,xyz")
code_generator.save('code.png')


import cv2
exif_data = cv2.QRCodeDetector()
val, points, straight_qrcode = exif_data.detectAndDecode(cv2.imread('code.png'))
print(val)