from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time
import cv2

def recognize_face(target_name):
    # Initialize 'currentname' to trigger only when a new person is identified.
    currentname = "unknown"
    # Determine faces from encodings.pickle file model created from train_model.py
    encodingsP = "./facial_recognition/encodings.pickle"

    # load the known faces and embeddings along with OpenCV's Haar cascade for face detection
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())

    # initialize the video stream and allow the camera sensor to warm up
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    # loop over frames from the video stream
    while True:
        # grab the frame from the threaded video stream and resize it
        frame = vs.read()
        frame = imutils.resize(frame, width=500)

        # detect the face boxes
        boxes = face_recognition.face_locations(frame)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known encodings
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"  # if face is not recognized, then print Unknown

            # check if we have found a match
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                print("matches")
                print(matches)
                # loop over the matched indexes and maintain a count for each recognized face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number of votes
                name = max(counts, key=counts.get)
                print(name)
                print(counts[name])
                if counts[name] <= 15:
                    name = "Unknown"
                print(name)
                # If the given name is found, return True
                if str(name) == str(target_name):
                    print("found face, return")
                    vs.stop()
                    return True

            # update the list of names
            names.append(name)