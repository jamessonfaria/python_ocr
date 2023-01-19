
import pytesseract
import cv2

img_path = "c:\\work\\capco\\aws-ocr\\images\\cert_obt1.jpg"
image = cv2.imread(img_path)

# image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# output = img_path.replace(".png", "_cinza.png")
# cv2.imwrite(output, image_converted)

path_tesseract = "C:\\Program Files\\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = path_tesseract + "\\tesseract.exe"

result = pytesseract.image_to_string(image, lang="por")

print(result)