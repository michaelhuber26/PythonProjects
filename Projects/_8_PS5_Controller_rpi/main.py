# if you don't need to be wireless, check out the library pydualsense

import threading
import time
from typing import Container
from evdev import InputDevice, categorize, ecodes  # pip install evdev
import RPi.GPIO as GPIO


servoPIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

servo1 = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz

servo1.start(0)  # Initialisierung


gamepad = InputDevice(
    "/dev/input/event0"
)  # "cd /dev/input" then "ls -al" to see your connections

button_presses = {  # ecodes.EV_KEY
    304: "square",
    305: "x",
    306: "circle",
    307: "triangle",
    308: "L1",
    309: "R1",
    310: "L2",  # this shows up when the button clicks before the analog signals are reported
    311: "R2",
    312: "share",  # 3 vertical lines, top left side of touchpad
    313: "pause",  # 3 horizontal lines, top right of touchpad
    314: "L3",  # left joystick press down vertically
    315: "R3",
    316: "playstation",
    317: "touchpad",
}

button_values = {0: "up", 1: "down"}  # ecodes.EV_KEY button press values

absolutes = {  # ecodes.EV_ABS
    0: "left joystick left/right",  # 0 = left, 255 = right
    1: "left joystick up/down",  # 0 = up, 255 = down
    2: "right joystick left/right",  # 0 = left, 255 = right
    3: "L2 analog",  # 0 = no press, 255 = full press
    4: "R2 analog",  # 0 = no press, 255 = full press
    5: "right joystick up/down",  # 0 = up, 255 = down
    16: "leftpad left/right",  # -1 = left, 0 = stop pressing, 1 = right
    17: "leftpad up/down",  # -1 = up, 0 = stop pressing, 1 = down
}

leftpad_left_right_values = {
    -1: "left",
    0: "left-right stop",  # stoip means that the button was no longer pressed
    1: "right",
}

leftpad_up_down_values = {-1: "up", 0: "up-down stop", 1: "down"}

CENTER = 128
BLIND = 6  # there's a lot of drift at 128, so don't report changes within (128 - this value)
MAX_EMERGENCY_DELAY = 1000  # max number of milliseconds between taps to qualify as an emergency double-tap

emergency_tap_time = (
    0  # track when the last time the emergency button (touchpad) was pressed
)
left_joystick, right_joystick = [CENTER, CENTER], [CENTER, CENTER]


def update_left_joystick_position(event, value):
    global left_joystick
    if event.code == 0:  # left joystick, x-axis (left/right)
        left_joystick[0] = value
    elif event.code == 1:  # left joystick, y-axis (up/down)
        left_joystick[1] = value


def check_controller_event():
    for event in gamepad.read_loop():
        # print(categorize(event))
        # print(event)

        if (
            event.type == ecodes.EV_ABS and event.code in absolutes
        ):  # leftpad, joystick motion, or L2/R2 triggers
            action, value = absolutes[event.code], event.value

            if event.code in [0, 1, 2, 5]:  # joystick motion
                if event.code in [0, 1]:  # left joystick moving
                    update_left_joystick_position(event, value)

                if event.value > (CENTER - BLIND) and event.value < (
                    CENTER + BLIND
                ):  # skip printing the jittery center for the joysticks
                    continue

                print(f"{left_joystick}")
                return left_joystick[1]


def main():
    prev_dutycycle = 0
    try:
        while True:

            # Ask user for angle and turn servo to it ~20 - 165
            # controllerNum = float(input("Enter controller range (0 - 255)"))

            controllerNum = check_controller_event()

            angle = float(180 / 255) * controllerNum
            print(angle)

            dutycycle = 2 + (angle / 18)

            print(f"PrevDC: {prev_dutycycle}\t DC: {dutycycle}")

            servo1.ChangeDutyCycle(dutycycle)
            time.sleep(0.2)
            servo1.ChangeDutyCycle(0)

            prev_dutycycle = dutycycle

            # time.sleep(0.5)
            # servo1.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        servo1.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    # execute only if run as a script
    main()
