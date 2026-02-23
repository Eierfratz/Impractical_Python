# Poor Man's Bar Chart

import pprint
from collections import defaultdict

def main():
    # 1. Get input from the user
    text = input("Enter text: ").lower()

    # 2. Use defaultdict to count letter frequency
    # We initialize it with 'list' so we can append the letters to create the bar
    stats = defaultdict(list)

    for char in text:
        if char.isalpha():  # We only care about letters, not spaces or punctuation
            stats[char].append(char)

    # 3. Use pprint to display the dictionary in an organized way
    print("\nLetter Frequency Bar Chart:\n")
    pprint.pprint(dict(stats), width=100)

print("You may need to stretch the console window if text wrapping occurs.")

if __name__ == "__main__":
    main()