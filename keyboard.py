import time
from pynput.keyboard import Listener, Controller as KeyboardController

# Function to monitor keyboard movement
def monitor_keyboard():
    # Create a keyboard controller
    keyboard = KeyboardController()

    # Define a callback function for keyboard events
    def on_press(key):
        print('Key {} pressed'.format(key))

    # Start listening to keyboard events
    with Listener(on_press=on_press) as listener:
        listener.join()

# Run the monitoring function
if __name__ == "__main__":
    print("Monitoring keyboard movement...")
    monitor_keyboard()
