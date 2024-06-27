import mss
import time
import numpy as np
import win32api
from Mouse import mouse_move
import keyboard


def get_pixel_color_from_center_screen(x, y, monitor):
    with mss.mss() as sct:
        # Grab a smaller region around the pixel
        region = {
            "left": monitor["left"] + x,
            "top": monitor["top"] + y,
            "width": 1,
            "height": 1,
        }
        screen = sct.grab(region)
        img = np.array(screen)
        color = img[0, 0, :3]
        return tuple(color)


def click_left():
    keyboard.press('e')
    mouse_move(1, 0, 0, 0)  # Mouse down
    time.sleep(0.03)
    mouse_move(0, 0, 0, 0)  # Mouse up
    keyboard.release('e')


# Example usage targeting the center monitor (index 1)
pixel_x = -1076  # Adjust as needed
pixel_y = 659    # Adjust as needed

pixel_x2 = -972
pixel_y2 = 750
primary_monitor_index = 1  # Assuming center monitor is index 1

with mss.mss() as sct:
    monitors = sct.monitors
    monitor = monitors[primary_monitor_index]

    while True:
        # Check if XButton1 (mouse button 5) is held down
        if win32api.GetAsyncKeyState(0x42):
            current_color = get_pixel_color_from_center_screen(
                pixel_x, pixel_y, monitor)
            print(f"Current color: {current_color}")

            if current_color != (0, 0, 0):
                second_color = get_pixel_color_from_center_screen(
                    pixel_x2, pixel_y2, monitor)

                if second_color == (0, 0, 0):
                    keyboard.press('r')
                    time.sleep(0.03)
                    keyboard.release('r')
                click_left()

                print(
                    f"Clicked at ({monitor['left'] + pixel_x}, {monitor['top'] + pixel_y}) because color {current_color} was detected.")

                # Wait until the color turns back to black
                while True:
                    current_color = get_pixel_color_from_center_screen(
                        pixel_x, pixel_y, monitor)
                    if current_color == (0, 0, 0):
                        break

                # Check if 'V' key is pressed
        if keyboard.is_pressed('v'):

            current_color = get_pixel_color_from_center_screen(
                pixel_x, pixel_y, monitor)
            print(f"Current color: {current_color}")

            if current_color != (0, 0, 0):
                # Simulate pressing and releasing the Shift key
                keyboard.press('shift')
                time.sleep(0.03)  # Adjust if necessary
                keyboard.release('shift')
                print(
                    f"Shift key pressed because color {current_color} was detected.")

                # Wait until the color turns back to black
                while True:
                    current_color = get_pixel_color_from_center_screen(
                        pixel_x, pixel_y, monitor)
                    if current_color == (0, 0, 0):
                        break
