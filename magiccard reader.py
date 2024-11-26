import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

camera = cv2.VideoCapture(0)

while True:

    ret, image = camera.read()
    if not ret:
         #if not true cameras fucked
        print("camera not found")
        break
    #show camera feed
    cv2.imshow('camera feed', image)
    
    #show feed until key is pressed
    key=cv2.waitKey(10)
    if key == 121 or key == 89:
        #make greyscale for easier reading
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret ,thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)

        #parse text
        text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
        text = text.strip()
        if len(text) > 0:
            print(text)

    if key == 81 or key == 113:
        break
        
    
camera.release()
cv2.destroyAllWindows()
