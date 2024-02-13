# User Activity Monitor and Simulator

## Overview

This project consists of three Python scripts: `abhishek.py`, `mouse.py`, and `keyboard.py`. These scripts are designed to monitor user activity and simulate activity to prevent systems from going idle. Below, you'll find instructions on how to install, set up, and use each script.

## Installation

To use the scripts, you'll need Python installed on your system. If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/).

After installing Python, you can follow these steps to set up the project:

1. Clone the repository or download the script files directly.
2. Navigate to the directory where you saved the files.
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
abhishek.py
Overview
abhishek.py is the main script that monitors user activity and simulates mouse movement, mouse wheel scroll, and keyboard press to prevent system idle.

Setup
You can run the script with the following command:

bash
Copy code
python abhishek.py [options]
Options
-s, --seconds: Define in seconds how long to wait after a user is considered idle. Default is 300 seconds.
-p, --pixels: Set how many pixels the mouse should move. Default is 1.
-c, --circular: Move the mouse in a circular pattern. By default, it moves diagonally.
-m, --mode: Available options are keyboard, mouse, both, and scroll. Default is mouse. This option determines the action taken when the user is idle.
-r, --random: Execute actions based on a random interval between start and stop seconds. Overrides the -s, --seconds argument.
Example
To run the script with a mouse delay of 2 seconds:

bash
Copy code
python abhishek.py --seconds 2
mouse.py
Overview
mouse.py monitors mouse movement and prints whether the mouse is active or idle.

Setup
You can run the script with the following command:

bash
Copy code
python mouse.py
keyboard.py
Overview
keyboard.py monitors keyboard events and prints the keys pressed.

Setup
You can run the script with the following command:

bash
Copy code
python keyboard.py
Feel free to explore and customize the scripts according to your requirements! If you encounter any issues or have suggestions for improvements, please let me know.
```
