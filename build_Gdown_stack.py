# Build the GDown_stack
from numpy import *
import cv


def build_Gdown_stack(video_file, startIndex, endIndex, level):

    # Read with ffvideo
    video = ffvideo.VideoStream(video_file)

    video_height = video.frame_height
    video_width = video.width
    nChannels = 3

    capture = cv.CaptureFromFile(video_file)

    img = cv.QueryFrame(capture)
    tmp = cv.CreateImage(cv.GetSize(img),8,3)
    cv.CvtColor(img,tmp,cv.CV_BGR2RGB)
    frame = asarray(cv.GetMat(tmp))

    blurred = blurDnClr(frame,level)

    for i in range(startIndex + 1, endIndex):
        img = cv.QueryFrame(capture)
        tmp = cv.CreateImage(cv.GetSize(img),8,3)
        cv.CvtColor(img,tmp,cv.CV_BGR2RGB)
        frame = asarray(cv.GetMat(tmp))

    GDown_stack = zeros(endIndex - startIndex +1, size(blurred,axis=0),size(blurred,axis=1),size(blurred,axis=2))

