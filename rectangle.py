import cv2
import numpy as np
from math import sqrt
from util import distance, edgeDetect

def deletePoints(approx,threshValue):
	# Delete redundant points while detection table from image
	idx= 0
	n = len(approx)
	while idx < n:
		idx2 = 0
		while idx2 < n:
			if approx[idx] == approx[idx2]:
				idx2 += 1
				continue

			if distance(approx[idx][0],approx[idx2][0]) < threshValue :
				# print ("Deleted")
				del approx[idx2]
				n -= 1
				continue

			idx2 += 1
		idx += 1
	return approx


def extractTable(inImg):
	row,col = inImg.shape[:-1]
	copy = inImg.copy()
	canny = edgeDetect(inImg)
	canny=cv2.dilate(canny, np.ones((7, 7), np.uint8), iterations=1)

	# Find contours on Image
	_, c, h = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	cMax = max(c, key = cv2.contourArea)
	# print(cMax)

	# Polygon Approximation to find corners of table
	epsilon = 0.05*cv2.arcLength(cMax,True)
	approx = cv2.approxPolyDP(cMax,epsilon,True).tolist()
	approx.sort(key = lambda x : sqrt(x[0][0]**2 + x[0][1]**2))
	# print("Points detected : " , len(approx))
	#deletePoints(approx,int(min(row,col)/10))
	# print("After deletion, : ", len(approx))

	x,y,w,h = cv2.boundingRect(cMax)		# Find the Bounding Rectangle
	# cv2.rectangle(inImg,(x,y),(x+w,y+h),(0,0,255),2)


	for i in approx :
		cv2.circle(inImg,(i[0][0],i[0][1]),5,(0,255,0),-1)		# Draw Table corners

	if len(approx)==4:
		print ("Table Detected")

		pts1 = np.float32([i[0] for i in approx])
		# print (pts1)
		if w>=h:		# Horizontal Table
			print ("Horizontal")
			pts2 = np.float32([[0,0],[0,h],[w,0],[w,h]])
			M = cv2.getPerspectiveTransform(pts1,pts2)
			roi = cv2.warpPerspective(inImg,M,(w,h))
		else:
			print ("Vertical")		# Vertical Table
			pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
			M = cv2.getPerspectiveTransform(pts1,pts2)
			roi = cv2.warpPerspective(inImg,M,(w,h))

	else:
		print("Returning original Image, Points : ",len(approx))
		cv2.drawContours(inImg, cMax, -1, (255, 0, 0), 1)
		roi = copy

	#cv2.imshow("Input",inImg)
	# cv2.waitKey(0)
	return roi
