import math

def detect_gesture(hand_landmarks):
    # Extract y-coordinates of finger tips for simplicity
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    lm = hand_landmarks.landmark

    # Open Palm: all fingers extended
    if all(lm[tip].y < lm[tip - 2].y for tip in tips_ids[1:]):  # index->pinky above joints
        return "Open Palm"

    # Fist: all fingers closed
    if all(lm[tip].y > lm[tip - 2].y for tip in tips_ids[1:]):
        return "Fist"

    # Peace: Index + Middle up, others down
    if (lm[8].y < lm[6].y and lm[12].y < lm[10].y and
        lm[16].y > lm[14].y and lm[20].y > lm[18].y):
        return "Peace"

    return "Unknown"
