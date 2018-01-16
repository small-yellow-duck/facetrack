'''
Q1: within ipython do
	run facedetect.py group_photo_large.jpg 
    run facedetect.py group_photo_small.jpg
    how are the results different?
    
Q2: what happens if you adjust the value of the scaleFactor parameter passed to faceCascade.detectMultiScale?
Q3: modify find_faces to check if the image is already grey-scale
Q4: after you run find_faces, use cv2.imshow() to view the contents of 'image'.... did the function add green squares? Modify find_faces so that it does not change the original image.
Q5: What are the current dimensions of the image? Add a line to __main__ that prints the image dimensions.
Q6: modify find_faces so that the image shown doesn't have a dimension larger than 800 pixels. Do you want to resize the image before or after the face detection routine runs?

'''


import cv2
import sys

	
def find_faces(image, faceCascade):
	#the haar cascade algorithm requires greyscale images as input
	#convert image to greyscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow("Faces found", image)
	input('press a key to continue')
	cv2.destroyAllWindows() 
	

def getCasc():
	# Get user supplied values
	cascPath = 'haarcascade_frontalface_default.xml'

	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)
	
	return faceCascade




#run facedetect.py group_photo_small.jpg
#commenting out the the 'main' statement allows you to work with the functions in ipython
if __name__ == "__main__":
	imagePath = sys.argv[1]

	image = cv2.imread(imagePath)
	faceCascade = getCasc()

	find_faces(image, faceCascade)
	
	
#max_x, max_y = 800, 800
#yscale = min([max_y/image.shape[0], 1.0])
#xscale = min([max_x/image.shape[1], 1.0])
#scale = min([xscale, yscale])
#image2 = cv2.resize(image, (0,0), fx=scale, fy=scale)
	

