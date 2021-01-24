import cv2
import numpy as np
from backend.processor.roi import createRow
from backend.processor.rectangle import extractTable
from backend.processor.util import resize
from backend.processor.detectLines import detectHorizontal
from backend.processor.vertical import detectVertical

def convert(img_path):
    img_path = './'+ str(img_path)
    img =  cv2.imread(img_path)
    #print(img.shape)

    # Resize image to appt proportion
    resizedImg = resize(img)

    # Extract table and change Perspective
    rectImg = extractTable(resizedImg)

    # Detect Horizontal Lines
    horizontalLines = detectHorizontal(rectImg)
    # Detect Vertical Lines
    verticalLines = detectVertical(rectImg)

    # Create Cells and Call predictor on each cell
    createRow(rectImg,horizontalLines,verticalLines)

    xls_path = './media/results/Result.xlsx'
    return xls_path



    #cv2.imshow("Rectangle",rectImg)
    #cv2.imshow("Original",img)

# except AttributeError:
#     print("Enter valid Image name")

# #cv2.waitKey(0)
# cv2.destroyAllWindows()
