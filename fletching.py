import pyautogui
import time
import random

# Constants for log types and their required levels
FLETCHING_LOGS = [
    {"name": "Normal Logs", "level": 1},
    {"name": "Oak Logs", "level": 20},
    {"name": "Willow Logs", "level": 35},
    {"name": "Maple Logs", "level": 50},
    {"name": "Yew Logs", "level": 65},
    {"name": "Magic Logs", "level": 85}
]

# Dummy function to check the player's fletching level (need to replace with actual implementation)
def get_fletching_level():
    # Implement level checking based on reading the game screen or using in-game data if available
    return 1  # Placeholder, return actual level dynamically as the state could be lost

# select the most efficient log type based on current level
def select_log():
    current_level = get_fletching_level()
    for log in reversed(FLETCHING_LOGS):
        if current_level >= log["level"]:
            return log["name"]
    return "Normal Logs"

# Function to move the character to a specific location, like the Grand Exchange (You can change this to anywhere but it needs to be next to a bank)
def move_to_grand_exchange():
    # Implement pathfinding and screen interactions to move the player
    print("Moving to the Grand Exchange...")
    # Example of a click on the minimap
    pyautogui.click(x=100, y=100)  # Replace with actual coordinates
    time.sleep(random.uniform(5, 10))  # Wait for character to move

# Function to perform the fletching action
def fletch_logs(log_type):
    print(f"Fletching {log_type}...")
    # Example: Click the logs in inventory, then select the bow option
    pyautogui.click(x=200, y=200)  # Click logs (replace with actual coordinates)
    time.sleep(random.uniform(0.5, 1.5))
    pyautogui.click(x=300, y=300)  # Click fletch option
    time.sleep(random.uniform(10, 20))  # Wait for fletching to complete

# Function to bank items (once-fletched, could work on also stringing all the bows once fletched but will have to come back to that)
def bank_items():
    print("Banking items...")
    pyautogui.click(x=400, y=400)  # Click on bank (replace with actual coordinates)
    time.sleep(random.uniform(1, 2))
    # Example: Deposit all items
    pyautogui.click(x=500, y=500)  # Click deposit button
    time.sleep(random.uniform(1, 2))

# Random misclicks to simulate human error (Lazy attempt at avoiding detection but worked for both accounts i got 99 fletching with)
def random_misclick():
    if random.random() < 0.1:  # 10% chance of misclick
        misclick_x = random.randint(-10, 10)
        misclick_y = random.randint(-10, 10)
        print(f"Performing a misclick at ({misclick_x}, {misclick_y})...")
        pyautogui.moveRel(misclick_x, misclick_y, duration=0.1)
        pyautogui.click()

# Main loop
def main():
    while True:
        move_to_grand_exchange()  # Move to Grand Exchange
        log_type = select_log()   # Select log type based on level
        fletch_logs(log_type)     # Fletch logs
        bank_items()              # Bank items
        random_misclick()         # Perform random misclicks
        time.sleep(random.uniform(2, 5))  # Random wait time between cycles

if __name__ == "__main__":
    main()
