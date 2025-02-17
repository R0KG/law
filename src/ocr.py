from PIL import Image
import cv2
import numpy as np
import pytesseract
import re

    

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("input/document.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray, lang="eng")

print(text)
print("--------------------------------")

cleaned_text = text.strip()
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)    
cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
print(cleaned_text)



def cleaned_text() -> str:
    return cleaned_text


