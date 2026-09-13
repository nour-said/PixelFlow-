import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def count_fingers(hand_landmarks, hand_label):

    fingers = 0

    # Index, Middle, Ring, Pinky
    finger_tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    finger_pips = [
        mp_hands.HandLandmark.INDEX_FINGER_PIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
        mp_hands.HandLandmark.RING_FINGER_PIP,
        mp_hands.HandLandmark.PINKY_PIP
    ]

    # Check four fingers
    for tip, pip in zip(finger_tips, finger_pips):

        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers += 1

    # Check thumb
    thumb_tip = hand_landmarks.landmark[
        mp_hands.HandLandmark.THUMB_TIP
    ]

    thumb_ip = hand_landmarks.landmark[
        mp_hands.HandLandmark.THUMB_IP
    ]

    if hand_label == "Right":
        if thumb_tip.x < thumb_ip.x:
            fingers += 1

    else:
        if thumb_tip.x > thumb_ip.x:
            fingers += 1

    return fingers

def get_hand_control(hand_landmarks):

    thumb = hand_landmarks.landmark[
        mp_hands.HandLandmark.THUMB_TIP
    ]

    index = hand_landmarks.landmark[
        mp_hands.HandLandmark.INDEX_FINGER_TIP
    ]

    # Distance between thumb and index
    dx = index.x - thumb.x
    dy = index.y - thumb.y

    distance = math.sqrt(dx ** 2 + dy ** 2)

    # Angle between thumb and index
    angle = math.degrees(math.atan2(dy, dx))

    return distance, angle


def normalize(value, min_value, max_value):

    value = max(min_value, min(value, max_value))

    return (value - min_value) / (max_value - min_value)

# Open webcam
cap = cv2.VideoCapture(0)

previous_strength = 0
alpha = 0.15

while True:

    ret, frame = cap.read()

    if not ret:
        print("Could not read from camera.")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Convert BGR → RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    results = hands.process(rgb_frame)

    # Draw hand landmarks
    if results.multi_hand_landmarks:

     for hand_landmarks, handedness in zip(
        results.multi_hand_landmarks,
        results.multi_handedness
     ):

        # Get hand label
       
        hand_label = handedness.classification[0].label

        if hand_label == "Right":

         distance, angle = get_hand_control(
         hand_landmarks
       )
        current_strength = normalize(
          distance,
          0.02,
          0.97
        )

        distortion_strength = (
          alpha * current_strength + (1 - alpha) * previous_strength
        )

        previous_strength = distortion_strength

        previous_rotation = 0
        rotation_alpha = 0.15

        current_rotation = angle / 180.0

        rotation = (
          rotation_alpha * current_rotation + (1 - rotation_alpha) * previous_rotation
        )

        previous_rotation = rotation

        
        cv2.putText(
          frame,
          f"Distance: {distance:.2f}",
          (30, 130),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.8,
          (0, 255, 0),
          2
        )

        cv2.putText(
          frame,
          f"Angle: {angle:.1f}",
          (30, 165),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.8,
          (0, 255, 0),
          2
       )


        if hand_label == "Left":

           finger_count = count_fingers(
            hand_landmarks,
            hand_label
        )

           if finger_count == 0:
            mode = "GRAYSCALE"

           elif finger_count == 1:
            mode = "RED"

           elif finger_count == 2:
            mode = "GREEN"

           elif finger_count == 3:
            mode = "BLUE"

           elif finger_count == 5:
            mode = "RGB"

           else:
            mode = "UNKNOWN"

           cv2.putText(
            frame,
            f"Fingers: {finger_count}",
            (30, 50),
          cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
            )

           cv2.putText(
              frame,
              f"Mode: {mode}",
              (30, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
               1,
               (0, 255, 0),
               2
            )

        # Draw landmarks
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

        # Get wrist position
        h, w, _ = frame.shape

        wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

        x = int(wrist.x * w)
        y = int(wrist.y * h)

        # Display Left / Right
        cv2.putText(
            frame,
            hand_label,
            (x, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
    # Show camera
    cv2.imshow("PixelFlow - Hand Tracking", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
hands.close()
cv2.destroyAllWindows()