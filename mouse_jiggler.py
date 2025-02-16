import pyautogui
import time
import threading
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import ctypes
import random
import string


class MouseJigglerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Jiggler")

        # Variables
        self.jiggling = False
        self.thread = None

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_jiggling)
        self.start_button.pack(pady=10)

        # Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_jiggling, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Add GIF image
        self.gif_label = tk.Label(self.root)
        self.gif_label.pack(pady=20)

        self.load_gif("mouse_shaking_ass.gif")  # Provide the path to the gif file








    def jiggle_mouse_and_keyboard(self):
        x, y = pyautogui.position()
        while self.jiggling:
            # Move the mouse to simulate activity
            pyautogui.moveTo(x + 1, y)
            time.sleep(0.5)
            pyautogui.moveTo(x, y)
            time.sleep(0.5)

            # Simulate keyboard activity to avoid "away" status in Skype
            self.simulate_keyboard_activity()

            # Prevent the system from going to sleep
            self.prevent_sleep()

    def simulate_keyboard_activity(self):
        # Simulate a random keyboard key press (Shift key is a common choice)
        pyautogui.write(random.choice(string.ascii_letters), interval=0.1)

    def prevent_sleep(self):
        # Windows API call to prevent system sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    def start_jiggling(self):
        # Disable the Start button and enable the Stop button
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Set jiggling flag to True
        self.jiggling = True

        # Start the jiggling in a separate thread to keep the UI responsive
        self.thread = threading.Thread(target=self.jiggle_mouse_and_keyboard)
        self.thread.start()

    def stop_jiggling(self):
        # Disable the Stop button and enable the Start button
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

        # Set jiggling flag to False to stop the loop
        self.jiggling = False

        # Wait for the jiggling thread to finish
        if self.thread is not None:
            self.thread.join()


# Create the main Tkinter window
root = tk.Tk()

# Create the MouseJigglerApp instance
app = MouseJigglerApp(root)

# Start the Tkinter main loop
root.mainloop()
