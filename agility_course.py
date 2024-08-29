import pyautogui
import time
import random
import cv2
import numpy as np

"Sleep for a random amount of time between min_time and max_time."
def random_sleep(min_time, max_time):
    sleep_time = random.uniform(min_time, max_time)
    time.sleep(sleep_time)

"Randomly offset the target click location to simulate human error." #Update
def random_misclick(x, y, max_offset=5):
    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)
    return x + offset_x, y + offset_y

"Move the mouse in a human-like curved path to the target location."
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5), tween=pyautogui.easeInOutQuad)

"Click at the given coordinates with random misclicks."
def click(x, y):
    target_x, target_y = random_misclick(x, y)
    move_mouse(target_x, target_y)
    pyautogui.click()

"Capture a screenshot of the screen for object detection."
def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

"Find the location of a specific object on the screen using template matching."
def find_object_on_screen(template_path):
    screenshot = capture_screen()
    template = cv2.imread(template_path, 0)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # Add a threshold to determine if a match is found
    threshold = 0.8
    if max_val > threshold:
        return max_loc
    return None

"Main function to perform an automated action."
def perform_action():
    
    # Example: Finding a specific object on the screen
    object_location = find_object_on_screen("path/to/your/template.png")
    if object_location:
        x, y = object_location
        click(x, y)
        random_sleep(1, 3)  # Random sleep between 1 to 3 seconds

while True:
    perform_action()
    random_sleep(10, 20)  # Wait for a random period between actions
