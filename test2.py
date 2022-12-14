import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        print(results.face_landmarks)
        

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw face landmarks

        #for connecting all the points
        # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

        #just the outlines of the face
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, 
        
                                mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1))
        
                        
        cv2.imshow('My Cam ', image)

        if (cv2.waitKey(10) & 0xFF ==ord ('q')):
            break

cap.release()
cv2.destroyAllWindows()