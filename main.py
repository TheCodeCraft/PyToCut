import cv2
import os

directory = "output"
parent_dir = os.path.abspath(os.getcwd())
path = os.path.join(parent_dir, directory)
os.mkdir(path)
vid = cv2.VideoCapture(input("filename: "))
frames = input("frames: ")
i = 0
while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break
    if i % int(frames) == 0:
        cv2.imwrite(directory + '/frame' + str(i) + '.png', frame)
    i += 1
    print("File: " + str(i))
vid.release()
cv2.destroyAllWindows()
