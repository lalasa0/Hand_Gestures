import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Open webcam
cap = cv2.VideoCapture(0)

# Timer
start_time = time.time()
max_duration = 30  # seconds

def classify_gesture(landmarks):
    """Classify basic hand gestures: Palm, Fist, Peace."""
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    fingers_up = []
    for tip, pip in zip(finger_tips, finger_pips):
        if landmarks[tip].y < landmarks[pip].y:  # finger extended
            fingers_up.append(1)
        else:
            fingers_up.append(0)

    # Thumb check
    if landmarks[4].x < landmarks[3].x:
        fingers_up.insert(0, 1)
    else:
        fingers_up.insert(0, 0)

    # Classification rules
    if sum(fingers_up) == 0:
        return "Fist"
    elif sum(fingers_up) == 5:
        return "Palm"
    elif fingers_up[1] == 1 and fingers_up[2] == 1 and sum(fingers_up) == 2:
        return "Peace"
    else:
        return "Unknown"

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture = "No Hand"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = classify_gesture(hand_landmarks.landmark)

    cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Recognition", frame)

    # Quit if 'q' pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Quit if time exceeds max_duration
    if time.time() - start_time > max_duration:
        print("⏳ Auto-stopped after 30 seconds.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
