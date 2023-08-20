# user_input.py
import os
def get_name():
    user_name = input("Please enter your name: ")
    return user_name

def get_family_name():
    family_name = input("Please enter your family name: ")
    return family_name

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI escape code for green text
GREEN = '\033[92m'
# ANSI escape code to reset text color
RESET_COLOR = '\033[0m'    