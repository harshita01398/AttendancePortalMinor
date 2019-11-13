import cv2
import numpy as np
import detectLines
import vertical
import roi
from rectangle import extractTable
from util import resize

try:
    img =  cv2.imread(input("Enter the name of the image : "))
    #print(img.shape)

    # Resize image to appt proportion
    resizedImg = resize(img)

    # Extract table and change Perspective
    rectImg = extractTable(resizedImg)

    # Detect Horizontal Lines
    horizontalLines = detectLines.detect(rectImg)
    # Detect Vertical Lines
    verticalLines = vertical.detect(rectImg)

    # Create Cells and Call predictor on each cell
    roi.createRow(rectImg,horizontalLines,verticalLines)


    #cv2.imshow("Rectangle",rectImg)
    #cv2.imshow("Original",img)

except AttributeError:
    print("Enter valid Image name")

#cv2.waitKey(0)
cv2.destroyAllWindows()
