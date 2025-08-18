import cv2
import mediapipe as mp
import subprocess
import time
import os
import pyautogui  # pip install pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

chrome_process = None  # To store Google Chrome process
last_action_time = 0   # Prevent rapid repeated actions

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process hands
        results = hands.process(rgb)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks with connecting lines and dots
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
                )

                # Count fingers
                tips = [8, 12, 16, 20]  # Index, middle, ring, pinky tips
                if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    finger_count += 1  # Thumb
                for tip in tips:
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                        finger_count += 1

        # Display finger count
        cv2.putText(frame, f"Fingers: {finger_count}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Prevent rapid actions
        current_time = time.time()
        if current_time - last_action_time > 1:  # 1-second delay
            if finger_count == 1 and chrome_process is None:
                chrome_process = subprocess.Popen(["start", "chrome", "https://google.com"], shell=True)
                print("Open Google Chrome")
                last_action_time = current_time

            elif finger_count == 2:
                pyautogui.hotkey("ctrl", "right")  # Next track in Spotify
                print("Next track in Spotify")
                last_action_time = current_time

            elif finger_count == 3 and chrome_process is not None:
                pyautogui.hotkey("ctrl", "t")  # Open new tab in Chrome
                print("New tab in Google Chrome")
                last_action_time = current_time

            elif finger_count == 4 and chrome_process is not None:
                os.system("taskkill /im chrome.exe /f")
                chrome_process = None
                print("Close Google Chrome")
                last_action_time = current_time

            elif finger_count == 5 and chrome_process is not None:
                pyautogui.hotkey("ctrl", "w")  # Close current tab
                print("Close current tab in Google Chrome")
                last_action_time = current_time

        # Show the frame
        cv2.imshow("Finger Detection", frame)

        # Press ESC to exit program
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()


