import cv2
import sys
import numpy as np


#image = load_image('group_photo_small.jpg')
def load_image(imagePath, transparent=False):
	# Read the image
	if not transparent:
		image = cv2.imread(imagePath)
	else:
		image = cv2.imread(imagePath, -1)	
	
	return image
	
	
def find_faces_still(image, faceCascade):
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
	
	image_labeled = 1*image

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(image_labeled, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow("Faces found", image_labeled)
	input('press a key to continue')
	cv2.destroyAllWindows() 
	
	return faces
	


def find_faces(faceCascade):


	video_capture = cv2.VideoCapture(0)
	

	while True:
		# Capture frame-by-frame
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
		)

		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		# Display the resulting frame
		cv2.imshow('Video', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()




if __name__ == "__main__":
	cascPath = 'haarcascade_frontalface_default.xml'
	faceCascade = cv2.CascadeClassifier(cascPath)
	
	background_image = cv2.imread('group_photo_small.jpg')
	foreground_image = cv2.imread('carnival_mask.png', -1)	
	
	cv2.imshow('mask', foreground_image[:, :, 3])
	
	faces = find_faces_still(background_image, faceCascade)
	roi_fg = 0*background_image
	roi_bg = background_image
	
	for facen in range(len(faces)):
	
		#cv2.imshow('face1', background_image[faces[facen][1]:faces[facen][1]+faces[facen][3], faces[facen][0]:faces[facen][0]+faces[facen][2]])

		#resize foreground image so that it is the same width as facen
	
		new_h = int(1.0*faces[facen][3]/foreground_image.shape[1]* foreground_image.shape[0])
		foreground_image_rs = cv2.resize(foreground_image, (faces[facen][3],new_h))

		# Create foreground mask from alpha transparency.
		foreground_mask = foreground_image_rs[:, :, 3]
 
		# Create inverted background mask.
		background_mask = cv2.bitwise_not(foreground_mask)
 
		# Convert foreground image to BGR from BGRT
		foreground_image_rs = foreground_image_rs[:, :, 0:3]
 
		start_h = faces[facen][1]
		end_h = faces[facen][1]+foreground_mask.shape[0]
		start_w = faces[facen][0]
		end_w = faces[facen][0]+foreground_mask.shape[1]
	
		
		roi_bg[start_h:end_h, start_w:end_w] = cv2.bitwise_and(background_image[start_h:end_h, start_w:end_w], background_image[start_h:end_h, start_w:end_w], mask=background_mask)
	
		roi_fg[start_h:end_h, start_w:end_w] = cv2.bitwise_and(foreground_image_rs, foreground_image_rs, mask=foreground_mask)

	# Join the roi_bg and roi_fg.
	dst = cv2.add(roi_bg, roi_fg)
	
	cv2.imshow('combined', dst)
	cv2.imwrite('group_photo_snapchat.jpg', dst)

	#print('to stop capture make the video window the foreground window and press any key ')
	#find_faces(faceCascade)

	
	
	
	