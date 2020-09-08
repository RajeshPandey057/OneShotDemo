import cv2
import numpy as np
import os
import dlib
from imutils import face_utils
from imutils.face_utils import FaceAligner
import easygui

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_aligner = FaceAligner(shape_predictor, desiredFaceWidth=200)
video_capture = cv2.VideoCapture(0)
name = easygui.enterbox("Enter Name", "DataSet Generator")
path = 'images'
directory = os.path.join(path, name)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok='True')
msg = "How do you want to add new data?"
title = "DataSet Generator"
choices = ["Live Video", "Upload Photo"]
choice = easygui.choicebox(msg, title, choices)
t = choice
number_of_images = 0
MAX_NUMBER_OF_IMAGES = 10
count = 0
if t == "Live Video":
    while number_of_images < MAX_NUMBER_OF_IMAGES:
        ret, frame = video_capture.read()

        frame = cv2.flip(frame, 1)

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame_gray)
        if len(faces) == 1:
            face = faces[0]
            (x, y, w, h) = face_utils.rect_to_bb(face)
            face_img = frame_gray[y - 50:y + h + 100, x - 50:x + w + 100]
            face_aligned = face_aligner.align(frame, frame_gray, face)

            if count == 5:
                cv2.imwrite(os.path.join(directory, str(name + str(number_of_images) + '.jpg')), face_aligned)
                number_of_images += 1
                count = 0
            count += 1

        cv2.imshow('Video', frame)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    video_capture.release()
    cv2.destroyAllWindows()

else:
    MAX_NUMBER_OF_IMAGES = 5
    path2 = easygui.fileopenbox()
    frame = cv2.imread(path2)
    while number_of_images < MAX_NUMBER_OF_IMAGES:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame_gray)
        if len(faces) == 1:
            face = faces[0]
            (x, y, w, h) = face_utils.rect_to_bb(face)
            face_img = frame_gray[y - 50:y + h + 100, x - 50:x + w + 100]
            face_aligned = face_aligner.align(frame, frame_gray, face)

            if count == 5:
                cv2.imwrite(os.path.join(directory, str(name + str(number_of_images) + '.jpg')), face_aligned)
                number_of_images += 1
                count = 0
            count += 1
