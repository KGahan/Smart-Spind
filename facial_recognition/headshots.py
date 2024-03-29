import cv2
import time
import os

def make_headshots(name):
    print("make headshots")
    if not os.path.exists("./facial_recognition/dataset/" + str(name)):
        os.mkdir("./facial_recognition/dataset/" + str(name))
    cam = cv2.VideoCapture(0, cv2.CAP_V4L)

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0
    
    while img_counter < 20:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)
        
        img_name = "./facial_recognition/dataset/"+ str(name) +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        time.sleep(0.5)
        
    cam.release()
    cv2.destroyAllWindows()
