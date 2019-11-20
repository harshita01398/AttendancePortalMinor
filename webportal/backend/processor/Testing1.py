import cv2
import numpy as np
import backend.processor.detectLines as detectLines
import backend.processor.vertical as vertical
import backend.processor.roi as roi 
import backend.processor.rectangle as rectangle

from django.conf import settings

def convert(img_path):
    img_path = './'+ str(img_path)
    img =  cv2.imread(img_path)
    # print(img.shape)

    # Resize image to appt proportion
    resized_img = rectangle.resize(img)

    # Extract table and change Perspective
    rect_img = rectangle.draw(resized_img)

    # Detect Horizontal Lines
    horizontal_lines = detectLines.detect(rect_img)
    # Detect Vertical Lines
    vertical_lines = vertical.detect(rect_img)

    # Create Cells and Call predictor on each cell
    xls_file = roi.create_row(rect_img,horizontal_lines,vertical_lines)

    xls_path = './media/results/Result.xlsx'
    return xls_path


    # cv2.imshow("Rectangle",rect_img)
    # cv2.imshow("Original",img)

#cv2.waitKey(0)
# cv2.destroyAllWindows()
