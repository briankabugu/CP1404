"""
CP1404/CP5632 Practical
Quick Picks
"""

import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = 5
NUM_PER_QUICK_PICK = 6

def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)

# Function to generate a quick pick
def generate_quick_pick():
    numbers = []
    for i in range(NUM_PER_QUICK_PICK):
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)


# Function to display quick picks
def display_quick_picks(num_quick_picks):
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))

main()
    
