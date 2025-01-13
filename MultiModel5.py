import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import numpy as np
from math import hypot
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85,
    max_num_hands=2,
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


def process_frame():
    ret, frame = cap.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = [
                (int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0]))
                for lm in hand_landmarks.landmark
            ]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            cv2.circle(frame, thumb_tip, 7, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, index_tip, 7, (0, 255, 0), cv2.FILLED)
            cv2.line(frame, thumb_tip, index_tip, (0, 255, 0), 3)

            length = hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])

            brightness_level = np.interp(length, [15, 220], [0, 100])
            sbc.set_brightness(int(brightness_level))

    return frame


def update_frame():
    if video_on:
        frame = process_frame()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)
            lbl_video.imgtk = frame
            lbl_video.configure(image=frame)
        root.after(10, update_frame)


def start_video():
    global video_on
    video_on = True
    update_frame()


def stop_video():
    global video_on
    video_on = False
    lbl_video.configure(image="")
    cap.release()


def on_closing():
    stop_video()
    cv2.destroyAllWindows()
    root.destroy()


root = tk.Tk()
root.title("Hand Tracking & Brightness Control System Developed By A&J")
root.geometry("1920x1080")
root.configure(bg="#343f71")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=on_closing)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About", "Hand Tracking & Brightness Control\nVersion 1.0\nDeveloped By A&J"
    ),
)

title_label = tk.Label(
    root,
    text="Hand Tracking & Brightness Control",
    font=("Arial", 30, "bold"),
    bg="#343f71",
    fg="#ffffff",
)
title_label.pack(pady=20)

lbl_video = tk.Label(root, bg="#343f71")
lbl_video.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

start_button = tk.Button(
    root,
    text="Start Video",
    command=start_video,
    font=("Arial", 15),
    bg="#009500",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
start_button.pack(side=tk.LEFT, padx=20, pady=50)

stop_button = tk.Button(
    root,
    text="Stop Video",
    command=stop_video,
    font=("Arial", 15),
    bg="#e74c3c",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
stop_button.pack(side=tk.RIGHT, padx=20, pady=50)

footer_label = tk.Label(
    root, text="Developed By A&J", font=("Arial", 15), bg="#343f71", fg="#ffea00"
)
footer_label.pack(side="bottom", pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
