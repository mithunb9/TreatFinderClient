import requests
import cv2
import numpy as np
from matplotlib import pyplot as plt

#be sure to change the size of the map
centerLat = 33.001362229015434
centerLong= -96.639781590491
URL = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(centerLat)+ "," + str(centerLong) + "&zoom=20&size=400x400&key=AIzaSyAHeT3omlNayd1-p5pEP0FwZbhXlpobqDY&signature=YOUR_SIGNATURE"

#create a file to store the image
response = requests.get(URL)
with open("map.png", "wb") as f:
    f.write(response.content)

img = cv2.imread(URL)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i=0

for cnt in contours:

    if i==0: #first loop detects the entire image or frame as a contour
        i=1 #ignoring the first contour
        continue    

    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 5)

    #find the center-coordinates of the contour
    M = cv2.moments(cnt)
    if M['m00']!=0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    #4 vertices = building -- anything else is a house
    if len(approx)!=4:
        cv2.putText(img, "House", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        print("0")
    elif len(approx)==4:
        cv2.putText(img, "Building", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        print("1")

cv2.imshow('map', img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



