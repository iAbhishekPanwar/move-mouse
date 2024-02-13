import time
import pyautogui

# Function to monitor mouse movement
def monitor_mouse():
    # Get the initial position of the mouse
    last_mouse_position = pyautogui.position()

    while True:
        # Pause for a short time to reduce CPU usage
        time.sleep(0.5)
        
        # Get the current position of the mouse
        current_mouse_position = pyautogui.position()

        # Check if the mouse has moved
        if current_mouse_position != last_mouse_position:
            print("Mouse active")
        else:
            print("Mouse idle")

        # Update the last known mouse position
        last_mouse_position = current_mouse_position

# Run the monitoring function
if __name__ == "__main__":
    print("Monitoring mouse movement...")
    monitor_mouse()
