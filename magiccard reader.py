import cv2
from PIL import Image
import pytesseract
import requests
import re

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

camera = cv2.VideoCapture(0)

while True:

    ret, image = camera.read()
    if not ret:
         #if not true cameras fucked
        print("camera not found")
        break
    imageboxed = cv2.rectangle(image, (25, 30), (500, 70), color=(0,225,0), thickness=2)
    #show camera feed
    cv2.imshow('camera feed', imageboxed)
    
    #show feed until key is pressed
    key=cv2.waitKey(10)
    if key == 121 or key == 89:
        #crop to box
        image = image[30:70,25:500]
        cv2.imshow('cropped', image)
        
        #make greyscale for easier reading
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret ,thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)
        cv2.imshow('greyscale', thresholded)
        #parse text
        text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
        text = text.strip()
        text = re.sub(r'\W+','',text)
        if len(text) > 0:
            print(text)
            headers = {"User-Agent":"LetheCardChecker","Accept":"*/*","Content-Type": "application/json"} 
            response = requests.get("https://api.scryfall.com/cards/named",headers=headers,params={"fuzzy":text, "pretty":True})
            if response.status_code == 404:
                print("card name invalid, try getting a clearer picture or ensure that your OCR is setup for the language the card is in")
            else:
                cardDat=response.json()
                legalities=cardDat["legalities"]
                legal = []
                nlegal = []
                for i in legalities:
                    if legalities[i]=="not_legal":
                        nlegal.append(i)
                    else:
                        legal.append(i)
                print(text, "is legal in: ")
                print(legal)
                print("and not legal in: ")
                print(nlegal)
            
    if key == 81 or key == 113:
        break
        
    
camera.release()
cv2.destroyAllWindows()
