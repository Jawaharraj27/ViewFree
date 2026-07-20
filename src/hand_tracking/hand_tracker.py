import cv2
import mediapipe as mp
import sys
import os

# =====================================================
# Add project root path
# =====================================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from src.gesture_engine.gesture import detect_gesture
from src.gesture_engine.pinch import detect_pinch
from src.action_engine.action import perform_action
from src.cursor_engine.cursor import get_cursor_position
from src.ui.view_orb import draw_view_orb
from src.ui.radial_menu import draw_radial_menu
from src.ui.menu_selector import get_selected_menu
from src.app_manager.app_manager import ApplicationManager
from src.ui.menu_animation import update_menu_animation
from src.ui.selection_progress import update_selection


# =====================================================
# MediaPipe Initialization
# =====================================================

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# =====================================================
# Finger Detection Function
# =====================================================

def get_finger_states(hand_landmarks):

    landmarks = hand_landmarks.landmark

    fingers = {}

    # Thumb
    fingers["Thumb"] = landmarks[4].x > landmarks[3].x

    # Index
    fingers["Index"] = landmarks[8].y < landmarks[6].y

    # Middle
    fingers["Middle"] = landmarks[12].y < landmarks[10].y

    # Ring
    fingers["Ring"] = landmarks[16].y < landmarks[14].y

    # Pinky
    fingers["Pinky"] = landmarks[20].y < landmarks[18].y

    return fingers


# =====================================================
# Camera Setup
# =====================================================

camera = cv2.VideoCapture(0)

# Application Manager
app_manager = ApplicationManager()

# Cursor smoothing
smooth_x = 0
smooth_y = 0

SMOOTHING = 0.2


# =====================================================
# Main Loop
# =====================================================

while True:

    success, frame = camera.read()

    if not success:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect hands
    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            height, width, _ = frame.shape

            # -----------------------------------------
            # Finger Detection
            # -----------------------------------------

            finger_states = get_finger_states(
                hand_landmarks
            )

            # -----------------------------------------
            # Gesture Detection
            # -----------------------------------------

            gesture = detect_gesture(
                finger_states
            )

            # -----------------------------------------
            # Pinch Detection
            # -----------------------------------------

            pinch = detect_pinch(
                hand_landmarks
            )

            # -----------------------------------------
            # Action Engine
            # -----------------------------------------

            action = perform_action(
                gesture,
                pinch
            )

            # -----------------------------------------
            # Cursor Position
            # -----------------------------------------

            cursor_x, cursor_y = get_cursor_position(
                hand_landmarks,
                width,
                height
            )

            # Smooth Cursor
            smooth_x = int(
                smooth_x +
                (cursor_x - smooth_x) * SMOOTHING
            )

            smooth_y = int(
                smooth_y +
                (cursor_y - smooth_y) * SMOOTHING
            )

            # -----------------------------------------
            # Draw Hand Skeleton
            # -----------------------------------------

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # -----------------------------------------
            # Draw Cursor / Orb
            # -----------------------------------------

            # Fixed View Orb Position
            orb_x = width // 2
            orb_y = height // 2

            draw_view_orb(
                frame,
                orb_x,
                orb_y,
                pinch
            )

            selected_menu = None
            selection_progress = 0.0

            progress = update_menu_animation(pinch)

            if pinch:

                selected_menu = get_selected_menu(
                    smooth_x,
                    smooth_y,
                    orb_x,
                    orb_y
                )

                opened_app, selection_progress = update_selection(
                    selected_menu
                )

                if opened_app is not None:
                    app_manager.switch_app(opened_app)

                draw_radial_menu(
                    frame,
                    orb_x,
                    orb_y,
                    selected_menu,
                    progress,
                    selection_progress
                )

            current_app = app_manager.get_current_app()
            app_manager.render(frame)

            # -----------------------------------------
            # Draw Landmark Points
            # -----------------------------------------

            for idx, landmark in enumerate(
                hand_landmarks.landmark
            ):

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 0, 255),
                    -1
                )

                cv2.putText(
                    frame,
                    str(idx),
                    (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1
                )

            # -----------------------------------------
            # Debug Information
            # -----------------------------------------

            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Pinch: {'YES' if pinch else 'NO'}",
                (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Action: {action}",
                (10, 85),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Cursor: ({smooth_x}, {smooth_y})",
                (10, 115),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"App: {current_app}",
                (10, 145),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # -----------------------------------------
            # Finger States
            # -----------------------------------------

            y_offset = 180

            for finger, state in finger_states.items():

                text = f"{finger}: {'Open' if state else 'Closed'}"

                cv2.putText(
                    frame,
                    text,
                    (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

                y_offset += 30

    # =================================================
    # Show Camera
    # =================================================

    cv2.imshow(
        "ViewFree Hand Tracking",
        frame
    )

    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# =====================================================
# Cleanup
# =====================================================

camera.release()
cv2.destroyAllWindows()