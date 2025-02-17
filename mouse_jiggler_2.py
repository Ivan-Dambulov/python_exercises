import pyautogui
import time
import random
import ctypes  # For preventing sleep (Windows)

# Function to prevent sleep on Windows
def prevent_sleep():
    # This will prevent the system from entering sleep mode
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

def jiggle_and_shift_click_mouse():
    prevent_sleep()  # Prevent sleep at the start

    while True:
        # Get the current position of the mouse
        x, y = pyautogui.position()

        # Move the mouse slightly in random directions
        new_x = x + random.randint(-10, 10)  # Random horizontal movement

        # Move the mouse to the new position
        pyautogui.moveTo(new_x)

        # Randomly decide whether to Shift-click
        if random.random() < 0.2:  # 20% chance to Shift-click
            # Hold down the 'Shift' key, click the mouse, and release 'Shift'
            pyautogui.keyDown('shift')  # Hold down the Shift key
            pyautogui.keyUp('shift')    # Release the Shift key
            print("Shift-clicked!")
            pyautogui.click()           # Perform the click while holding Shift
            print("mouse-clicked!")
        # Wait for a few seconds before jiggling again
        time.sleep(random.uniform(2, 5))  # Wait time between jiggling

if __name__ == "__main__":
    print("Starting mouse jiggler with exceShift-click and preventing sleep. Press Ctrl+C to stop.")
    jiggle_and_shift_click_mouse()
