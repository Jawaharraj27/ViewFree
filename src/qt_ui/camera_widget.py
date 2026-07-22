import cv2
import mediapipe as mp

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class CameraWidget(QLabel):

    def __init__(self):

        super().__init__()


        # ---------- UI SETTINGS ----------

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumSize(860, 540)

        self.setStyleSheet("""
            QLabel{
                background:#000000;
                border-radius:15px;
                border:1px solid #444;
            }
        """)



        # ---------- CAMERA ----------

        self.camera = cv2.VideoCapture(0)


        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            1280
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            720
        )


        if not self.camera.isOpened():

            raise RuntimeError(
                "Camera could not open"
            )




        # ---------- MEDIAPIPE ----------

        self.mp_hands = mp.solutions.hands

        self.mp_draw = mp.solutions.drawing_utils



        self.hands = self.mp_hands.Hands(

            static_image_mode=False,

            max_num_hands=2,

            min_detection_confidence=0.7,

            min_tracking_confidence=0.7

        )



        # ---------- GESTURE MEMORY ----------

        self.previous_gesture = "NONE"

        self.current_gesture = "NONE"

        self.gesture_counter = 0

        self.required_frames = 5




        # ---------- TIMER ----------

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_frame
        )

        self.timer.start(30)





    # ==================================================
    # MAIN CAMERA LOOP
    # ==================================================


    def update_frame(self):


        success, frame = self.camera.read()


        if not success:

            return



        frame = cv2.flip(
            frame,
            1
        )



        rgb = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )


        results = self.hands.process(
            rgb
        )


        gesture = "NO HAND"

        action = "WAIT"




        if results.multi_hand_landmarks:


            for hand in results.multi_hand_landmarks:


                # Draw landmarks

                self.mp_draw.draw_landmarks(

                    frame,

                    hand,

                    self.mp_hands.HAND_CONNECTIONS

                )



                landmarks = self.extract_landmarks(

                    hand,

                    frame

                )



                fingers = self.count_fingers(

                    landmarks

                )



                detected_gesture = self.recognize_gesture(

                    fingers

                )



                gesture = self.stabilize_gesture(

                    detected_gesture

                )



                action = self.perform_action(

                    gesture

                )




        # ---------- TEXT DISPLAY ----------


        cv2.putText(

            frame,

            "Gesture : " + gesture,

            (30,50),

            cv2.FONT_HERSHEY_SIMPLEX,

            1.2,

            (0,255,0),

            3

        )


        cv2.putText(

            frame,

            "Action  : " + action,

            (30,100),

            cv2.FONT_HERSHEY_SIMPLEX,

            1.2,

            (255,255,0),

            3

        )



        self.display_frame(frame)





    # ==================================================
    # LANDMARK EXTRACTION
    # ==================================================


    def extract_landmarks(self, hand, frame):


        landmarks=[]


        h,w,_ = frame.shape



        for id,lm in enumerate(hand.landmark):


            x=int(lm.x*w)

            y=int(lm.y*h)


            landmarks.append(

                (id,x,y)

            )


        return landmarks






    # ==================================================
    # FINGER DETECTION
    # ==================================================


    def count_fingers(self, landmarks):


        fingers=[]



        # Thumb

        if landmarks[4][1] < landmarks[3][1]:

            fingers.append(1)

        else:

            fingers.append(0)



        # Four fingers

        tips=[8,12,16,20]



        for tip in tips:


            if landmarks[tip][2] < landmarks[tip-2][2]:

                fingers.append(1)

            else:

                fingers.append(0)



        return fingers






    # ==================================================
    # GESTURE RECOGNITION
    # ==================================================


    def recognize_gesture(self,fingers):


        if fingers == [1,1,1,1,1]:

            return "OPEN PALM"



        elif fingers == [0,0,0,0,0]:

            return "FIST"



        elif fingers == [1,0,0,0,0]:

            return "THUMBS UP"



        elif fingers == [0,1,1,0,0]:

            return "PEACE"



        elif fingers == [0,1,0,0,0]:

            return "POINT"



        else:

            return "UNKNOWN"







    # ==================================================
    # STABILITY FILTER
    # ==================================================


    def stabilize_gesture(self,gesture):


        if gesture == self.previous_gesture:

            self.gesture_counter += 1


        else:

            self.gesture_counter = 0



        self.previous_gesture = gesture



        if self.gesture_counter >= self.required_frames:


            self.current_gesture = gesture



        return self.current_gesture






    # ==================================================
    # ACTION ENGINE (FIXED)
    # ==================================================


    def perform_action(self,gesture):


        if gesture == "OPEN PALM":

            return "READY"



        elif gesture == "FIST":

            return "PAUSED"



        elif gesture == "THUMBS UP":

            return "CONFIRMED"



        elif gesture == "PEACE":

            return "MODE CHANGE"



        elif gesture == "POINT":

            return "SELECT"



        else:

            return "WAIT"






    # ==================================================
    # DISPLAY
    # ==================================================


    def display_frame(self,frame):


        rgb=cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )


        rgb=rgb.copy()


        h,w,ch=rgb.shape



        image=QImage(

            rgb.data,

            w,

            h,

            ch*w,

            QImage.Format_RGB888

        )



        pixmap=QPixmap.fromImage(
            image
        )



        self.setPixmap(

            pixmap.scaled(

                self.size(),

                Qt.IgnoreAspectRatio,

                Qt.SmoothTransformation

            )

        )






    def closeEvent(self,event):


        if self.camera.isOpened():

            self.camera.release()



        self.hands.close()



        event.accept()