## This file contains generic methods that may be used by multiple modules in future 


def resize(inImg):
	# Resize image to appt size
	row,col = inImg.shape[:-1]
	if row > 2000 or col > 2000:
		inImg = cv2.resize(inImg,(int(col/2),int(row/2)),interpolation = cv2.INTER_CUBIC)

	return inImg

def edgeDetect(inImg):
	# Thresh using Edge Detection
	cv2.GaussianBlur(inImg,(5,5),1)
	gray = cv2.cvtColor(inImg,cv2.COLOR_BGR2GRAY)
	canny = cv2.Canny(inImg,100,200)
	cv2.GaussianBlur(canny,(5,5),1)
	return canny

def slope(line):            # Find Slope of line
    if line[0][0] == line[0][2]:
        return 90
    return math.degrees(math.atan(abs(line[0][1] - line[0][3])/abs(line[0][0] - line[0][2])))

def thresh(inImg):
	# Thresh using Adaptive Thresholding
	cv2.GaussianBlur(inImg,(5,5),1)
	gray = cv2.cvtColor(inImg,cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	cv2.GaussianBlur(thresh,(5,5),1)
	return thresh

def distance(pt1,pt2):	# Find distance between 2 points
	return sqrt((pt1[0]-pt2[0])**2 + (pt1[1] - pt2[1])**2 )