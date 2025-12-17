import random
import time

dice = [1, 2, 3, 4, 5, 6]

def roll_dice():
    side_1 = random.choice(dice)
    side_2 = random.choice(dice)
    return side_1, side_2

def calculate(side_1, side_2):
    return side_1 + side_2

def main():
    print("Welcome to Dice game")
    n = int(input("How many rolls? "))

    frequency = {}  # dictionary to store sums

    for i in range(n):
        print("\nRolling Dice...")
        time.sleep(1)

        s1, s2 = roll_dice()
        total = calculate(s1, s2)

        print(f"Dice rolled: {s1} and {s2}")
        print(f"Sum: {total}")

        if total in frequency:
            frequency[total] += 1
        else:
            frequency[total] = 1

    print("\nFrequency of sums:")
    for total in sorted(frequency):
        print(f"Sum {total}: {frequency[total]} times")

main()
