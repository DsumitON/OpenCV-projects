#!/usr/bin/python3
import numpy as np
import cv2

capture=cv2.VideoCapture(0)

fps=30

size=(int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size) #.avi
#video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('P','I','M','1'),fps,size) #.avi
#video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size) #.avi
video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('M','P','4','V'),fps,size) #.mp4
#video=cv2.VideoWriter('MyVideoOutput.mp4',cv2.VideoWriter_fourcc('X','2','6','4'),fps,size) #.mp4
#video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('T','H','E','O'),fps,size) #.ogv
#video=cv2.VideoWriter('MyVideoOutput.avi',cv2.VideoWriter_fourcc('F','L','V','1'),fps,size) #.flv


success,frame=capture.read()

remainingframe=10*fps-1 # 10 seconds

while success and remainingframe>0 and cv2.waitKey(1)==-1:
	cv2.imshow('MY Video', frame)
	video.write(frame)
	success,frame=capture.read()
	#print(capture.read())
	remainingframe -=1
	
cv2.destroyWindow('MY Video')
capture.release()
