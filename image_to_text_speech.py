# Author: Endri Dibra

# importing the required libraries
import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound

# Initializing the type of audio and language
audio = 'speech.mp3'
language = "en"

# tesseract's path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# image to be processed
img = cv2.imread('text_image.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# getting image's shape
height_Img, weight_Img, _ = img.shape

# processing the image, putting into boxes the letters, splitting the letters
# and drawing the respectively letters

boxes = pytesseract.image_to_boxes(img)

for box in boxes.splitlines():

    box = box.split(' ')

    print(box)

    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])

    cv2.rectangle(img, (x, height_Img - y), (w, height_Img - h), (50, 50, 255), 2)

    cv2.putText(img, box[0], (x, height_Img - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)


# printing the final image
text = pytesseract.image_to_string(Image.open("text_image.png"))
print(text)

cv2.imshow('img', img)
cv2.waitKey(0)

# Initializing input, language
sp = gTTS(text=text, lang=language, slow=False)

# The input from the user will be saved
# and played by the computer using machine-voice
sp.save(audio)
playsound(audio)