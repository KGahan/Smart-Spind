import cv2
import time

name = 'Kim' #replace with your name

def make_headshots():
    cam = cv2.VideoCapture(0, cv2.CAP_V4L)

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0
    
    while img_counter < 10:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)
        
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        time.sleep(0.5)
        
    cam.release()
    cv2.destroyAllWindows()

make_headshots()
