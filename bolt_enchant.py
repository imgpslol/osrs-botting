import pyautogui
import time
import random

# Function to perform a randomized delay
def random_delay(min_time=0.5, max_time=1.5):
    time.sleep(random.uniform(min_time, max_time))

# Function to move the mouse to a specific location with randomness
def move_and_click(x, y):
    pyautogui.moveTo(x + random.randint(-5, 5), y + random.randint(-5, 5), duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    random_delay()

# Main loop to enchant bolts
def enchant_bolts():
    # Example coordinates (these should be the actual coordinates on your screen)
    enchant_spell_location = (1000, 500)  # Replace with actual coordinates of enchant spell
    bolts_location = (1100, 600)          # Replace with actual coordinates of bolts

    # Example loop for enchanting a stack of bolts
    for _ in range(27):  # Assuming a full inventory with 27 slots
        move_and_click(*enchant_spell_location)
        move_and_click(*bolts_location)
        random_delay(1, 2)  # Add delay between enchantments

# Start the script with a delay
print("Starting in 5 seconds...")
time.sleep(5)

# Call the main function
enchant_bolts()