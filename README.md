# Real-Time Static Hand Gesture Recognition

## Overview
This project implements a **real-time hand gesture recognition system** using **OpenCV** and **MediaPipe**. The application uses a webcam feed to detect hand landmarks and classify them into predefined static gestures:
- Open Palm
- Fist
- Peace Sign
- Thumbs Up

The system runs in real time and overlays the recognized gesture on the video feed.

## Dataset & Preprocessing
No external dataset was required. Instead, the system leverages **MediaPipe Hands** to extract 21 key landmarks from the hand in each frame. These landmarks are then used in simple **rule-based logic** to classify gestures:
- Landmark positions are compared (e.g., fingertip vs. finger joint).
- Finger states (open/closed) are determined.
- A combination of finger states is mapped to a gesture.

This approach avoids the need for manual data collection and training.

## Model / Gesture Logic
- **Framework:** MediaPipe for landmark detection.
- **Logic:** Rule-based gesture classification using landmark geometry.

### Rules Used:
- **Open Palm:** All five fingers extended.
- **Fist:** All fingers folded.
- **Peace Sign:** Index and middle extended, others folded.

## Training & Results
Since this is a **rule-based system**, no explicit model training was required.
The system achieves **real-time performance (~30 FPS)** on a standard laptop webcam.


## Demo
A short screen recording of the application running in real time is provided:
[Demo Video]

## Setup & Usage
1. Clone the repository:
   ```bash
   git clone <your-repo>
   cd hand_gesture_recognition
