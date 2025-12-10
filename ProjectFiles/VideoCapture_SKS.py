#!/usr/bin/python3
import numpy
import cv2

capture=cv2.VideoCapture(0) #camera capture

fps=30

size=(int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

VideoWriter=cv2.VideoWriter('sksVideo.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
#VideoWriter=cv2.VideoWriter('MyOutputVid.avi',0,fps,size)
success,frame=capture.read()
remainingframe=10*fps-1

while success and remainingframe >0:
	VideoWriter.write(frame)
	success,frame=capture.read()
	remainingframe -=1
	

