#imports
import cv2
import os

#dir
directory = "output"
parent_dir = os.path.abspath(os.getcwd())
path = os.path.join(parent_dir, directory)
#creating the dir
os.mkdir(path)
#input video
vid = cv2.VideoCapture(input("filename: "))
#input frames
frames = input("frames: ")
i = 0
i2 = 0
while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break
    if i % int(frames) == 0:
        #writing
        cv2.imwrite(directory + '/frame' + str(i2) + '.png', frame)
        i2 += 1
    i += 1
  print("File: " + str(i) + " Frame: " + str(i2))
#close
vid.release()
cv2.destroyAllWindows()
