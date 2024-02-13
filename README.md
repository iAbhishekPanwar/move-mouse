# User Activity Monitor and Simulator

This program **moves the mouse** or presses a key when it detects that you are **away** from your computer.

It does nothing if you are using your computer, making it useful for **tricking your machine into thinking you are still using it**.

This project consists of three Python scripts: **abhishek.py**, **mouse.py**, and **keyboard.py**. These scripts are designed to monitor user activity and simulate activity to prevent systems from going idle. Below, you'll find instructions on how to install, set up, and use each script

# Manual installation

```
git clone https://github.com/iAbhishekPanwar/move-mouse.git

cd move-mouse

```

### Run

```
python3 abhishek.py
```

## Optional arguments

```
-h, --help                        show this help message and exit

-s SECONDS, --seconds SECONDS     Define in seconds how long to wait after a user is
                                  considered idle. Default 300.

-p PIXELS, --pixels PIXELS        Set how many pixels the mouse should move. Default 1.

-c, --circular                    Move mouse in a circle. Default move diagonally.

-m MODE, --mode MODE              Available options: keyboard, mouse, both (mouse & keyboard) and scroll.
                                  Default is mouse.
                                  This is the action that will be executed when the user is idle.
                                  If keyboard is selected, the program will press the shift key.
                                  If mouse is selected, the program will move the mouse.
                                  If both is selected, the program will do both actions.

-r RANDOM RANDOM, --random RANDOM RANDOM
                                  Usage: two numbers (ex. -r 3 10). Execute actions based on a
                                  random interval between start and stop seconds.
                                  Note: Overwrites the seconds argument.

```

# mouse.py

## Overview

mouse.py monitors mouse movement and prints whether the mouse is active or idle.

### Setup

You can run the script with the following command:

```
python3 mouse.py
```

# keyboard.py

## Overview

keyboard.py monitors keyboard events and prints the keys pressed.

## Setup

You can run the script with the following command:

```
python keyboard.py
```
