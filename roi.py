import sys
import cv2
import pytesseract
import vertical
from keras.models import load_model
import rectangle
from Cell_test import printedText
#import Predict
import pandas as pd

def rowHeight(lines):          # Find average height of each row
    avgDistance = 0
    count=0
    if lines is None:
        return 0
    else:
        for idx,line in enumerate(lines):
            if idx == len(lines)-1:
                break

            avgDistance +=  max(lines[idx+1][0][1],lines[idx+1][0][3]) - min(line[0][1],line[0][3])
            count += 1

        avgDistance /= count
        return int(avgDistance)


def generateOutputFile(result):
    # print(result)
    df = pd.DataFrame(result)
    # print(df)
    df.to_csv("Output/Output.csv",sep=' ',encoding='utf_8',header=False,index=False,na_rep = '')

    dfNew = pd.read_csv("Output/Output.csv",sep=' ')
    writer = pd.ExcelWriter("Output/Result.xlsx")
    dfNew.to_excel(writer,index=False)
    writer.save()
    print("Output Generated")


def createRow(img,horizontalLines,verticalLines):        # Create Cells
    rowSize = rowHeight(horizontalLines)
    print("Row Height : " ,rowSize)
    row,col = img.shape[:-1]
    counter = 0
    model = load_model('Classifier/PA.h5')         # Load Model
    output=[]
    header = [["Roll No","Name "]]
    maxColCount = 0
    TA = []
    for index,line in enumerate(horizontalLines) :
        colCount = 0
        if index == len(horizontalLines)-1:
            # roi = img[line[0][1]:row,:,:]
            break
        else:
            roi = img[min(line[0][1],line[0][3]):max(horizontalLines[index+1][0][1],horizontalLines[index+1][0][3]),:,:]      # Create rows

        roiRow,roiCol,_ = roi.shape
        if roiRow > 10:
        # if roiRow > rowSize :
            # cv2.imshow("ROI",roi)
            # cv2.waitKey(0)

            counter += 1
            if counter > 3:
                # print()
                row = []
                cnt = 0


                currentAttendance = 0
                for idx,verLine in enumerate(verticalLines):
                    if idx == len(verticalLines)-1:
                        break
                    if cnt == 0:
                        cnt += 1
                        continue

                    cells = roi[:,verLine:verticalLines[idx+1]]           # Detect Cells in each row
                    cv2.imwrite("tempImg.jpg",cells)
                    # cv2.imshow("Cells",cells)
                    # cv2.waitKey(0)
                    text = printedText("tempImg.jpg",model)     # Get text in the cells
                    # print (text,end=' ')
                    if text != "":
                        colCount += 1
                        row.append(text)

                       
                    if text == '1':
                        currentAttendance += 1

                    # if cv2.waitKey(0) == ord('q'):
                        # sys.exit(0)

                if maxColCount < colCount:
                    maxColCount = colCount

                TA.append([currentAttendance])

    # Create Output Files
                output.append(row)


    for i in range(1,maxColCount-1):
        header[0].extend([i])

    header[0].extend(["Total Attendance"])
    print("Total Columns : " ,maxColCount)
    print(output)
    for i in range(len(TA)):
        TA[i][0] = str(round(TA[i][0]/(maxColCount-2) * 100,2))
        TA[i][0] += "%"

    for i in range(len(output)):
        curLen = len(output[i])
        if curLen != maxColCount:
            for j in range(maxColCount-curLen):
                output[i].append('A')


    for i in range(len(output)):
        output[i].append(TA[i][0])
    

    header.extend(output)
    generateOutputFile(header)